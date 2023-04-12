"""
Copyright 2023 MITO-EK
This file is part of dhummat.
dhummat is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
dhummat is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with dhummat. If not, see <https://www.gnu.org/licenses/>.
"""

from . import inverif


def StandardFactor(n, flag):
    # Edge case 1.
    if n == 1:
        return "1 is neither prime nor composite, and its sole factor is 1."
    # Check up to sqrt(n), another factor can be found through division.
    mx = int(n ** .5)
    factors = []
    for i in range(1, mx + 1):
        # Formatting: if -d then add factors together in pairs.
        if n % i == 0:
            if flag:
                factors.append((i, int(n / i)))
            else:
                factors.append(i)
                if int(n / i) != mx:
                    factors.append(int(n / i))
    factors.sort()
    # Determine whether prime or composite number.
    t = "prime"
    if (not flag and len(factors) > 2) or (flag and len(factors) > 1):
        t = "composite"
    # Report result.
    return ("{} is {} with factors: {}".format(str(n), t,
                                               str(factors)[1:-1] + "."))


def PrimeFactor(n):
    # Edge case 1.
    if n == 1:
        return 1, 1
    # Dictionary that contains primes and their frequencies.
    f = {}
    # Total count of primes.
    lf = 0
    # Divide the lowest prime that divides m until m is reduced to a prime.
    # Add those results to the dictionary.
    m = int(n)
    k = 0
    while k != m:
        k = int(m)
        for i in range(2, int(m ** .5) + 1):
            if m % i == 0:
                try:
                    f[i] += 1
                except Exception as err:
                    f[i] = 1
                lf += 1
                m = int(m / i)
                break
    try:
        f[m] += 1
    except Exception as err:
        f[m] = 1
    lf += 1
    return f, lf


# Execute Factorization
def RunFactor(args):
    if not inverif.FactArgs(args, ['-p', '-d']):
        return "", ""
    # If there is a modifier tag.
    if len(args) > 2:
        # '-d', run standard factor formatted in pairs.
        if args[2] == '-d':
            return StandardFactor(int(args[1]), 1), ""
        else:
            # '-f' run prime factorization.
            f, lf = PrimeFactor(int(args[1]))
            if f == 1:
                return "1 is neither prime nor composite," +\
                       " and its sole factor is 1.", 1
            # Format result string from prime factorization.
            if lf == 1:
                return "{} is prime.".format(args[1]) +\
                       " Its prime factorization is itself.", int(args[1])
            res = args[1] + " is composite with prime factorization: "
            for p in f:
                if f[p] == 1:
                    res += "{} * ".format(str(p))
                else:
                    res += ("{}^{} * ".format(str(p), str(f[p])))
            return res[:-3], ""
    # Otherwise, standard factor with regular formatting.
    return StandardFactor(int(args[1]), 0), ""


# Calculates square root of n.
def Sqrt(n, d):
    if n == 1:
        return 1, 1
    # If '-d', just use the exponent and return the decimal square root.
    if d:
        ans = n ** .5
        # If perfect square, return an int instead.
        if ans == float(int(ans)):
            return int(ans), 1
        else:
            return ans, 1
    # Otherwise, format answer in the form outside * sqrt(inside)
    else:
        # Get the prime factorization of n.
        f, lf = PrimeFactor(n)
        outside = 1
        inside = 1
        # Separate even exponents out of the square root.
        for p in f:
            if f[p] % 2 == 1:
                inside *= p
            outside *= (p ** int(f[p] / 2))
        return outside, inside


# Execute Square Root.
def RunSqrt(args):
    if not (inverif.FactArgs(args, ['-d'])):
        return "", ""
    # '-d' flag is present, run with decimal output.
    if len(args) == 3:
        s, t = Sqrt(int(args[1]), True)
        return "sqrt({}) = {}".format(args[1], str(s)), s
    # Otherwise, run normally.
    s, t = Sqrt(int(args[1]), False)
    # Input was 1.
    if s == t and s == 1:
        return "sqrt(1) = 1", 1
    # Outside is 1, meaning prime factorization is all singleton integers.
    if s == 1:
        return "sqrt({}) = sqrt({})".format(args[1], str(t)), ""
    # Inside is 1, meaning number is a perfect square.
    if t == 1:
        return "sqrt({}) = {}".format(args[1], str(s)), s
    # Standard formatting: outside * sqrt(inside)
    return "sqrt({}) = {} * sqrt({})".format(args[1], str(s), str(t)), ""
