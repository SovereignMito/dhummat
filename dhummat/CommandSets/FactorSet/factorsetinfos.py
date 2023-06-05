"""
Copyright 2023 SovereignMito
This file is part of dhummat.
dhummat is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
dhummat is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with dhummat. If not, see <https://www.gnu.org/licenses/>.
"""

from . import facterialize, gcl


packageinfos = {
    'factor': "Syntax: factor <n> <modifier>\nTakes a natural number <n> and returns its factors, or all natural numbers that divide n.\nmodifier:\n-d: returns the factors in the form of product pairs.\n-p: performs a *prime factorization*, reducing `n` to a product of prime numbers.\nSigning: Return value not signable.",
    'gcd': "Syntax: gcd <int> <int> ... <int>\nFinds the greatest common divisor of at least two integers.\nSigning: Integer.",
    'lcm': "Syntax: lcm <int> <int> ... <int>\nFinds the least common multiple of of at least two integers.\nSigning: Integer.",
    'simp': "Syntax: simp <n> <d>\nSimplifies a fraction of numerator <n> and denominator <d>.\n<n> and <d> must be integer values and <d> cannot be zero.\nSigning: Return value not signable.",
    'sqrt': "Syntax: sqrt <n> <-d>\nFinds the square root of positive integer <n> and returns it in a * sqrt(b) formatting.\n<-d>: display the result as a decimal instead.\nSigning: If n is a perfect square, an integer. If -d, an integer or a float."
}

packageexes = {
    'factor': facterialize.RunFactor,
    'gcd': gcl.RunGCD,
    'lcm': gcl.RunLCM,
    'simp': gcl.RunSimp,
    'sqrt': facterialize.RunSqrt
}

packagetitles = {
    'Factor Command Set: ': 'factor, gcd, lcm, simp, sqrt'
}
