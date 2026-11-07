"""
PATTERN 07: BINARY SEARCH
Read lesson.md first. Test your answers with:  python3 practice.py 7
"""


# =============================================================================
# 1. FIND AN ORDER IN THE SORTED ORDER LIST
# =============================================================================
# THE PROBLEM
#   Your shop keeps every order number from today in a list, sorted from
#   smallest to biggest. A customer rings up about their order, and you need to
#   find where it sits in the list so you can pull up its details.
#
#   On a busy day the list can have hundreds of thousands of orders, so reading
#   through it from the start is too slow while the customer waits.
#
# THE DATA
#   order_ids = [101, 104, 108, 115, 120, 133, 140]
#   target = 120
#
# YOUR TASK
#   find_order(order_ids, target) returns the position of target in the list,
#   or -1 if it isn't there. Don't go through the list item by item.
#
# EXAMPLE
#   find_order(order_ids, 120)  ->  4     (order_ids[4] is 120)
#   find_order(order_ids, 110)  ->  -1
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Binary Search - Leetcode 704 - Python (NeetCode)
#   https://www.youtube.com/watch?v=s4DPM8ct1pI
#   Same idea as LeetCode 704 Binary Search. The video uses a different story and
#   different names, so watch for the method, not the details.
def find_order(order_ids, target):
    pass


# =============================================================================
# 2. THE FIRST DELIVERY AT OR AFTER A GIVEN TIME
# =============================================================================
# THE PROBLEM
#   Drivers leave the shop at set minutes through the evening, and the list of
#   those minutes is sorted. When a pizza comes out of the oven, it goes with
#   the first driver leaving at that minute or later.
#
#   If the pizza is ready after the last driver has left, it can't go out
#   tonight.
#
# THE DATA
#   leave_times = [5, 12, 12, 20, 31]
#   ready = 13
#
# YOUR TASK
#   first_departure(leave_times, ready) returns the first leave time that is
#   at or after `ready`, or -1 if there isn't one.
#
# EXAMPLE
#   first_departure(leave_times, 13)  ->  20
#   first_departure(leave_times, 12)  ->  12    (leaving AT 12 counts)
#   first_departure(leave_times, 0)   ->  5
#   first_departure(leave_times, 40)  ->  -1
#
# HINT
#   You're not looking for an exact match. Keep track of the best answer so
#   far: when the middle time is >= ready, it's a possible answer, but there
#   might be an earlier one to the left.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   BS-2. Implement Lower Bound and Upper Bound | Search Insert Position (take U forward)
#   https://www.youtube.com/watch?v=6zhGS79oQ4k
#   Same idea as LeetCode 35 Search Insert Position. The video uses a different story and
#   different names, so watch for the method, not the details.
def first_departure(leave_times, ready):
    pass


# =============================================================================
# 3. HOW FAST DOES THE PIZZA ROBOT NEED TO BE?
# =============================================================================
# THE PROBLEM
#   Your shops are trying out a robot that tops pizzas. Each shop has a pile
#   of bases waiting. The robot works on one shop's pile per hour: in that
#   hour it tops up to `speed` pizzas from that pile. If the pile has fewer
#   left than that, it finishes them and sits idle until the next hour.
#
#   The robot has to clear every shop's pile within a set number of hours.
#   A faster robot costs more, so you want the slowest speed that still gets
#   everything done in time.
#
# THE DATA
#   piles = [3, 6, 7, 11]     (bases waiting at each shop)
#   hours = 8
#   hours is always at least len(piles), so a fast enough speed always exists.
#
# YOUR TASK
#   slowest_speed(piles, hours) returns the smallest whole-number speed that
#   finishes every pile within `hours`.
#
# EXAMPLE
#   speed 3: hours needed = 1 + 2 + 3 + 4 = 10     too slow
#   speed 4: hours needed = 1 + 2 + 2 + 3 = 8      fits
#   (a pile of 7 at speed 4 takes 2 hours: 4 in the first, 3 in the second)
#
#   slowest_speed(piles, 8)  ->  4
#
# HINT
#   Write a helper hours_needed(speed). Then binary search the SPEEDS from
#   1 to max(piles), looking for the smallest speed where hours_needed <= hours.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Koko Eating Bananas - Binary Search - Leetcode 875 - Python (NeetCode)
#   https://www.youtube.com/watch?v=U2SozAs9RzA
#   Same idea as LeetCode 875 Koko Eating Bananas. The video uses a different story and
#   different names, so watch for the method, not the details.
def slowest_speed(piles, hours):
    pass
