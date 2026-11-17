"""
PATTERN 11: Try every option - PRACTICE
Read a_lesson.md first. Write your code where it says `pass`.
Test from the pattern_course folder:   python3 practice.py 11
"""
import math
from itertools import combinations, permutations


# =============================================================================
# 1. THE SHORTEST DELIVERY ROUTE
# =============================================================================
# THE PROBLEM
#   A driver starts at your pizza shop, delivers to a few customers, then
#   drives back to the shop. They can visit the customers in any order, and
#   you want the order that means the least driving.
#
#   The shop and customer addresses come in as text, like "0,0 1,1 2,0 2,2".
#   Each x,y pair is one address on a grid. The first one is the shop and the
#   rest are customers. The driver goes in a straight line from one place to
#   the next.
#
# THE DATA
#   text = "0,0 1,1 2,0 2,2"
#   Shop = (0, 0), A = (1, 1), B = (2, 0), C = (2, 2)
#
# YOUR TASK
#   Write three functions:
#
#   read_points(text) takes the text and returns a list of (x, y) pairs of
#   ints, one per address, in the same order.
#
#   trip_length(trip) takes a list of (x, y) places in order and returns the
#   total straight-line distance from each place to the next.
#
#   best_route(points) takes the list that read_points returns. It returns
#   (route, distance) for the shortest route that starts at points[0] (the
#   shop), visits every other point once, and ends back at points[0]. route is
#   the list of places in visiting order. If there are no customers, the route
#   is just [shop, shop] with distance 0.
#
# EXAMPLE
#   read_points("0,0 1,1 2,0 2,2")  ->  [(0, 0), (1, 1), (2, 0), (2, 2)]
#
#   trip_length([(0, 0), (1, 1), (2, 2), (2, 0), (0, 0)])
#       1.41 + 1.41 + 2 + 2  ->  6.83 (to 2 decimal places)
#
#   best_route([(0, 0), (1, 1), (2, 0), (2, 2)])
#       ->  ([(0, 0), (1, 1), (2, 2), (2, 0), (0, 0)], 6.83)
#       The same loop the other way round is also accepted.
#
# HINT
#   math.dist(a, b) gives the distance between two points.
#   permutations(points[1:]) gives every order of the customers.
#
# VIDEO (try the problem yourself for 20-30 minutes first, then watch)
#   Backtracking: Permutations - Leetcode 46 - Python (NeetCode)
#   https://www.youtube.com/watch?v=s7AvT7cGdSo
#   This problem uses the same method as LeetCode 46 Permutations. The video uses a
#   different story and different names, so watch for the method, not the details.
def read_points(text):
    pass


def trip_length(trip):
    pass


def best_route(points):
    pass


# =============================================================================
# 2. EVERY WAY TO CHOOSE TOPPINGS
# =============================================================================
# THE PROBLEM
#   Your pizza shop has a "build your own" pizza. Customers pick a set number
#   of toppings from a list. Your menu designer wants to see every possible
#   choice, so
#   they can check none of them sound awful together.
#
#   Order doesn't matter: ham and olive is the same pizza as olive and ham.
#
# THE DATA
#   toppings = ["ham", "mushroom", "olive", "pepper"]
#   k = 2      (how many toppings the customer picks)
#
# YOUR TASK
#   topping_choices(toppings, k) takes the list of toppings and k. It returns
#   a list of every possible choice, each as a tuple of k toppings. The
#   choices can come in any order. Choosing 0 toppings has
#   exactly one way: [()]. Choosing more toppings than there are has no ways: [].
#
# EXAMPLE
#   topping_choices(["ham", "mushroom", "olive", "pepper"], 2)  ->
#       [("ham", "mushroom"), ("ham", "olive"), ("ham", "pepper"),
#        ("mushroom", "olive"), ("mushroom", "pepper"), ("olive", "pepper")]
#   That's 6 choices.
#
# HINT
#   First get it passing with itertools.combinations.
#   Then delete that and write it yourself with recursion: for the first
#   topping, either take it (and choose k - 1 from the rest) or leave it
#   (and choose k from the rest). a_lesson.md has this written out, under
#   "The pattern, in general".
#
# VIDEO (try the problem yourself for 20-30 minutes first, then watch)
#   Combinations - Leetcode 77 - Python (NeetCode)
#   https://www.youtube.com/watch?v=q0s6m7AiM7o
#   This problem uses the same method as LeetCode 77 Combinations. The video uses a
#   different story and different names, so watch for the method, not the details.
def topping_choices(toppings, k):
    pass


# =============================================================================
# 3. FILL THE VAN EXACTLY
# =============================================================================
# THE PROBLEM
#   Your pizza shop is delivering to a big event. You've hired a van that
#   carries exactly a set number of pizza boxes, and the hire company charges
#   the same however full it is. So you want to send a group of orders that
#   fills it exactly, with no empty space.
#
#   Each order has a number of pizzas, and an order can't be split. Out of the
#   orders waiting, find a group whose pizzas add up exactly to the van's
#   capacity. Use as few orders as possible, so there are fewer stops.
#
# THE DATA
#   orders = [("a", 3), ("b", 5), ("c", 2), ("d", 4)]
#   capacity = 9
#   Each order is (order name, number of pizzas).
#
# YOUR TASK
#   fill_the_van(orders, capacity) takes the list of orders and the van's
#   capacity in pizzas. It returns a list of order names whose
#   pizzas add up to exactly capacity, using the fewest orders possible.
#   If several groups tie for fewest, any of them is fine.
#   Return None if no group adds up exactly.
#   A capacity of 0 is filled by no orders at all: [].
#
# EXAMPLE
#   Groups that add up to 9:
#       b + d      = 5 + 4     = 9   (2 orders)
#       a + c + d  = 3 + 2 + 4 = 9   (3 orders)
#   fill_the_van(orders, 9)   ->  ["b", "d"]
#   fill_the_van(orders, 1)   ->  None   (no order is that small)
#
# HINT
#   Try groups of size 0, then size 1, then size 2, and so on, with
#   combinations(orders, size). The first group that adds up exactly is
#   automatically one of the smallest.
#
# VIDEO (try the problem yourself for 20-30 minutes first, then watch)
#   Subsets - Backtracking - Leetcode 78 (NeetCode)
#   https://www.youtube.com/watch?v=REOH22Xwdkk
#   This problem uses the same method as LeetCode 78 Subsets. The video uses a different
#   story and different names, so watch for the method, not the details.
def fill_the_van(orders, capacity):
    pass
