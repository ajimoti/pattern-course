"""
PATTERN 08: HEAP (ALWAYS GET THE SMALLEST NEXT)
Read a_lesson.md first. Test your answers with:  python3 practice.py 8
"""


# =============================================================================
# 1. GIVING ORDERS TO DRIVERS
# =============================================================================
# THE PROBLEM
#   Your pizza shop has two delivery drivers, and new orders are constantly
#   coming out of the oven. Each delivery takes exactly six minutes, including
#   the time needed for the driver to return to the shop.
#
#   Whenever a pizza is ready, you want to assign it to whichever driver
#   becomes available first. If a driver is already at the shop, they can
#   leave immediately. However, if both drivers are out making deliveries, the
#   pizza must wait until one returns.
#
# THE DATA
#   orders = [(101, 0), (102, 2), (103, 3), (104, 10)]
#            (order number, minute the pizza is ready), in time order
#   drivers = 2      (both at the shop at minute 0)
#   trip = 6
#
# YOUR TASK
#   dispatch(orders, drivers, trip) returns {order number: minute it leaves}.
#   Use heapq.
#
# EXAMPLE
#   dispatch(orders, 2, 6)  ->  {101: 0, 102: 2, 103: 6, 104: 10}
#   Order 103 is ready at 3, but the first driver isn't back until 6.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Single-Threaded CPU - Priority Queue - Leetcode 1834 - Python (NeetCode)
#   https://www.youtube.com/watch?v=RR1n-d4oYqE
#   Same idea as LeetCode 1834 Single-Threaded CPU (similar idea). The video uses a different story and
#   different names, so watch for the method, not the details.
def dispatch(orders, drivers, trip):
    pass


# =============================================================================
# 2. THE CLOSEST CUSTOMERS
# =============================================================================
# THE PROBLEM
#   A driver has room for a few more pizzas before leaving, and there are
#   customers waiting all over town. To keep things quick, you want to send the
#   pizzas to the customers who live closest to the shop.
#
#   If two customers are exactly the same distance away, the one whose name
#   comes first alphabetically gets their pizza first.
#
# THE DATA
#   customers = [("Amara", 4.5), ("Ben", 1.2), ("Chloe", 3.0),
#                ("Dev", 1.2), ("Esi", 7.1)]
#               (name, kilometres from the shop)
#   k = 3          (how many customers to pick)
#
# YOUR TASK
#   closest_customers(customers, k) returns the k closest names, closest first.
#   If k is bigger than the number of customers, return all of them.
#
# EXAMPLE
#   Ben 1.2 and Dev 1.2 are tied, so Ben comes first. Then Chloe 3.0.
#   closest_customers(customers, 3)  ->  ["Ben", "Dev", "Chloe"]
#
# HINT
#   Push (distance, name) pairs onto a heap, then pop k times.
#   The heap compares distance first, and name only when distances are equal.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   K Closest Points to Origin - Heap / Priority Queue - Leetcode 973 (NeetCode)
#   https://www.youtube.com/watch?v=rI2EBUEMfTk
#   Same idea as LeetCode 973 K Closest Points to Origin. The video uses a different story and
#   different names, so watch for the method, not the details.
def closest_customers(customers, k):
    pass


# =============================================================================
# 3. MERGE SORTED ORDER LISTS FROM SEVERAL SHOPS
# =============================================================================
# THE PROBLEM
#   Each of your shops sends head office a list of the minutes its orders came
#   in, and each shop's list is already sorted. Head office wants one combined
#   list of every order time, in order, to see how busy the whole company was.
#
#   You could join all the lists and sort the lot, but the lists can be long,
#   and they're already sorted, so there's a quicker way.
#
# THE DATA
#   shop_lists = [[1, 5, 9],
#                 [2, 3, 10],
#                 [4]]
#
# YOUR TASK
#   merge_order_lists(shop_lists) returns one sorted list of every minute.
#   Some shops may send an empty list.
#
# EXAMPLE
#   merge_order_lists(shop_lists)  ->  [1, 2, 3, 4, 5, 9, 10]
#
# HINT
#   The smallest of everything is always one of the FIRST items of a list.
#   Put each list's first item on a heap as (minute, which list, position).
#   Pop the smallest, add it to the result, then push the next item from that
#   same list (if it has one).
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Merge K Sorted Lists - Leetcode 23 - Python (NeetCode)
#   https://www.youtube.com/watch?v=q5a5OiGbT6Q
#   Same idea as LeetCode 23 Merge k Sorted Lists. The video uses a different story and
#   different names, so watch for the method, not the details.
def merge_order_lists(shop_lists):
    pass
