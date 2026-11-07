"""
PATTERN 14: DYNAMIC PROGRAMMING (BUILD ANSWERS FROM SMALLER ANSWERS) - SOLUTIONS
"""


# =============================================================================
# 1. THE FEWEST BOXES FOR AN ORDER OF SLICES
# =============================================================================
# Idea: work out the fewest boxes for 0 slices, then 1, then 2, ... up to the
# order. For each amount, try every box size: "use one box of this size, plus
# the fewest boxes for whatever is left" (already worked out). Keep the best.
# float("inf") means "can't be done (yet)".
# Speed: (number of slices) x (number of box sizes).
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Coin Change - Dynamic Programming Bottom Up - Leetcode 322 (NeetCode)
#   https://www.youtube.com/watch?v=H9bfqozjoqs
#   Same idea as LeetCode 322 Coin Change. The video uses a different story and
#   different names, so watch for the method, not the details.
def fewest_boxes(slices, box_sizes):
    best = [0] + [float("inf")] * slices       # best[amount] = fewest boxes for that amount

    for amount in range(1, slices + 1):
        for size in box_sizes:
            if size <= amount:
                with_this_box = best[amount - size] + 1
                if with_this_box < best[amount]:
                    best[amount] = with_this_box

    if best[slices] == float("inf"):
        return -1
    return best[slices]


# =============================================================================
# 2. THE MOST TIPS ON ONE STREET
# =============================================================================
# Idea: go along the street one house at a time. At each house there are two
# choices:
#   skip it  -> keep the best total so far
#   stop     -> this house's tip + the best total from two houses back
# Keep the bigger one. You only ever need the last two totals.
# Speed: one pass along the street.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   House Robber - Leetcode 198 - Dynamic Programming (Python) (Greg Hogg)
#   https://www.youtube.com/watch?v=kIII1uT6F8Y
#   Same idea as LeetCode 198 House Robber. The video uses a different story and
#   different names, so watch for the method, not the details.
def most_tips(tips):
    two_back = 0      # best total up to two houses ago
    one_back = 0      # best total up to the previous house

    for tip in tips:
        best_here = max(one_back, two_back + tip)
        two_back = one_back
        one_back = best_here

    return one_back


# =============================================================================
# 3. HOW MANY WAYS TO BOX AN ORDER?
# =============================================================================
# Idea: ways[amount] = how many different mixes of boxes make exactly that
# amount. Start with ways[0] = 1 (the empty mix). Bring in one box size at a
# time: for every amount, the mixes that use this size = ways[amount - size].
# Doing one size at a time (outer loop) means each mix is counted once,
# whatever order the boxes are listed in.
# Speed: (number of slices) x (number of box sizes).
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Coin Change 2 - Dynamic Programming Unbounded Knapsack - Leetcode 518 - Python (NeetCode)
#   https://www.youtube.com/watch?v=Mjy4hd2xgrs
#   Same idea as LeetCode 518 Coin Change II. The video uses a different story and
#   different names, so watch for the method, not the details.
def ways_to_pack(slices, box_sizes):
    ways = [1] + [0] * slices

    for size in box_sizes:
        for amount in range(size, slices + 1):
            ways[amount] += ways[amount - size]

    return ways[slices]
