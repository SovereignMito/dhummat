"""
Copyright 2023 MITO-EK
This file is part of dhummat.
dhummat is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
dhummat is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with dhummat. If not, see <https://www.gnu.org/licenses/>.
"""

from . import pccalc, pclist


packageinfos = {
    'fac': "Syntax: fac <n>\nCalculates <n> factorial. <n> is an integer greater than or equal to zero.",
    'com': "Syntax: com <n> <-d>\nCalculates the number of combinations (of any length) that can be made from <n> objects. <n> is a positive integer.\nOptional flag <-d> lists the quantities of each combination by length.\nSyntax: com <k> <n>\nCalculates the number of combinations of length <k> from <n> objects. <n> and <k> are both positive integers.",
    'per': "Syntax: per <n> <-d>\nCalculates the number of permutations (of any length) that can be made from <n> objects. <n> is a positive integer.\nOptional flag <-d> lists the quantities of each permutation by length.\nSyntax: per <k> <n>\nCalculates the number of permutations of length <k> from <n> objects. <n> and <k> are both positive integers.",
    'call': "Syntax: call <n>\nFinds all possible combinations (of any length) of a set of natural numbers from 1 to <n>, sorted by length. <n> is a natural number.\n\nSyntax: call <k> <n>\nFinds all possible combinations of length <k> of a set of natural numbers from 1 to <n>. <n> is a natural number. <k> must be a positive integer.",
    'pall': "Syntax: pall <n>\nFinds all possible permutations (of any length) of a set of natural numbers from 1 to <n>, sorted by length. <n> is a natural number.\n\nSyntax: pall <k> <n>\nFinds all possible permutations of length <k> of a set of natural numbers from 1 to <n>. <n> is a natural number. <k> must be a positive integer."
}

packageexes = {
    'fac': pccalc.RunFac,
    'com': pccalc.RunCom,
    'per': pccalc.RunPer,
    'call': pclist.RunCall,
    'pall': pclist.RunPall
}

packagetitles = {
    'Combos Command Set: ': 'fac, per, com, pall, call'
}
