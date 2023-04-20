"""
Copyright 2023 MITO-EK
This file is part of dhummat.
dhummat is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
dhummat is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with dhummat. If not, see <https://www.gnu.org/licenses/>.
"""

from . import inverif
from . import helpers
import operator as op


# Perform the arithmetic operation.
def Operate(s, a, operation):
    try:
        t = operation(s, a)
        if t == float('inf') or t == float('-inf'):
            raise OverflowError
        if t != t:
            raise ValueError
    except OverflowError as err:
        print("Error: Overflow.")
        return ""
    except ZeroDivisionError as err:
        print("Error: Divide by zero.")
        return ""
    except ValueError as err:
        print("Error: Illegal operation resulting in NaN output.")
        return ""
    except Exception as err:
        print("Error: An unexpected arithmetic error has occurred.")
        return ""
    return t


def AddAll(args):
    # Convert arguments to list of floats.
    nums, r = inverif.AllNumCheck(args, False)
    if len(nums) == 0:
        return "", ""
    # Starting sum.
    s = 0
    # For every input, add it to the sum.
    for n in nums:
        s = Operate(s, n, op.add)
        if s == "":
            return "", ""
        # Highest # of decimal places = input with the most decimal places.
        dp = helpers.CalcPlaces(n)
        r = max(r, dp)
    # Round to remove floating point inaccuracies.
    s = round(s, r)
    s = helpers.FormatIntFloat(s)
    return str(s), s


def SubAll(args):
    # Convert arguments into list of floats.
    nums, r = inverif.AllNumCheck(args, False)
    if len(nums) == 0:
        return "", ""
    # Starting difference.
    s = "start"
    for n in nums:
        # Set first argument to starting difference.
        if s == "start":
            s = Operate(n, 0, op.add)
        # For every other argument, subtract it from the difference.
        else:
            s = Operate(s, n, op.sub)
        if s == "":
            return "", ""
        # Highest # of decimal places = input with the most decimal places.
        dp = helpers.CalcPlaces(n)
        r = max(r, dp)
    # Round to remove floating point inaccuracies.
    s = round(s, r)
    s = helpers.FormatIntFloat(s)
    return str(s), s


def MultAll(args):
    # Convert arguments into list of floats.
    nums, r = inverif.AllNumCheck(args, False)
    if len(nums) == 0:
        return "", ""
    # Starting product.
    s = 1
    # Multiply every input to build a product.
    for n in nums:
        s = Operate(s, n, op.mul)
        if s == "":
            return "", ""
        # Highest # of decimal places = sum of # decimal places of all inputs.
        r += helpers.CalcPlaces(n)
    # Round to remove floating point inaccuracies.
    s = round(s, r)
    s = helpers.FormatIntFloat(s)
    return str(s), s


def DivAll(args):
    # Convert arguments into list of floats.
    nums, r = inverif.AllNumCheck(args, False)
    if len(nums) == 0:
        return "", ""
    # Starting quotient.
    s = "start"
    for n in nums:
        # Set first argument as starting quotient.
        if s == "start":
            s = Operate(0, n, op.add)
        # For every other argument, perform division.
        else:
            s = Operate(s, n, op.truediv)
        if s == "":
            return "", ""
    # Only round if '-r' was present.
    if r >= 0:
        s = round(s, r)
    s = helpers.FormatIntFloat(s)
    return str(s), s


def ModAll(args):
    # Convert arguments into list of ints.
    nums, r = inverif.AllNumCheck(args, True)
    if len(nums) == 0:
        return "", ""
    # Staring modulus.
    s = "start"
    for n in nums:
        # Set first argument as the starting modulus.
        if s == "start":
            s = Operate(0, n, op.add)
        # For other inputs, perform s % new input.
        else:
            s = Operate(s, n, op.mod)
        if s == "":
            return "", ""
    return str(s), s


def PowAll(args):
    # Convert arguments to list of floats.
    nums, r = inverif.AllNumCheck(args, False)
    if len(nums) == 0:
        return "", ""
    # Starting answer.
    s = "start"
    for n in nums:
        # Set first argument as starting answer.
        if s == "start":
            s = Operate(0, n, op.add)
        # For other arguments, exponentiate.
        else:
            s = Operate(s, n, op.pow)
        if s == "":
            return "", ""
    s = helpers.FormatIntFloat(s)
    return str(s), s
