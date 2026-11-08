"""
PATTERN 03: TWO POINTERS - PRACTICE
Read a_lesson.md first. Write your code where it says `pass`.
Test from the pattern_course folder:   python3 practice.py 3
"""


# =============================================================================
# 1. TWO PIZZAS THAT USE UP A BUDGET EXACTLY
# =============================================================================
# THE PROBLEM
#   A customer has a gift card worth exactly £20 and wants to spend all of it
#   on two different pizzas. The menu prices are listed from cheapest to most
#   expensive.
#
#   Checking every pizza against every other pizza would work, but the full
#   menu is long and the app has to answer instantly. Because the prices are
#   already in order, you can do it in one pass.
#
# THE DATA
#   prices = [4, 6, 9, 11, 15]     sorted, cheapest first
#   budget = 20
#
# YOUR TASK
#   two_prices(prices, budget) returns (cheaper price, dearer price) for two
#   different pizzas that add up to exactly the budget. If there's no such
#   pair, return None. Two pizzas can have the same price.
#
# EXAMPLE
#   4 + 15 = 19, too small  -> move left  (4 -> 6)
#   6 + 15 = 21, too big    -> move right (15 -> 11)
#   6 + 11 = 17, too small  -> move left  (6 -> 9)
#   9 + 11 = 20, exact      -> (9, 11)
#   two_prices(prices, 20)  ->  (9, 11)
#
# HINT
#   left = 0, right = len(prices) - 1, and loop while left < right.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Two Sum II - Leetcode 167 - Python (NeetCode)
#   https://www.youtube.com/watch?v=cQ1Oz4ckceM
#   Same idea as LeetCode 167 Two Sum II. The video uses a different story and
#   different names, so watch for the method, not the details.
def two_prices(prices, budget):
    pass


# =============================================================================
# 2. AN ORDER CODE THAT READS THE SAME BACKWARDS
# =============================================================================
# THE PROBLEM
#   For a bit of fun, the shop is running a promotion: if your order code
#   reads the same forwards and backwards, your pizza is free. The codes are
#   made of letters and numbers, and upper or lower case doesn't matter, so
#   "Xy1yX" counts.
#
#   The till needs to check each code as it's printed. Compare the first
#   character with the last, the second with the second-to-last, and so on,
#   working inwards from both ends.
#
# THE DATA
#   code = "Xy1yX"
#
# YOUR TASK
#   is_mirror_code(code) returns True if the code reads the same forwards and
#   backwards (ignoring upper/lower case), otherwise False.
#   An empty code or a one-character code counts as True.
#
# EXAMPLE
#   "Xy1yX" in lowercase is "xy1yx"
#   position 0 "x" vs position 4 "x" -> same, move both inwards
#   position 1 "y" vs position 3 "y" -> same, move both inwards
#   position 2 meets position 2      -> stop, nothing left to compare
#   is_mirror_code("Xy1yX")  ->  True
#
#   "AB12BA": position 2 "1" vs position 3 "2" -> different -> False
#
# HINT
#   Lowercase the code first. Then left = 0, right = len(code) - 1, and move
#   both inwards while left < right.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Valid Palindrome - Leetcode 125 - Python (NeetCode)
#   https://www.youtube.com/watch?v=jJXJ16kPFWg
#   Same idea as LeetCode 125 Valid Palindrome. The video uses a different story and
#   different names, so watch for the method, not the details.
def is_mirror_code(code):
    pass


# =============================================================================
# 3. MERGING TWO SORTED LISTS OF ORDER TIMES
# =============================================================================
# THE PROBLEM
#   Orders come in from two places: the app and the phone line. Each system
#   gives you its own list of order times, already sorted from earliest to
#   latest. The kitchen screen needs one combined list, earliest first.
#
#   You could join the lists and sort them again, but both are already in
#   order, so you can build the combined list in a single pass by always
#   taking whichever list has the earlier time next.
#
# THE DATA
#   app   = [5, 12, 30]
#   phone = [8, 12, 40, 41]
#   (minutes after opening, earliest first)
#
# YOUR TASK
#   merge_orders(app, phone) returns one list with every time from both
#   lists, earliest first. Don't use sorted() or .sort().
#   If one list is empty, return a copy of the other.
#
# EXAMPLE
#   app 5  vs phone 8   -> take 5   [5]
#   app 12 vs phone 8   -> take 8   [5, 8]
#   app 12 vs phone 12  -> take 12 (from app; either is fine)   [5, 8, 12]
#   app 30 vs phone 12  -> take 12  [5, 8, 12, 12]
#   app 30 vs phone 40  -> take 30  [5, 8, 12, 12, 30]
#   app is finished     -> add the rest of phone: 40, 41
#   merge_orders(app, phone)  ->  [5, 8, 12, 12, 30, 40, 41]
#
# HINT
#   i = 0 for app, j = 0 for phone. Loop while both have items left. After
#   the loop, add whatever is left in either list.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Merge Sorted Array - Leetcode 88 - Python (NeetCode)
#   https://www.youtube.com/watch?v=P1Ic85RarKY
#   Same idea as LeetCode 88 Merge Sorted Array. The video uses a different story and
#   different names, so watch for the method, not the details.
def merge_orders(app, phone):
    pass
