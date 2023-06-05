"""
Copyright 2023 SovereignMito
This file is part of dhummat.
dhummat is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
dhummat is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with dhummat. If not, see <https://www.gnu.org/licenses/>.
"""

from . import inverif


# GCD of two integers.
def GCD(n, m):
    # Sort the largest of the two integers to be first.
    if abs(n) > abs(m):
        x = abs(n)
        y = abs(m)
    else:
        x = abs(m)
        y = abs(n)
    z = 1
    # Apply Euclidean algorithm.
    while y != 0:
        z = x % y
        x = y
        y = z
    return x


# LCM of two integers.
def LCM(n, m):
    # Edge case n = m = 0
    if n == 0 and m == 0:
        return 0
    # Derive LCM from the GCD
    g = GCD(n, m)
    return int(abs(n)*(abs(m)/g))


def RunGCD(args):
    # Verify arguments.
    if not inverif.MultiIntArgs(args):
        return "", ""
    # Get gcd of first two integers.
    g = GCD(int(args[1]), int(args[2]))
    # Perform a fold if more than two integers.
    if (len(args) > 3):
        for h in args[3:]:
            g = GCD(g, int(h))
    # Build output string.
    ans = "gcd("
    for y in args[1:]:
        ans += (y + ", ")
    return (ans[:-2] + ") = " + str(g)), g


def RunLCM(args):
    # Verify arguments.
    if not inverif.MultiIntArgs(args):
        return "", ""
    # Get lcm of first two integers.
    low = LCM(int(args[1]), int(args[2]))
    # Perform a fold if more than two integers.
    if (len(args) > 3):
        for m in args[3:]:
            low = LCM(low, int(m))
    # Build output string.
    ans = "lcm("
    for y in args[1:]:
        ans += (y + ", ")
    return (ans[:-2] + ") = " + str(low)), low


def RunSimp(args):
    # Verify arguments are exactly 2 integers.
    if not inverif.TwoIntArgs(args):
        return "", ""
    # Get the gcd of the numerator and denominator.
    n = int(args[1])
    d = int(args[2])
    if d == 0:
        print("Error: Denominator is zero.")
        return "", ""
    g = GCD(n, d)
    # If gcd is 1 then fraction already simplified.
    if g == 1:
        return ("{}/{} is already in simplest form.")\
               .format(args[1], args[2]), ""
    # Otherwise, divide both numerator and denominator by the gcd.
    n = int(n / g)
    d = int(d / g)
    return ("{}/{} = {}/{}").format(args[1], args[2], str(n), str(d)), ""
