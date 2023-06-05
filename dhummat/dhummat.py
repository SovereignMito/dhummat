"""
Copyright 2023 SovereignMito
dhummat is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
dhummat is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with dhummat. If not, see <https://www.gnu.org/licenses/>.
"""

import sys, fileinput
from CommandSets import csman
from Operations import fileops, sign


# BEGIN PACKAGE MANAGEMENT
# Maps commands to info.
infos = {}
# Maps commands to their methods.
executables = {}
# Contains name of command set + commands.
titles = {}
# Import infos and executables from Command Sets.
infos, executables, titles = csman.ImportAll()
# END PACKAGE MANAGEMENT


# BEGIN HELPERS
# Run an executable command and record the response and signable output.
def Execute(cmd, pr):
    cmdx = sign.ReplaceSigns(cmd)
    if cmdx == "":
        return "", ""
    res, signout = executables[cmdx[0]](cmdx)
    if res != "":
        fileops.WriteOut(res, pr)
        if not fileops.hiding:
            print(res)
    if signout != "":
        sign.Sign('$', str(signout))
    return res, signout


# Takes an input string and splits it by chains ('>>').
def SplitInput(uin):
    out = []
    allin = uin.split(">>")
    for u in allin:
        formattedu = fileops.CleanInput(u)
        if formattedu == []:
            if len(allin) != 1:
                print("Error: Command is missing.")
            return []
        out.append(formattedu)
    return out


# Prints the command overview from using 'info' on its own.
def PrintInfo():
    print("List of Commands")
    print("Base Commands: info, exit")
    print("File Operations: inx, outx, outs, scr, hide")
    print("Sign Operations: sign, unsign")
    res = ""
    for cs in titles:
        print("{}{}".format(cs, titles[cs]))
# END HELPERS


# BEGIN SIGN
def ExSign(args, show):
    # Command is not sign <a> <command>, let the sign command set deal with it.
    if len(args) < 4 or args[0] == "unsign":
        if not fileops.hiding and show:
            print(" ".join(args))
        res = sign.RunSign(args)
        if res != "":
            if not fileops.hiding:
                print(res)
            fileops.WriteOut(res, " ".join(args) + '\n')
        else:
            return False
    else:
        # Input is sign <a> <command>.
        # Verify <a> is a-z, A-Z and <command> is valid executable.
        if not sign.ValidSign(args[1], True):
            return False
        if args[1] == '$':
            print("Error: Cannot write to special variable.")
            return False
        if not (args[2] in executables):
            print("Error: Command '{}' not recognized. Is it executable?"
                  .format(args[2]))
            return False
        if not fileops.hiding and show:
            print(" ".join(args))
        # Execute <command> to get printed response and returned value.
        res, signout = Execute(args[2:], " ".join(args[2:]) + '\n')
        if res == "":
            return False
        # Sign the value to the variable <a>.
        if signout != "":
            sign.Sign(args[1], str(signout))
            r = "{} = {}".format(args[1], str(signout))
            fileops.WriteOut(r, "")
            if not fileops.hiding:
                print(r)
        else:
            print("Error: Output is not supported for signing.")
            return False
    return True
# END SIGN


# BEGIN FILEOPS
# Run a command on the inputs in a file.
def InX(filename, args):
    # Get a list of inputs from the file.
    inputs = fileops.InCheck(filename, args, executables)
    if len(inputs) == 0:
        return
    # For every set of inputs combine it with the command then run the command.
    for i in inputs:
        if args[0] == '-c':
            cmd = [args[1]] + i + args[2:]
            if not fileops.hiding:
                print(" ".join(cmd))
        else:
            cmd = [args[0]] + i + args[1:]
        res, s = Execute(cmd, " ".join(cmd) + '\n')
        # If there's an error, stop executing on lines early.
        if res == "":
            print("Recognized error with input {}.".format(" ".join(i)))
            break


