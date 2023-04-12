"""
Copyright 2023 MITO-EK
This file is part of dhummat.
dhummat is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
dhummat is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with dhummat. If not, see <https://www.gnu.org/licenses/>.
"""


# Verify a single natural number with a single valid flag (or none).
def FactArgs(args, validflags):
    # Verify correct number of arguments.
    if len(args) == 1:
        print("Usage: {} <n> <modifier>".format(args[0]))
        return False
    elif len(args) > 3:
        print("Error: Too many arguments.")
        return False
    # Check that input is a positive integer.
    try:
        checknum = int(args[1])
        if checknum <= 0:
            print("Error: Input must be a positive integer.")
            return False
    except Exception as err:
        print("Error: \'{}\' is not an integer.".format(args[1]))
        return False
    # Check that the modifier value is valid.
    if len(args) == 3:
        if not (args[2] in validflags):
            print("Error: Unrecognized argument \'{}\'.".format(args[2]))
            return False
    return True


# Verify that input arguments are exactly 2 integers.
def TwoIntArgs(args):
    # Command with no arguments.
    if len(args) == 1:
        print("Usage: " + args[0] + " <int> <int>")
        return False
    # Only one argument.
    elif len(args) < 3:
        print("Error: Missing inputs.")
        return False
    # More than 2 arguments.
    elif len(args) > 3:
        print("Error: Too many inputs.")
        return False
    # Check that arguments are integers.
    try:
        check = int(args[1])
        check = int(args[2])
    except Exception as err:
        print("Error: One or more inputs is not an integer.")
        return False
    return True


# Verify input is 2 or more integers.
def MultiIntArgs(args):
    # Command with no arguments.
    if len(args) == 1:
        print("Usage: " + args[0] + " <int> <int> ... <int>")
        return False
    # Less than two arguments provided.
    elif len(args) < 3:
        print("Error: Not enough input.")
        return False
    # Verify all arguments are integers.
    for arg in args[1:]:
        try:
            check = int(arg)
        except Exception as err:
            print(("Error: \'{}\' is not an integer.").format(arg))
            return False
    return True
