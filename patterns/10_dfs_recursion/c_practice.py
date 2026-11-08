"""
PATTERN 10: DFS and recursion (go deep first)
Read a_lesson.md first. Test with:  python practice.py 10
"""


# =============================================================================
# 1. HOW MANY PIZZAS ARE IN THIS DEAL?
# =============================================================================
# THE PROBLEM
#   Your shop sells combo deals, and some deals include other deals. The
#   Family deal comes with two pizzas of its own, plus a Kids box and a Party
#   add-on. The Party add-on has a pizza of its own, plus a Mini pack.
#
#   The kitchen needs to know how many pizzas to make when someone orders a
#   deal. Work out the total number of pizzas in a deal, including everything
#   inside it, however many levels deep it goes.
#
# THE DATA
#   mini_pack   = {"name": "Mini pack",    "pizzas": 3, "contains": []}
#   kids_box    = {"name": "Kids box",     "pizzas": 1, "contains": []}
#   party_addon = {"name": "Party add-on", "pizzas": 1, "contains": [mini_pack]}
#   family_deal = {"name": "Family deal",  "pizzas": 2,
#                  "contains": [kids_box, party_addon]}
#
# YOUR TASK
#   total_pizzas(deal) returns the total number of pizzas in the deal,
#   counting every deal inside it at every level.
#
# EXAMPLE
#   Kids box     = 1                     (contains nothing)
#   Mini pack    = 3                     (contains nothing)
#   Party add-on = 1 + Mini pack (3)     = 4
#   Family deal  = 2 + Kids box (1) + Party add-on (4) = 7
#
#   total_pizzas(family_deal)  ->  7
#
# HINT
#   Start with the deal's own pizzas, then add total_pizzas() of each deal in
#   its "contains" list.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   5 Simple Steps for Solving Any Recursive Problem (Reducible)
#   https://www.youtube.com/watch?v=ngCos392W4w
def total_pizzas(deal):
    pass


# =============================================================================
# 2. HOW MANY DIFFERENT ROUTES ARE THERE?
# =============================================================================
# THE PROBLEM
#   The streets around your shop are all one-way. A new driver wants to know
#   how many different routes there are from the shop to a customer, so they
#   can learn them all.
#
#   You have a list of which places each place's one-way streets lead to. The
#   streets never lead you back to somewhere you've already been, so a driver
#   can't go round in circles.
#
# THE DATA
#   roads = {
#       "Shop": ["A", "B"],
#       "A":    ["C"],
#       "B":    ["A", "C"],
#       "C":    [],
#   }
#   roads["B"] = ["A", "C"] means one-way streets lead from B to A and from B to C.
#   A place with no streets out might be missing from the dict altogether.
#
# YOUR TASK
#   count_routes(roads, start, end) returns how many different routes go
#   from start to end. If start and end are the same place, that counts as 1
#   route (you're already there).
#
# EXAMPLE
#   Routes from Shop to C:
#       Shop -> A -> C
#       Shop -> B -> A -> C
#       Shop -> B -> C
#   count_routes(roads, "Shop", "C")  ->  3
#
#   Routes from A to C: just A -> C       ->  1
#   Routes from C to Shop: none            ->  0
#
# HINT
#   The routes from a place = the routes from each place its streets lead to,
#   added together. Stopping point: if you're at the end, that's 1 route.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Learn Depth First Search in 7 minutes (Bro Code)
#   https://www.youtube.com/watch?v=by93qH4ACxo
#   Same idea as LeetCode 797 All Paths From Source to Target. The video uses a different story and
#   different names, so watch for the method, not the details.
def count_routes(roads, start, end):
    pass


# =============================================================================
# 3. HOW MANY SEPARATE NEIGHBOURHOODS ARE THERE?
# =============================================================================
# THE PROBLEM
#   You're splitting the town into delivery areas. A driver can only move up,
#   down, left or right along roads, and buildings block the way. Any roads a
#   driver can get between without crossing a building belong to the same
#   neighbourhood.
#
#   Count how many separate neighbourhoods there are, so you know how many
#   delivery areas you need.
#
# THE DATA
#   grid = ["..#.",
#           ".##.",
#           "#..#"]
#   "." = road, "#" = building. grid[row][col] gives the symbol at (row, col).
#
# YOUR TASK
#   count_neighbourhoods(grid) returns the number of separate groups of
#   connected road squares. An empty grid, or one with no roads, has 0.
#
# EXAMPLE
#   Neighbourhood 1: (0,0), (0,1), (1,0)
#   Neighbourhood 2: (0,3), (1,3)
#   Neighbourhood 3: (2,1), (2,2)
#   count_neighbourhoods(grid)  ->  3
#
#   (2,1) and (1,0) aren't connected: (2,0) and (1,1) are both buildings.
#
# HINT
#   Go through every square. When you find a road square you haven't seen,
#   that's a new neighbourhood: add 1, then call a recursive explore(row, col)
#   that marks every road square connected to it as seen.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Number of Islands - Leetcode 200 - Graphs (Python) (Greg Hogg)
#   https://www.youtube.com/watch?v=gCswsDauXPc
#   Same idea as LeetCode 200 Number of Islands. The video uses a different story and
#   different names, so watch for the method, not the details.
def count_neighbourhoods(grid):
    pass