# Run a script: a file containing executable commands.
def Scr(filename, args):
    # Get list of raw lines from the file.
    cmds, printcmd, ignore = fileops.CheckScr(filename, args)
    if len(cmds) == 0:
        return
    # For every line in the file, execute it as if it were a command.
    for line in cmds:
        cmd = fileops.CleanInput(line)
        # Sign command.
        if cmd[0] == "sign" or cmd[0] == "unsign":
            if not ExSign(cmd, printcmd):
                if ignore:
                    continue
                print("Error in command {}".format(" ".join(cmd)))
                break
        else:
            # Regular executable.
            try:
                # Print command if "-c"
                if printcmd and not fileops.hiding:
                    print(line.split('\n')[0])
                # Decide how to print the command to a outx file.
                printline = line
                if fileops.OutSet(2) and line[-1] != '\n':
                    printline = line + '\n'
                # Run the command.
                res, s = Execute(cmd, printline)
                if res == "":
                    if ignore:
                        continue
                    print("Error in command {}".format(" ".join(cmd)))
                    break
            except Exception as err:
                print("Command \'" + cmd[0] + "\' is not executable.")
                if ignore:
                    continue
                print("Error in command {}".format(" ".join(cmd)))
                break


# File operation commands
fileopscmd = {
    'inx': [InX, "Usage: inx <f> <command>"],
    'outx': [fileops.OutX, "Usage: outx <f> <type> <modifier>"],
    'outs': [fileops.OutS],
    'scr': [Scr, "Usage: scr <f> <modifier>"],
    'hide': [""]
}
# END FILEOPS


# BEGIN EXECUTION
# Prints info of a command to console.
def GetInfo(un):
    if len(un) == 1:
        PrintInfo()
    elif len(un) > 2:
        print("Error: Too many arguments.")
    else:
        try:
            print(infos[un[1]])
        except Exception as err:
            print("Command \'" + un[1] + "\' not recognized.")


# Decides whether to quit the main input loop.
quit = False
# Build an input string from command line argument.
precharge_data = ""
if len(sys.argv) == 2:
    precharge_data += sys.argv[1]
elif len(sys.argv) > 2:
    print("Error: Too many arguments. Check that the command is in quotes.")
    quit = True

if not quit:
    # Build an input string from stdin only if no terminal argument specified.
    if not sys.stdin.isatty() and precharge_data == "":
        precharge_data = '>>'.join(list(fileinput.input()))

    # Only print splash prompt when no arguments are used for execution.
    if precharge_data == "":
        print("dhummat Command Set Math Tool.\nVersion 1.2\nUse info for help.")

# Main input loop.
while not quit:
    # If input is prefilled, run that.
    if precharge_data != "":
        quit = True
        userl = SplitInput(precharge_data)
    # Otherwise, collect user input and separate it into individual commands.
    else:
        try:
            userl = SplitInput(input("dhummat> "))
        except EOFError as err:
            quit = True
            userl[:] = []
    # Scan individual commands in between chains.
    for userin in userl:
        if len(userin) == 0:
            continue
        # Exit command.
        elif (userin[0] == 'exit'):
            quit = True
            break
        # Info command.
        elif (userin[0] == 'info'):
            GetInfo(userin)
        # File Operation.
        elif (userin[0] in fileopscmd):
            if (userin[0] == 'hide'):
                fileops.SwitchHide(userin)
            elif (userin[0] == 'outs'):
                fileops.OutS(userin)
            elif (len(userin) >= 2):
                fileopscmd[userin[0]][0](userin[1], userin[2:])
            else:
                print(fileopscmd[userin[0]][1])
        # Sign Operation
        elif (userin[0] == "sign" or userin[0] == "unsign"):
            ExSign(userin, False)
        # Regular executable command.
        else:
            try:
                Execute(userin, " ".join(userin) + '\n')
            except KeyError as err:
                print("Command \'" + userin[0] + "\' not recognized.")
            except Exception as err:
                print("An unexpected error has occurred.")
# END EXECUTION
