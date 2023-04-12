"""
Copyright 2023 MITO-EK
This file is part of dhummat.
dhummat is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
dhummat is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with dhummat. If not, see <https://www.gnu.org/licenses/>.
"""


# Single integer >= a
def SingleInt(args, a):
    # Command used by itself.
    if len(args) == 1:
        print("Usage: {} <n>".format(args[0]))
        return False
    # Too many inputs.
    if len(args) > 2:
        print("Error: Too many inputs.")
        return False
    # Verify input is an integer and >= a.
    try:
        check = int(args[1])
    except Exception as err:
        print("Error: \'{}\' is not an integer.".format(args[1]))
        return False
    if check < a:
        print("Error: Input must be >= {}.".format(str(a)))
        return False
    return True


# Two positive integers or one followed by flag -d if counting (com, per).
# Only two positive integers if not counting (pall, call).
def DoubleArg(args, counting):
    # Too many input.
    if len(args) > 3:
        print("Error: Too many inputs.")
        return False
    # Verify first input is a positive integer.
    try:
        check = int(args[1])
        if check < 1:
            print("Error: {} is not a positive integer.".format(args[1]))
            return False
    except Exception as err:
        print("Error: \'{}\' is not an integer.".format(args[1]))
        return False
    # Check whether 2nd argument is flag -d or a second positive integer.
    if counting and args[2] == '-d':
        return True
    else:
        try:
            check = int(args[2])
            if check < 1:
                print("Error: {} is not a positive integer.".format(args[2]))
                return False
        except Exception as err:
            print("Error: \'{}\' invalid 2nd argument.".format(args[2]))
            return False
    return True
