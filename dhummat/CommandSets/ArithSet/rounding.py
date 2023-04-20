"""
Copyright 2023 MITO-EK
This file is part of dhummat.
dhummat is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
dhummat is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with dhummat. If not, see <https://www.gnu.org/licenses/>.
"""

from . import inverif
from . import helpers


def RoundTo(args):
    # Input validation.
    if not inverif.RoundArgs(args):
        return "", ""
    # Round n to r decimal places.
    n = float(args[1])
    r = int(args[2])
    ans = helpers.FormatIntFloat(round(n, r))
    return str(ans), ans


def FlCeil(args):
    # Input validation.
    if not inverif.OneFloat(args):
        return "", ""
    n = float(args[1])
    # Integer or positive floor/negative ceil: remove the decimal places.
    ans = int(n)
    if (n == int(n)):
        pass
    # Negative floor, subtract 1 then remove decimals.
    elif args[0] == 'floor' and n < 0:
        ans = int(n - 1)
    # Postiive ceil, addm1 then remove decimals.
    elif args[0] == 'ceil' and n > 0:
        ans = int(n + 1)
    return str(ans), ans
