"""
Copyright 2023 MITO-EK
This file is part of dhummat.
dhummat is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
dhummat is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with dhummat. If not, see <https://www.gnu.org/licenses/>.
"""

from . import inverif


# Table that remembers past factorials.
factable = [1, 1]
facs = 1


# n factorial.
def Fac(n):
    global facs
    global factable
    # Search the fact table for the answer.
    # If it doesn't exist, generate factorials up to n.
    while facs < n:
        factable.append(factable[facs] * (facs + 1))
        facs += 1
    return factable[n]


# Number of k-permutations.
def KPer(k, n, f):
    o = ""
    # Can't make a permutation of size k if k > n.
    if k > n:
        return 0
    a = int(Fac(n)/Fac(n - k))
    # If '-d', print the k-permutation information.
    if f:
        o += "{}-perms: {}\n".format(str(k), str(a))
    return a, o


# Number of k-combinations.
def KCom(k, n, f):
    o = ""
    # Can't make a combination of size k if k > n.
    if k > n:
        return 0
    a = int(Fac(n)/(Fac(n - k) * Fac(k)))
    # If '-d', print the k-combination information.
    if f:
        o += "{}-combs: {}\n".format(str(k), str(a))
    return a, o


# Find total number of permutations for n objects.
def Per(n, f):
    out = ""
    k = 1
    s = 0
    # Add up k-permutations up to n.
    while k < n + 1:
        a, o = KPer(k, n, f)
        s += a
        out += o
        k += 1
    return s, out


# Find total number of combinations for n objects.
def Com(n, f):
    out = ""
    k = 1
    s = 0
    # Add up k-combinations up to n.
    while k < n + 1:
        a, o = KCom(k, n, f)
        s += a
        out += o
        k += 1
    return s, out


# Verify input is a single integer that is >= 0 then report n!.
def RunFac(args):
    if not inverif.SingleInt(args, 0):
        return "", ""
    f = Fac(int(args[1]))
    return "{}! = {}".format(args[1], str(f)), f


# Execute combination counting command.
def RunCom(args):
    # Command used by itself.
    if len(args) == 1:
        print("Usage: com <n> <-d>\nUsage: com <k> <n>")
        return "", ""
    # Command used with one integer.
    if len(args) == 2 and inverif.SingleInt(args, 1):
        coms, o = Com(int(args[1]), False)
        return "{} total combinations from {} objects."\
               .format(str(coms), args[1]), coms
    # Command used with two arguments.
    if len(args) > 2 and inverif.DoubleArg(args, True):
        # Single integer and flag '-d'
        if args[2] == '-d':
            coms, o = Com(int(args[1]), True)
            return o + "{} total combinations from {} objects."\
                       .format(str(coms), args[1]), coms
        # Two integers k and n.
        else:
            coms, o = KCom(int(args[1]), int(args[2]), False)
            return "{} {}-combinations from {} objects."\
                   .format(str(coms), args[1], args[2]), coms
    return "", ""


# Execute permutation counting command.
def RunPer(args):
    # Command used by itself.
    if len(args) == 1:
        print("Usage: per <n> <-d>\nUsage: per <k> <n>")
        return "", ""
    # Command used with one integer.
    if len(args) == 2 and inverif.SingleInt(args, 1):
        pers, o = Per(int(args[1]), False)
        return "{} total permutations from {} objects."\
               .format(str(pers), args[1]), pers
    # Command used with two arguments.
    if len(args) > 2 and inverif.DoubleArg(args, True):
        # Single integer with flag '-d'
        if args[2] == '-d':
            pers, o = Per(int(args[1]), True)
            return o + "{} total permutations from {} objects."\
                       .format(str(pers), args[1]), pers
        # Two integers k and n.
        else:
            pers, o = KPer(int(args[1]), int(args[2]), False)
            return "{} {}-permutations from {} objects."\
                   .format(str(pers), args[1], args[2]), pers
    return "", ""
