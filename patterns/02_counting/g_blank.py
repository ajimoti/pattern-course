"""
PATTERN 02: COUNTING WITH A DICT - PRACTICE
Read a_lesson.md first. Write your code where it says `pass`.
Test from the pattern_course folder:   python3 practice.py 2
"""


# =============================================================================
# 1. WHAT'S POPULAR RIGHT NOW?
# =============================================================================
# THE PROBLEM
#   Your pizza shop's app has a "Popular right now" section that shows
#   customers which pizzas have been ordered the most in the last hour.
#
#   As customers place orders, the system records the type of pizza and the
#   minute each order was placed. Only orders placed within the last 60
#   minutes should count. If two or more pizzas have the same number of
#   orders, they should appear in alphabetical order.
#
# THE DATA
#   events = [(0, "margherita"), (30, "pepperoni"), (70, "pepperoni"),
#             (80, "hawaiian"), (85, "hawaiian"), (90, "margherita")]
#            (minute the order was placed, pizza name)
#   now = 90     the current minute
#   k = 2        how many pizzas to show
#
# YOUR TASK
#   trending(events, now, k) returns a list of the top k pizza names.
#   Count only orders placed AFTER minute (now - 60), up to now.
#   If there are fewer than k pizzas, return them all. No orders -> [].
#
# EXAMPLE
#   An hour ago was minute 30. Minutes 0 and 30 don't count.
#   Counts: hawaiian 2, pepperoni 1, margherita 1
#   Ranked: hawaiian, then margherita and pepperoni (tied, so A to Z)
#   trending(events, 90, 2)  ->  ["hawaiian", "margherita"]
#
# HINT
#   Sort the names A to Z first, then sort that by count with reverse=True.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Top K Frequent Elements - Bucket Sort - Leetcode 347 - Python (NeetCode)
#   https://www.youtube.com/watch?v=YPTqKIgVk-k
#   Same idea as LeetCode 347 Top K Frequent Elements. The video uses a different story and
#   different names, so watch for the method, not the details.
def trending(events, now, k):
    pass


# =============================================================================
# 2. THE FIRST CUSTOMER WHO ONLY ORDERED ONCE
# =============================================================================
# THE PROBLEM
#   The shop wants to win back customers who tried it once and never came
#   back. Marketing will send a free garlic bread voucher, but they only have
#   one voucher left this week, so it goes to the earliest customer who has
#   ordered exactly once.
#
#   You have the list of customer names in the order their orders were
#   placed. Some names appear many times, some appear only once.
#
# THE DATA
#   orders = ["ada", "ben", "ada", "cy", "ben", "dee"]
#
# YOUR TASK
#   first_one_time_customer(orders) returns the name of the first customer in
#   the list who appears exactly once. If nobody ordered exactly once, return
#   None.
#
# EXAMPLE
#   Counts: ada 2, ben 2, cy 1, dee 1
#   Go through the list from the start and check each name's count:
#     "ada" -> 2, no
#     "ben" -> 2, no
#     "ada" -> 2, no
#     "cy"  -> 1, yes. Stop.
#   first_one_time_customer(orders)  ->  "cy"
#
# HINT
#   Two passes: count everyone first, then go through the list again in order
#   and return the first name with a count of 1.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Leetcode 387 - First Unique Character in a String - Python Solution (Data Engineering Studies)
#   https://www.youtube.com/watch?v=jKI5nClXQDM
#   Same idea as LeetCode 387 First Unique Character in a String. The video uses a different story and
#   different names, so watch for the method, not the details.
def first_one_time_customer(orders):
    pass


# =============================================================================
# 3. ORDERS WITH THE SAME TOPPINGS
# =============================================================================
# THE PROBLEM
#   To save time in the kitchen, the chef wants orders with exactly the same
#   toppings made together. The toppings might be listed in a different order
#   on different tickets ("ham, pineapple" and "pineapple, ham" are the same
#   pizza), but they still count as the same.
#
#   Put the orders into groups, where every order in a group has the same set
#   of toppings.
#
# THE DATA
#   orders = [(1, ["ham", "pineapple"]),
#             (2, ["pepperoni"]),
#             (3, ["pineapple", "ham"]),
#             (4, ["pepperoni"]),
#             (5, ["mushroom", "olive"])]
#            (order id, list of toppings)
#
# YOUR TASK
#   group_same_toppings(orders) returns a list of groups. Each group is a list
#   of order ids, in the order they appear. The groups are in the order their
#   first order appears. No orders -> [].
#
# EXAMPLE
#   Order 1: ham, pineapple       -> new group          [[1]]
#   Order 2: pepperoni            -> new group          [[1], [2]]
#   Order 3: pineapple, ham       -> same as order 1    [[1, 3], [2]]
#   Order 4: pepperoni            -> same as order 2    [[1, 3], [2, 4]]
#   Order 5: mushroom, olive      -> new group          [[1, 3], [2, 4], [5]]
#   group_same_toppings(orders)  ->  [[1, 3], [2, 4], [5]]
#
# HINT
#   Use a dict where the key is the toppings in A to Z order, and the value is
#   a list of order ids. A list can't be a dict key, so turn it into a tuple:
#   tuple(sorted(toppings)).
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Group Anagrams - Categorize Strings by Count - Leetcode 49 (NeetCode)
#   https://www.youtube.com/watch?v=vzdNOK2oB2E
#   Same idea as LeetCode 49 Group Anagrams. The video uses a different story and
#   different names, so watch for the method, not the details.
def group_same_toppings(orders):
    pass
