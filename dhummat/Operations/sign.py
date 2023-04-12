"""
Copyright 2023 MITO-EK
This file is part of dhummat.
dhummat is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
dhummat is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with dhummat. If not, see <https://www.gnu.org/licenses/>.
"""


# Maps variables to signed values.
signs = {}


# Check that A is a letter from a-z or A-Z.
def ValidSign(A, p):
    try:
        if (ord(A) >= 65 and ord(A) <= 90) or (ord(A) >= 97 and ord(A) <= 122):
            return True
        elif p:
            print("Error: {} must be between a-z or A-Z.".format(A))
    except Exception as err:
        if p:
            print("Error: {} must be a single character.".format(A))
    return False


# Return all signed variables.
def SignAll():
    if len(signs) == 0:
        return "No variables are signed."
    res = ""
    for sign in signs:
        res += "{}: {}\n".format(sign, str(signs[sign]))
    return res[:-1]


# Signs an integer or float n to A.
def Sign(A, n):
    try:
        signs[A] = int(n)
    except Exception as err:
        try:
            signs[A] = float(n)
        except Exception as err:
            print("Error: {} is not a numerical value.".format(n))
            return False
    return True


# Copies the value signed to A to B.
def SignCopy(A, B):
    try:
        signs[B] = signs[A]
    except Exception as err:
        print("Error: Could not copy, check that {} is signed.".format(A))
        return False
    return True


# Delete variable A.
def Unsign(A):
    try:
        del signs[A]
    except Exception as err:
        print("Error: {} not signed.".format(A))
        return False
    return True


# Return the value signed to A.
def GetSign(A):
    try:
        return signs[A]
    except Exception as err:
        print("Error: {} not signed.".format(A))
        return None


# Main execution of sign commands.
def RunSign(args):
    # sign or unsign by itself. (SignAll/Print Unsign prompt)
    if len(args) == 1:
        if args[0] == "sign":
            return SignAll()
        if args[0] == "unsign":
            return "Usage: unsign <a>"
    A = args[1]
    # sign/unsign with a single variable argument. (GetSign/Unsign)
    if len(args) == 2 and ValidSign(A, True):
        if args[0] == "sign":
            a = GetSign(A)
            if a is not None:
                return "{}: {}".format(A, str(a))
            return ""
        elif args[0] == "unsign" and Unsign(A):
            return "Deleted {}".format(A)
        else:
            return ""
    # sign with a variable and a numerical value/another variable.
    elif len(args) == 3 and ValidSign(A, True):
        if args[0] == "sign":
            bn = args[2]
            if ValidSign(bn, False):
                if SignCopy(A, bn):
                    return "{} = {}".format(bn, str(GetSign(A)))
            else:
                if Sign(A, bn):
                    return "{} = {}".format(A, bn)
        if args[0] == "unsign":
            print("Error: Too many arguments.")
            return ""
    elif len(args) > 3:
        print("Error: Too many arguments.")
    return ""


# Takes a list of arguments and replaces all variables with signed values.
def ReplaceSigns(args):
    sargs = args.copy()
    i = 0
    while i < len(sargs):
        if ValidSign(sargs[i], False):
            sargs[i] = str(GetSign(sargs[i]))
            if sargs[i] == 'None':
                return ""
        i += 1
    return sargs
