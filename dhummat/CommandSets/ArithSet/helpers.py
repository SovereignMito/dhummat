"""
Copyright 2023 SovereignMito
This file is part of dhummat.
dhummat is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
dhummat is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with dhummat. If not, see <https://www.gnu.org/licenses/>.
"""


# If m is a float with all 0s in decimal places, convert it to int.
def FormatIntFloat(m):
    if (m > 0 and m > float(int(m))) or (m < 0 and m < float(int(m))):
        return m
    return int(m)


# Calculate the number of decimal places a number has.
def CalcPlaces(n):
    # Number after decimal point/number from scientific notation.
    pd = 0
    pe = 0
    # Check for decimal places after the decimal point.
    if len(str(n).split(".")) > 1:
        pd = len(str(n).split(".")[1].split("e")[0])
    # Check for decimal places from a negative scientific notation.
    if len(str(n).split("e")) > 1 and int(str(n).split("e")[1]) < 0:
        pe = abs(int(str(n).split("e")[1]))
    return pd + pe
