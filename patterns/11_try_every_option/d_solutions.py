"""
PATTERN 11: Try every option - solutions
"""
import math
from itertools import combinations, permutations


# 1. THE SHORTEST DELIVERY ROUTE
# Try every order of the customers, put the shop at both ends, measure, keep
# the shortest. Speed: grows with n! (n factorial), where n is the number of
# customers - fine for about 8 customers.
#
# VIDEO (try the problem yourself for 20-30 minutes first, then watch)
#   Backtracking: Permutations - Leetcode 46 - Python (NeetCode)
#   https://www.youtube.com/watch?v=s7AvT7cGdSo
#   This problem uses the same method as LeetCode 46 Permutations. The video uses a
#   different story and different names, so watch for the method, not the details.
def read_points(text):
    points = []
    for pair in text.split(" "):
        x, y = pair.split(",")
        points.append((int(x), int(y)))
    return points


def trip_length(trip):
    total = 0
    for i in range(len(trip) - 1):
        total += math.dist(trip[i], trip[i + 1])
    return total


def best_route(points):
    shop = points[0]
    customers = points[1:]

    best = None
    shortest = float("inf")
    for order in permutations(customers):
        trip = [shop] + list(order) + [shop]
        length = trip_length(trip)
        if length < shortest:
            shortest = length
            best = trip
    return best, shortest


# 2. EVERY WAY TO CHOOSE TOPPINGS
# Written with recursion ("take it or leave it"). The one-line version is:
#     return list(combinations(toppings, k))
# Speed: grows with the number of choices, which is large for big lists.
#
# VIDEO (try the problem yourself for 20-30 minutes first, then watch)
#   Combinations - Leetcode 77 - Python (NeetCode)
#   https://www.youtube.com/watch?v=q0s6m7AiM7o
#   This problem uses the same method as LeetCode 77 Combinations. The video uses a
#   different story and different names, so watch for the method, not the details.
def topping_choices(toppings, k):
    if k == 0:
        return [()]
    if len(toppings) < k:
        return []
    first = toppings[0]
    rest = toppings[1:]
    with_first = [(first,) + choice for choice in topping_choices(rest, k - 1)]
    without_first = topping_choices(rest, k)
    return with_first + without_first


# 3. FILL THE VAN EXACTLY
# Try every group, smallest groups first. The first exact match uses the
# fewest orders. Speed: up to 2 to the power n groups, where n is the number of
# orders - fine for about 20 orders.
#
# VIDEO (try the problem yourself for 20-30 minutes first, then watch)
#   Subsets - Backtracking - Leetcode 78 (NeetCode)
#   https://www.youtube.com/watch?v=REOH22Xwdkk
#   This problem uses the same method as LeetCode 78 Subsets. The video uses a different
#   story and different names, so watch for the method, not the details.
def fill_the_van(orders, capacity):
    for size in range(len(orders) + 1):
        for group in combinations(orders, size):
            if sum(pizzas for _, pizzas in group) == capacity:
                return [name for name, _ in group]
    return None
