"""
Copyright 2023 MITO-EK
This file is part of dhummat.
dhummat is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
dhummat is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with dhummat. If not, see <https://www.gnu.org/licenses/>.
"""

# FORMAT: from CommandSets.<CommandSet Folder name> import <file containing infos and executables dicts>
from CommandSets.FactorSet import factorsetinfos
from CommandSets.CombosSet import combossetinfos


# Operational Command Set Infos
baseinfos = {
    'info': "You're very funny, you know that?\nSyntax: info\nPrints a list of commands to the screen.\nSyntax: info <command>\nProvides information on the function and usage of <command>.",
    'exit': "Syntax: exit\nExit the current instance of the program.",
    'inx': "Syntax: inx <f> <-c> <command>\nRuns <command> on the inputs in file <f>. <f> is a file that contains the appropriate inputs for the command.\n<command> can be run multiple times for multiple inputs by separating them with a newline in <f>.\n-c: Also print the command constructed from including the inputs.",
    'outx': "Syntax: outx <f> <type> <modifiers>\nCauses subsequent successful output of executable commands to be printed to file <f>.\n<type>:\n-t: truncates file <f>, adding any output to the end of the file if it already exists. Default option if <type> is not specified.\n-o: overwrites file <f> if it already exists.\n<modifiers>:\n-c: additionally prints the source command of the output to the file.\n-h: quick trigger for the hide command.",
    'outs': "Syntax: outs <-h>\nStops writing output to the file specified by outx and closes that file for writing.\n-h: quick trigger for the hide command.",
    'scr': "Syntax: scr <f> <modifiers>\nRuns all commands in script file <f>. A script file contains, line by line, commands as if they were written into the console manually.\n<modifiers>:\n-c: prints a command to the screen when it is being run.\n-i: ignore errors if they occur and continue.",
    'hide': "Syntax: hide\nToggles hiding. While hiding is active, hides successful output of commands from the screen. Errors are still displayed.\nThe -h modifier of outx and outs can be used to invoke this command without typing it out on its own.",
    'sign': "Syntax: sign\nReturns a list of all currently signed variables and their values.\n\nSyntax: sign <a> <command>\nTakes the result of executable <command> and signs it to variable <a>.\n\nSyntax: sign <a>\nReturns the current value signed to <a>, if applicable.\n\nSyntax: sign <a> <n>\nSigns numerical value <n> to <a>.\n\nSyntax: sign <a> <b>\nCopies the value signed to <a> onto <b>.",
    'unsign': "Syntax: unsign <a>\nDeletes variable <a> and the value signed to it, if applicable."
}

# External Command Set infos, executables, and titles.
# Add or exclude command set labels here.
infopackages = [factorsetinfos.packageinfos, combossetinfos.packageinfos]
exepackages = [factorsetinfos.packageexes, combossetinfos.packageexes]
titlepackages = [factorsetinfos.packagetitles, combossetinfos.packagetitles]


# Import all infos, executables, and titles from Command Set
# packages using the lists above.
def ImportAll():
    allinfos = baseinfos
    allexes = {}
    alltitles = {}
    for pkg in infopackages:
        allinfos.update(pkg)
    for pkg in exepackages:
        allexes.update(pkg)
    for pkg in titlepackages:
        alltitles.update(pkg)
    return allinfos, allexes, alltitles
