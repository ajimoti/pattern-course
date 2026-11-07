"""
PATTERN 14: DYNAMIC PROGRAMMING (BUILD ANSWERS FROM SMALLER ANSWERS) - PRACTICE
Read lesson.md first. Then write your code where it says `pass`.
Test your answers:   python practice.py 14
"""


# =============================================================================
# 1. THE FEWEST BOXES FOR AN ORDER OF SLICES   (the lesson's worked example)
# =============================================================================
# THE PROBLEM
#   Your shop sells pizza by the slice, and slices go out in boxes that hold
#   1, 4 or 6 slices. Every box has to go out full, so no half-empty boxes.
#
#   Boxes cost money, so for each order you want to use as few boxes as
#   possible. Sometimes the obvious choice isn't the best one. For 8 slices,
#   grabbing the biggest box first gives 6 + 1 + 1 (three boxes), but 4 + 4 is
#   only two.
#
#   Some orders can't be made up exactly with the boxes you have. When that
#   happens, you need to know.
#
# THE DATA
#   slices = 8
#   box_sizes = [1, 4, 6]
#
# YOUR TASK
#   fewest_boxes(slices, box_sizes) returns the smallest number of full boxes
#   that hold exactly `slices` slices.
#   Return -1 if it can't be done. 0 slices needs 0 boxes.
#
# EXAMPLE
#   6 + 1 + 1 = 8   -> 3 boxes
#   4 + 4     = 8   -> 2 boxes   <- fewest
#
#   fewest_boxes(8, [1, 4, 6])  ->  2
#   fewest_boxes(7, [4, 6])     ->  -1   (no mix of 4s and 6s makes 7)
#
# HINT
#   Work out the answer for 0 slices, then 1, then 2, and so on up to 8,
#   storing each one in a list. Each answer uses the ones before it.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Coin Change - Dynamic Programming Bottom Up - Leetcode 322 (NeetCode)
#   https://www.youtube.com/watch?v=H9bfqozjoqs
#   Same idea as LeetCode 322 Coin Change. The video uses a different story and
#   different names, so watch for the method, not the details.
def fewest_boxes(slices, box_sizes):
    pass


# =============================================================================
# 2. THE MOST TIPS ON ONE STREET
# =============================================================================
# THE PROBLEM
#   One of your drivers has a run down a long street where several houses have
#   ordered, and you know roughly what each one tips.
#
#   The street has strict parking. Once the driver stops outside a house, they
#   have to drive past the next house before they can stop again. So they
#   can never deliver to two houses that are next door to each other on the
#   same run.
#
#   Choose which houses the driver should stop at to collect the most tips.
#
# THE DATA
#   tips = [2, 7, 9, 3, 1]
#   tips[0] is the first house on the street, tips[1] the next one, and so on.
#
# YOUR TASK
#   most_tips(tips) returns the biggest total the driver can collect without
#   stopping at two next-door houses. An empty street gives 0.
#
# EXAMPLE
#   Stop at houses 0, 2 and 4:  2 + 9 + 1 = 12   <- most
#   Stop at houses 1 and 3:     7 + 3     = 10
#   Stop at houses 1 and 4:     7 + 1     = 8
#
#   most_tips([2, 7, 9, 3, 1])  ->  12
#
# HINT
#   Go house by house. At each one: is it better to skip this house, or to
#   stop here and add this tip to the best total from two houses back?
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   House Robber - Leetcode 198 - Dynamic Programming (Python) (Greg Hogg)
#   https://www.youtube.com/watch?v=kIII1uT6F8Y
#   Same idea as LeetCode 198 House Robber. The video uses a different story and
#   different names, so watch for the method, not the details.
def most_tips(tips):
    pass


# =============================================================================
# 3. HOW MANY WAYS TO BOX AN ORDER?
# =============================================================================
# THE PROBLEM
#   The shop manager wants to print a little chart by the counter showing the
#   different ways an order can be boxed, so staff stop arguing about it. The
#   boxes hold 1, 2 or 5 slices.
#
#   Two mixes count as the same if they use the same boxes in a different
#   order. A 2-box then a 1-box is the same mix as a 1-box then a 2-box.
#
#   For a given number of slices, how many different mixes of full boxes are
#   there?
#
# THE DATA
#   slices = 5
#   box_sizes = [1, 2, 5]
#
# YOUR TASK
#   ways_to_pack(slices, box_sizes) returns how many different mixes of boxes
#   hold exactly `slices` slices. For 0 slices there's exactly 1 way (no boxes).
#
# EXAMPLE
#   5
#   2 + 2 + 1
#   2 + 1 + 1 + 1
#   1 + 1 + 1 + 1 + 1
#   That's 4 mixes.
#
#   ways_to_pack(5, [1, 2, 5])  ->  4
#
# HINT
#   Keep a list ways[0..slices] starting at [1, 0, 0, ...]. Bring in one box
#   size at a time (outer loop), so each mix is only counted once.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Coin Change 2 - Dynamic Programming Unbounded Knapsack - Leetcode 518 - Python (NeetCode)
#   https://www.youtube.com/watch?v=Mjy4hd2xgrs
#   Same idea as LeetCode 518 Coin Change II. The video uses a different story and
#   different names, so watch for the method, not the details.
def ways_to_pack(slices, box_sizes):
    pass
