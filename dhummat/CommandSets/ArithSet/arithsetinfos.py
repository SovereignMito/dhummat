"""
Copyright 2023 SovereignMito
This file is part of dhummat.
dhummat is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
dhummat is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with dhummat. If not, see <https://www.gnu.org/licenses/>.
"""

from . import arith, rounding


packageinfos = {
    'add': "Syntax: add <a1> <a2> ... <an>\nCalculates the sum of numerical values <a1> to <an>.\nSigning: Integer or float.",
    'sub': "Syntax: sub <a1> <a2> ... <an>\nCalculates the total difference of numerical values <a1> to <an> from left to right.\nSigning: Integer or float.",
    'mult': "Syntax: mult <a1> <a2> ... <an>\nCalculates the product of numerical values <a1> to <an>.\nSigning: Integer or float.",
    'div': "Syntax: div <a1> <a2> ... <an> <-r> <m>\nCalculates the quotient of numerical values <a1> to <an> from left to right.\n(Optional) -r: round the answer to m decimal places.\nSigning: Integer or float.",
    'mod': "Syntax: mod <a1> <a2> ... <an>\nCalculates <a1> mod <a2> ... mod <an> of integers <a1> to <an>.\nSigning: Integer.",
    'pow': "Syntax: pow <a1> <a2> ... <an>\nTakes <a1> and exponentiates it by <a2> ... <an> from left to right.\nSigning: Integer or float.",
    'round': "Syntax: round <n> <r>\nRounds numerical value <n> to <r> decimal places.\n<r> is an integer greater than or equal to zero.\nSigning: Integer or float.",
    'floor': "Syntax: floor <n>\nReturns the floor of numerical value <n>, that is the largest integer less than or equal to <n>.\nSigning: Integer.",
    'ceil': "Syntax: ceil <n>\nReturns the ceiling of numerical value <n>, that is the smallest integer greater than or equal to <n>.\nSigning: Integer.",
}

packageexes = {
    'add': arith.AddAll,
    'sub': arith.SubAll,
    'mult': arith.MultAll,
    'div': arith.DivAll,
    'mod': arith.ModAll,
    'pow': arith.PowAll,
    'round': rounding.RoundTo,
    'floor': rounding.FlCeil,
    'ceil': rounding.FlCeil
}

packagetitles = {
    'Arithmetic Command Set: ': 'add, sub, mult, div, mod, round, floor, ceil'
}
