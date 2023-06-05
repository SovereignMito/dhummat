"""
Copyright 2023 SovereignMito
This file is part of dhummat.
dhummat is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
dhummat is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with dhummat. If not, see <https://www.gnu.org/licenses/>.
"""

from . import inverif


# Format command line text responses together from a list of perms or combs.
def BuildRes(li, r):
    res = r
    i = 0
    for line in li:
        res += "{}: {}".format(str(i+1), str(line)[1:-1])
        if i < len(li) - 1:
            res += '\n'
        i += 1
    return res


def BuildKes(li, r):
    res = r
    i = 0
    for line in li:
        res += "{}".format(str(line))
        if i < len(li) - 1:
            res += '\n'
        i += 1
    return res


# Helper function for combination recursion.
def KCHelper(k, nums):
    # Find all (k-1)-combinations of elements except 1st element,
    # then add them to the first element to form the k-comb.
    return [[nums[0]] + m for m in KCall(k - 1, nums[1:])]


# k-combinations of list l.
def KCall(k, nums):
    # Base case: 1-combinations are just one of each element.
    if (k == 1):
        return [[n] for n in nums]
    # Track iteration position and store combinations.
    p = 0
    combos = []
    # Combinations = one element + (k-1 combinations of elements to the right).
    for n in nums:
        # Stop if not enough elements to form a k-combination.
        if len(nums) - p < k:
            break
        # Initiate recursion process using only [element:] part of the list.
        combos.extend([m for m in KCHelper(k, nums[p:])])
        p += 1
    return combos


# All combinations of length 1 to length n.
def Call(n):
    cl = [k for k in range(1, n + 1)]
    combos = []
    for k in cl:
        combos.extend([KCall(k, cl)])
    return combos


# Helper function for permutation recursion.
def KPHelper(k, nums, p):
    # Find all (k-1)-permutations of elements except the current index,
    # then add them to the indexed element to form the k-perm.
    return [[nums[p]] + s for s in KPall(k - 1, nums[:p] + nums[p+1:])]


# k-permutations of a list l.
def KPall(k, nums):
    # Base case: 1-combinations are just one of each element.
    if k == 1:
        return [[n] for n in nums]
    # Track iteration position and store perms.
    perms = []
    for p in range(0, len(nums)):
        # Initiate recursion process using the entire list.
        # Mark the index to exclude during the recursion.
        perms.extend([m for m in KPHelper(k, nums, p)])
    return perms


# All permutations of length 1 to length n.
def Pall(n):
    pcl = [k for k in range(1, n + 1)]
    perms = []
    for k in pcl:
        perms.extend([KPall(k, pcl)])
    return perms


# Execute Combination listing command.
def RunCall(args):
    res = ""
    # Command used by itself.
    if len(args) == 1:
        print("Usage: call <n>\nUsage: call <k> <n>")
    # All combinations.
    elif len(args) == 2 and inverif.SingleInt(args, 1):
        res = "Combinations for n = {}:\n".format(args[1])
        res = BuildRes(Call(int(args[1])), res)
    # K-combinations.
    elif len(args) >= 3 and inverif.DoubleArg(args, False):
        res = "{}-Combinations for n = {}:\n".format(args[1], args[2])
        res = BuildKes(KCall(int(args[1]),
                       [n for n in range(1, int(args[2]) + 1)]), res)
    return res, ""


# Execute permutation listing command.
def RunPall(args):
    res = ""
    # Command used by itself.
    if len(args) == 1:
        print("Usage: pall <n>\nUsage: pall <k> <n>")
    # All permutations.
    elif len(args) == 2 and inverif.SingleInt(args, 1):
        res = "Permutations for n = {}:\n".format(args[1])
        res = BuildRes(Pall(int(args[1])), res)
    # K-permutations.
    elif len(args) >= 3 and inverif.DoubleArg(args, False):
        res = "{}-Permutations for n = {}:\n".format(args[1], args[2])
        res = BuildKes(KPall(int(args[1]),
                       [n for n in range(1, int(args[2]) + 1)]), res)
    return res, ""
