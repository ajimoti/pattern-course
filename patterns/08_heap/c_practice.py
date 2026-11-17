"""
PATTERN 08: HEAP (ALWAYS GET THE SMALLEST NEXT) - PRACTICE
Read a_lesson.md first. Write your code where it says `pass`.
Test from the pattern_course folder:   python3 practice.py 8
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
#   dispatch(orders, drivers, trip) returns a dict that maps each order number
#   to the minute it leaves the shop with a driver.
#   Use heapq (Python's built-in heap module: a heap always gives you the
#   smallest item next).
#
# EXAMPLE
#   dispatch(orders, 2, 6)  ->  {101: 0, 102: 2, 103: 6, 104: 10}
#   Order 103 is ready at 3, but both drivers are out. The one who took order
#   101 is back first, at 6.
#
# VIDEO (try the problem yourself for 20-30 minutes first, then watch)
#   Single-Threaded CPU - Priority Queue - Leetcode 1834 - Python (NeetCode)
#   https://www.youtube.com/watch?v=RR1n-d4oYqE
#   This problem uses the same method as LeetCode 1834 Single-Threaded CPU. The video
#   uses a different story and different names, so watch for the method, not the
#   details.
def dispatch(orders, drivers, trip):
    pass


# =============================================================================
# 2. THE CLOSEST CUSTOMERS
# =============================================================================
# THE PROBLEM
#   One of your pizza shop's drivers has room for a few more pizzas before
#   leaving, and there are customers waiting all over town. To keep things
#   quick, you want to send the pizzas to the customers who live closest to
#   the shop.
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
#   closest_customers(customers, k) returns a list of the names of the k
#   customers closest to the shop, closest first.
#   If k is bigger than the number of customers, return all of them.
#
# EXAMPLE
#   Ben 1.2 and Dev 1.2 are tied, so Ben comes first. Then Chloe 3.0.
#   closest_customers(customers, 3)  ->  ["Ben", "Dev", "Chloe"]
#
# HINT
#   Push (distance, name) pairs onto a heap with heapq (a heap always gives you
#   the smallest item next), then pop (take out) the smallest k times.
#   The heap compares distance first, and name only when distances are equal.
#
# VIDEO (try the problem yourself for 20-30 minutes first, then watch)
#   K Closest Points to Origin - Heap / Priority Queue - Leetcode 973 (NeetCode)
#   https://www.youtube.com/watch?v=rI2EBUEMfTk
#   This problem uses the same method as LeetCode 973 K Closest Points to Origin. The
#   video uses a different story and different names, so watch for the method, not the
#   details.
def closest_customers(customers, k):
    pass


# =============================================================================
# 3. MERGE SORTED ORDER LISTS FROM SEVERAL SHOPS
# =============================================================================
# THE PROBLEM
#   You run a chain of pizza shops with a head office. Each shop sends head
#   office a list of the minutes its orders came in, and each shop's list is
#   already sorted. Head office wants one combined list of every order time,
#   in order, to see how busy the whole company was.
#
#   You could join all the lists and sort the lot, but the lists can be long,
#   and they're already sorted, so there's a quicker way.
#
# THE DATA
#   shop_lists = [[1, 5, 9],
#                 [2, 3, 10],
#                 [4]]
#   (one list per shop, each sorted from earliest to latest)
#
# YOUR TASK
#   merge_order_lists(shop_lists) returns one sorted list of every minute from
#   all the shop lists. Some shops may send an empty list. If every list is
#   empty, it returns [].
#
# EXAMPLE
#   merge_order_lists(shop_lists)  ->  [1, 2, 3, 4, 5, 9, 10]
#
# HINT
#   The smallest minute not yet in your result is always the first unused item
#   of one of the lists.
#   Put each list's first item on a heap (with heapq) as
#   (minute, which list, position in that list).
#   Pop the smallest, add it to the result, then push the next item from that
#   same list (if it has one).
#
# VIDEO (try the problem yourself for 20-30 minutes first, then watch)
#   Merge K Sorted Lists - Leetcode 23 - Python (NeetCode)
#   https://www.youtube.com/watch?v=q5a5OiGbT6Q
#   This problem uses the same method as LeetCode 23 Merge k Sorted Lists. The video
#   uses a different story and different names, so watch for the method, not the
#   details.
def merge_order_lists(shop_lists):
    pass
