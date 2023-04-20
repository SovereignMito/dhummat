"""
Copyright 2023 MITO-EK
This file is part of dhummat.
dhummat is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
dhummat is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with dhummat. If not, see <https://www.gnu.org/licenses/>.
"""


# Verify all items in a list are numbers, then convert them to ints or floats.
def AllNumCheck(args, intsonly):
    # Command used by itself.
    if len(args) == 1:
        buffer = ""
        if args[0] == "div":
            buffer = " <-r> <m>"
        print("Usage: {} <a1> <a2> ... <an>{}".format(args[0], buffer))
        return [], 0
    # list of ints/floats.
    nums = []
    # Amount to round by to remove imprecisions.
    r = -1
    # Track index of number loop.
    p = 1
    while p < len(args):
        # Found values after a rounding value has been set (division).
        if r >= 0:
            print("Error: Garbage found after round value.")
            return [], r
        n = args[p]
        # Set the rounding value on encountering '-r' (division).
        if args[0] == 'div' and n == '-r' and len(nums) > 0:
            try:
                p += 1
                r = int(args[p])
            except Exception as err:
                print("Error: Missing or invalid round value.")
                return [], r
        # Otherwise, convert to int/float and add to number list.
        else:
            try:
                if intsonly:
                    nums.append(int(n))
                else:
                    nums.append(float(n))
            except Exception as err:
                if intsonly:
                    print("Error: {} is not an integer.".format(n))
                else:
                    print("Error: {} is not a number.".format(n))
                return [], r
        p += 1
    # Set initial rounding value to zero for non-division operations.
    if args[0] != 'div':
        r = 0
    return nums, r


# Round input verification. One float then one integer >= 0.
def RoundArgs(args):
    if len(args) == 1:
        print("Usage: round <n> <r>")
        return False
    if len(args) == 2:
        print("Error: Missing round value.")
        return False
    if len(args) > 3:
        print("Error: Too many arguments.")
        return False
    try:
        n = float(args[1])
        if n == float('inf') or n == float('-inf') or n != n:
            print("Error: Illegal input (infinity, NaN).")
            return False
    except Exception as err:
        print("Error: {} is not a number.".format(args[1]))
        return False
    try:
        r = int(args[2])
        if r < 0:
            print("Error: Rounding value is negative.")
            return False
    except:
        print("Error: {} is not an integer.".format(args[2]))
        return False
    return True


# Floor/Ceil input verification. Checks for exactly one float argument.
def OneFloat(args):
    if len(args) == 1:
        print("Usage: {} <n>".format(args[0]))
        return False
    if len(args) > 2:
        print("Error: Too many arguments.")
        return False
    try:
        n = float(args[1])
        if n == float('inf') or n == float('-inf') or n != n:
            print("Error: Illegal input (infinity, NaN).")
            return False
    except Exception as err:
        print("Error: {} is not a number.".format(args[1]))
        return False
    return True
