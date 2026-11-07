"""
PATTERN 12: FASTEST ROUTE (DIJKSTRA) - PRACTICE
Read lesson.md first. Then write your code where it says `pass`.
Test your answers:   python practice.py 12
"""
import heapq


# =============================================================================
# 1. THE FASTEST WAY TO A CUSTOMER   (the lesson's worked example)
# =============================================================================
# THE PROBLEM
#   A customer has just placed an order, and your driver needs to get their
#   pizza there as quickly as possible.
#
#   There are several ways from the shop to the customer, and some roads take
#   longer to drive than others. The route with the fewest roads isn't always
#   the fastest one.
#
#   You know how the roads connect and how many minutes each one takes. Find
#   the fastest route from the shop to the customer, and how long it takes.
#
# THE DATA
#   roads = [("Shop", "A", 4),
#            ("Shop", "B", 1),
#            ("B",    "A", 2),
#            ("A",    "C", 5),
#            ("B",    "C", 8)]
#   Each road is (place, other place, minutes). Roads go both ways.
#
# YOUR TASK
#   fastest_route(roads, start, end) returns (minutes, list of places in order).
#   If end can't be reached, return (-1, []).
#   If start and end are the same place, return (0, [start]).
#
# EXAMPLE
#   Shop -> A -> C        = 4 + 5     = 9 minutes
#   Shop -> B -> C        = 1 + 8     = 9 minutes
#   Shop -> B -> A -> C   = 1 + 2 + 5 = 8 minutes   <- fastest
#
#   fastest_route(roads, "Shop", "C")  ->  (8, ["Shop", "B", "A", "C"])
#
# HINT
#   Do it in two parts, like the lesson: first return only the time, then add
#   a came_from dict to build the route.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Implement Dijkstra's Algorithm (NeetCodeIO)
#   https://www.youtube.com/watch?v=XEb7_z5dG3c
#   Same idea as LeetCode Dijkstra in Python. The video uses a different story and
#   different names, so watch for the method, not the details.
def fastest_route(roads, start, end):
    pass


# =============================================================================
# 2. FASTEST TIME FROM THE SHOP TO EVERY PLACE
# =============================================================================
# THE PROBLEM
#   You're putting together a delivery-times table for the website, so
#   customers can see roughly how long they'll wait. For that you need the
#   fastest driving time from the shop to every place on the map, not just
#   one customer.
#
#   Some places aren't connected to the shop by any road. Those should be left
#   out of the table completely.
#
# THE DATA
#   roads = [("Shop", "A", 4), ("Shop", "B", 1), ("B", "A", 2),
#            ("A", "C", 5), ("B", "C", 8)]
#   Each road is (place, other place, minutes). Roads go both ways.
#
# YOUR TASK
#   fastest_times(roads, start) returns a dict: {place: fastest minutes}.
#   Include the start itself, with 0. Leave out places that can't be reached.
#
# EXAMPLE
#   Shop: 0
#   B:    1   (Shop -> B)
#   A:    3   (Shop -> B -> A, quicker than the 4-minute direct road)
#   C:    8   (Shop -> B -> A -> C)
#
#   fastest_times(roads, "Shop")  ->  {"Shop": 0, "B": 1, "A": 3, "C": 8}
#
# HINT
#   It's problem 1 without stopping early. Keep going until the heap is empty.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Dijkstra Algorithm - Single Source Shortest Path - Greedy Method (Abdul Bari)
#   https://www.youtube.com/watch?v=XB4MIexjvY0
#   Same idea as LeetCode Shortest path to every place. The video uses a different story and
#   different names, so watch for the method, not the details.
def fastest_times(roads, start):
    pass


# =============================================================================
# 3. WHEN HAS EVERY SHOP GOT THE PROMO MESSAGE?
# =============================================================================
# THE PROBLEM
#   Head office is launching a two-for-one deal and needs every shop to know
#   about it before it goes live. Head office can't message every shop
#   directly. It sends the news to a few shops, and those shops pass it on.
#
#   Each link only works one way, and each one takes a certain number of
#   minutes to get through. Head office wants to know how long it will be
#   until every shop has the message. If any shop will never get it, they
#   need to know that too.
#
# THE DATA
#   links = [("HQ",    "Leeds", 2),
#            ("HQ",    "York",  5),
#            ("Leeds", "York",  1),
#            ("York",  "Hull",  3)]
#   Each link is (sender, receiver, minutes). ONE WAY: Leeds can send to York,
#   but York can't send back to Leeds.
#   shops = ["HQ", "Leeds", "York", "Hull"]
#   start = "HQ"
#
# YOUR TASK
#   everyone_has_message(links, shops, start) returns the number of minutes
#   until every shop in `shops` has the message.
#   Return -1 if any shop never gets it.
#
# EXAMPLE
#   HQ    gets it at 0
#   Leeds gets it at 2   (HQ -> Leeds)
#   York  gets it at 3   (HQ -> Leeds -> York, quicker than HQ -> York at 5)
#   Hull  gets it at 6   (HQ -> Leeds -> York -> Hull)
#   The last shop to get it is Hull, at minute 6.
#
#   everyone_has_message(links, shops, "HQ")  ->  6
#
# HINT
#   Find the fastest time to every shop (problem 2), then take the biggest.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Network Delay Time - Dijkstra's algorithm - Leetcode 743 (NeetCode)
#   https://www.youtube.com/watch?v=EaphyqKU4PQ
#   Same idea as LeetCode 743 Network Delay Time. The video uses a different story and
#   different names, so watch for the method, not the details.
def everyone_has_message(links, shops, start):
    pass
