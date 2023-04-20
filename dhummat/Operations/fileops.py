"""
Copyright 2023 MITO-EK
This file is part of dhummat.
dhummat is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
dhummat is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with dhummat. If not, see <https://www.gnu.org/licenses/>.
"""


# Convert input into list of tokens, removing newlines at the end.
def CleanInput(un):
    unn = un.split(" ")
    tkns = []
    for tkn in unn:
        if tkn != '' and tkn != '\n':
            tkns.append(tkn.split('\n')[0])
    return tkns


# [file to output to, do we output to file?, do we write command?]
outsettings = [None, False, False]
# Don't display output to the screen.
hiding = False


def OutSet(x):
    return outsettings[x]


# Switch hiding on or off.
def SwitchHide(args):
    global hiding
    if len(args) > 1:
        print("Error: Too many arguments.")
        return
    if hiding:
        print("Stopped hiding output.")
        hiding = False
    else:
        print("Now hiding output.")
        hiding = True


# Stop writing to a file.
def OutS(args):
    global outsettings
    # Input validation.
    if len(args) > 2:
        print("Error: Too many arguments.")
        return
    # Check that if there is a flag that it is only '-h' to enable hiding.
    toHide = False
    if len(args) == 2:
        if args[1] == "-h":
            toHide = True
        else:
            print("Error: Invalid argument.")
            return
    # Check that an output file is open.
    if not OutSet(1):
        print("No file open.")
        return
    # Close the file and disable all output settings.
    outsettings[0].close()
    outsettings[0] = None
    outsettings[1] = False
    outsettings[2] = False
    print("File Closed")
    # Trigger hiding command if '-h'
    if toHide:
        SwitchHide([])


# Redirect output to a file.
def OutX(filename, args):
    global outsettings
    # flag parameters
    toHide = False
    overwrite = 'a'
    # Input validation.
    if len(args) > 3:
        print("Error: Extraneous arguments.")
        return
    # -t, -o, -c, or -h.
    elif len(args) == 1:
        if args[0] == '-o':
            overwrite = 'w'
        elif args[0] == '-c':
            outsettings[2] = True
        elif args[0] == '-h':
            toHide = True
        elif args[0] != '-t':
            print("Error: Invalid argument.")
            return
    # -t/-o and -c/-h or both -c and -h.
    elif len(args) == 2:
        # -o/-t -c/-h
        if args[0] == '-o' or args[0] == '-t':
            if args[0] == '-o':
                overwrite = 'w'
            if args[1] == '-c':
                outsettings[2] = True
            elif args[1] != '-h':
                print("Error: Invalid argument.")
                return
            else:
                toHide = True
        # -c -h
        elif args[0] == '-c':
            if args[1] != '-h':
                print("Error: Invalid argument.")
                return
            toHide = True
            outsettings[2] = True
        # -h -c
        elif args[0] == '-h':
            if args[1] != '-c':
                print("Error: Invalid argument.")
                return
            toHide = True
            outsettings[2] = True
        else:
            print("Error: Invalid argument.")
            return
    # All 3 arguments
    elif len(args) == 3:
        if args[0] == '-o':
            overwrite = 'w'
        elif args[0] != '-t':
            print("Error: Invalid argument.")
            return
        if (args[1] == '-c' and args[2] == '-h') or\
           (args[1] == '-h' and args[2] == '-c'):
            outsettings[2] = True
            toHide = True
        else:
            print("Error: Invalid argument.")
            return
    # Close the previous file first.
    if OutSet(1):
        OutS([])
    # Attempt to open file.
    try:
        outsettings[0] = open(filename, overwrite)
    except Exception as err:
        print("Error: {} could not be opened.".format(filename))
        return
    # Set file on.
    print("{} set successfully.".format(filename))
    outsettings[1] = True
    # Trigger hiding function if '-h'
    if toHide:
        SwitchHide([])


# Validate and generate a list of inputs from a file.
def InCheck(filename, args, exe):
    global outsettings
    # Input validation.
    if len(args) == 0:
        print("Error: No command supplied.")
        return []
    if args[0] == '-c':
        if len(args) == 1:
            print("Error: No command supplied.")
            return []
        if not (args[1] in exe):
            print("Command \'" + args[1] + "\' not recognized.")
            return []
    elif not (args[0] in exe):
        print("Command \'" + args[0] + "\' not recognized.")
        return []
    # Open file for reading.
    try:
        f = open(filename)
    except Exception as err:
        print("Error: {} could not be opened.".format(filename))
        return []
    # Generate a list of inputs.
    inputs = []
    for line in f:
        if len(line.split('\n')[0]) == 0:
            continue
        inputs.append(CleanInput(line))
    f.close()
    return inputs


# Validate and get raw lines from a script file.
def CheckScr(filename, args):
    global outsettings
    flag = False
    ig = False
    # Input validation.
    if len(args) > 2:
        print("Error: Extraneous arguments.")
        return [], flag, ig
    if len(args) == 1:
        if args[0] == '-c':
            flag = True
        elif args[0] == '-i':
            ig = True
        else:
            print("Error: invalid argument {}.".format(args[0]))
            return [], flag, ig
    if len(args) == 2:
        if (args[0] == '-c' and args[1] == '-i') or\
           (args[0] == '-i' and args[1] == '-c'):
            flag = True
            ig = True
        else:
            print("Error: invalid argument.")
            return [], flag, ig
    # Attempt to open the file for reading.
    try:
        f = open(filename)
    except Exception as err:
        print("Error: {} could not be opened.".format(filename))
        return [], flag, ig
    # Get raw lines from the file into a list.
    lines = []
    for line in f:
        if len(line.split('\n')[0]) == 0:
            continue
        lines.append(line)
    f.close()
    return lines, flag, ig


# Write response to the output file if set.
def WriteOut(res, pr):
    if OutSet(1):
        # Write the command.
        if OutSet(2):
            outsettings[0].write(pr)
        # Write the result.
        outsettings[0].write(res + '\n')
