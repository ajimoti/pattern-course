"""
PATTERN 05: SORT, THEN WALK THROUGH ONCE
Read a_lesson.md first. Test your answers with:  python3 practice.py 5
"""


# =============================================================================
# 1. HOW MANY OVENS DOES THE SHOP NEED?
# =============================================================================
# THE PROBLEM
#   Your pizza shop is getting busier, and you need to figure out how many
#   ovens are required to handle all the orders.
#
#   Each pizza has a scheduled time to go into the oven and a time when it
#   finishes baking. An oven can only bake one pizza at a time. However, as
#   soon as a pizza comes out, another can go straight in.
#
#   Your task is to calculate the minimum number of ovens the shop needs to
#   bake every pizza at its scheduled time without making any order wait.
#
# THE DATA
#   bakes = [(0, 10), (5, 15), (10, 20), (12, 14)]
#   Each pizza is (minute it goes in, minute it comes out).
#
# YOUR TASK
#   min_ovens(bakes) returns the number of ovens needed.
#   With no pizzas, return 0.
#
# EXAMPLE
#   At minute 12, pizzas (5, 15), (10, 20) and (12, 14) are all baking.
#   That's the busiest moment, so the answer is 3.
#
# HINT
#   +1 when a pizza goes in, -1 when it comes out. Sort, then keep a count.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Meeting Rooms II - Leetcode 253 - Python (NeetCode)
#   https://www.youtube.com/watch?v=FdzJmTCVyJU
#   Same idea as LeetCode 253 Meeting Rooms II. The video uses a different story and
#   different names, so watch for the method, not the details.
def min_ovens(bakes):
    pass


# =============================================================================
# 2. MERGE OVERLAPPING DRIVER SHIFTS
# =============================================================================
# THE PROBLEM
#   Several drivers have signed up for shifts tonight, and some of the shifts
#   overlap. Your manager doesn't care who is working, only when the shop has
#   at least one driver on the road.
#
#   If two shifts overlap, or one ends at exactly the minute the next one
#   starts, treat them as one continuous block of cover. Shifts that don't
#   touch stay separate.
#
#   Your task is to turn the list of shifts into the blocks of time when the
#   shop has cover, in time order.
#
# THE DATA
#   shifts = [(16, 18), (9, 12), (18, 20), (11, 14)]
#   Each shift is (start hour, end hour). They are NOT given in order.
#
# YOUR TASK
#   merge_shifts(shifts) returns a list of (start, end) blocks, earliest first.
#   With no shifts, return [].
#
# EXAMPLE
#   Sorted by start: (9, 12), (11, 14), (16, 18), (18, 20)
#   (9, 12) and (11, 14) overlap        -> one block (9, 14)
#   (16, 18) does not touch (9, 14)     -> new block (16, 18)
#   (18, 20) starts as (16, 18) ends    -> extend to (16, 20)
#
#   merge_shifts(shifts)  ->  [(9, 14), (16, 20)]
#
# HINT
#   Sort by start. Compare each shift with the LAST block you've built.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Merge Intervals - Sorting - Leetcode 56 (NeetCode)
#   https://www.youtube.com/watch?v=44H3cEC2fFM
#   Same idea as LeetCode 56 Merge Intervals. The video uses a different story and
#   different names, so watch for the method, not the details.
def merge_shifts(shifts):
    pass


# =============================================================================
# 3. CAN ONE DRIVER DO EVERY DELIVERY?
# =============================================================================
# THE PROBLEM
#   It's a quiet Tuesday and only one driver has turned up. Each delivery has
#   a time it has to leave the shop and a time the driver gets back.
#
#   A driver can't be on two deliveries at once, but if they get back at
#   minute 10, they can leave again at minute 10.
#
#   Your task is to work out whether one driver can cover every delivery.
#
# THE DATA
#   deliveries = [(25, 30), (0, 10), (10, 20)]
#   Each delivery is (minute it leaves, minute the driver is back).
#   They are NOT given in order.
#
# YOUR TASK
#   can_one_driver(deliveries) returns True or False.
#   With no deliveries, return True.
#
# EXAMPLE
#   Sorted: (0, 10), (10, 20), (25, 30)
#   (10, 20) leaves at 10, driver back at 10   -> fine
#   (25, 30) leaves at 25, driver back at 20   -> fine
#   can_one_driver(deliveries)  ->  True
#
#   can_one_driver([(0, 10), (5, 15)])  ->  False
#   (the second leaves at 5, but the driver isn't back until 10)
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Meeting Rooms - Leetcode 252 - Python (NeetCode)
#   https://www.youtube.com/watch?v=PaJxqZVPhbg
#   Same idea as LeetCode 252 Meeting Rooms. The video uses a different story and
#   different names, so watch for the method, not the details.
def can_one_driver(deliveries):
    pass
