"""
PATTERN 09: BFS (spread out one step at a time)
Read lesson.md first. Test with:  python practice.py 9
"""
from collections import deque


# =============================================================================
# 1. NEAREST CUSTOMER ON THE MAP
# =============================================================================
# THE PROBLEM
#   Your pizza shop has several customers waiting for their deliveries, and
#   you want to find out which one your driver can reach the fastest.
#
#   You have a map of the surrounding streets drawn as a grid. Your driver can
#   move one square at a time, up, down, left or right, and each move takes
#   one minute. Buildings block the way, so the driver has to go around them.
#   A customer who looks close might actually take longer to reach.
#
# THE DATA
#   grid = ["S.#C",
#           ".##.",
#           "...C"]
#   "S" = shop, "C" = customer, "#" = building, "." = road
#   grid[row][col] gives the symbol at (row, col). The shop is at (0, 0).
#
# YOUR TASK
#   Write two functions:
#
#   build_graph(grid) returns a dict: each square that isn't a building ->
#   a list of the squares you can drive to in one move (up, down, left,
#   right, in that order), leaving out squares off the map and buildings.
#
#   nearest_customer(grid) returns the minutes to the nearest customer,
#   or -1 if no customer can be reached.
#
# EXAMPLE
#   build_graph(grid)[(1, 0)]  ->  [(0, 0), (2, 0)]
#       up (0,0) is the shop, keep. down (2,0) is road, keep.
#       left (1,-1) is off the map. right (1,1) is a building.
#
#   nearest_customer(grid)  ->  5
#       (0,0) -> (1,0) -> (2,0) -> (2,1) -> (2,2) -> (2,3) is 5 moves.
#       The customer at (0,3) is blocked by the building at (0,2).
#
# HINT
#   Build the graph first, then search it exactly like the mango seller,
#   with each queue item being (square, minutes).
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Breadth First Search grid shortest path (WilliamFiset)
#   https://www.youtube.com/watch?v=KiCBXu4P-2Y
#   Same idea as LeetCode 1091 Shortest Path in Binary Matrix. The video uses a different story and
#   different names, so watch for the method, not the details.
def build_graph(grid):
    pass


def nearest_customer(grid):
    pass


# =============================================================================
# 2. HOW MANY REFERRAL STEPS BETWEEN TWO CUSTOMERS?
# =============================================================================
# THE PROBLEM
#   Your shop runs a "refer a friend" scheme, and you keep a record of which
#   customers are linked because one referred the other.
#
#   Marketing wants to know how closely two customers are connected. If Ada
#   referred Ben, they're 1 step apart. If Ben then referred Dev, Ada and Dev
#   are 2 steps apart. Find the smallest number of steps between two
#   customers, or say they aren't connected at all.
#
# THE DATA
#   links = {
#       "Ada":  ["Ben", "Cara"],
#       "Ben":  ["Ada", "Dev"],
#       "Cara": ["Ada"],
#       "Dev":  ["Ben", "Esi"],
#       "Esi":  ["Dev"],
#       "Femi": [],
#   }
#   Each customer -> the customers they're directly linked to.
#   Links are written down in both directions.
#
# YOUR TASK
#   referral_steps(links, start, target) returns the fewest steps from start
#   to target. Return 0 if start and target are the same person.
#   Return -1 if they aren't connected.
#
# EXAMPLE
#   referral_steps(links, "Ada", "Esi")   ->  3   (Ada -> Ben -> Dev -> Esi)
#   referral_steps(links, "Ada", "Cara")  ->  1
#   referral_steps(links, "Ada", "Femi")  ->  -1  (Femi isn't linked to anyone)
#
# HINT
#   This is the mango seller with steps counted, like problem 1 but without
#   having to build the graph: the links dict already is the graph.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Breadth First Search Algorithm (Shortest Path, Graph Theory) (WilliamFiset)
#   https://www.youtube.com/watch?v=oDqjPvD54Ss
#   Same idea as LeetCode BFS shortest path. The video uses a different story and
#   different names, so watch for the method, not the details.
def referral_steps(links, start, target):
    pass


# =============================================================================
# 3. HOW LONG UNTIL EVERY SHOP HEARS THE NEWS?
# =============================================================================
# THE PROBLEM
#   Head office has changed the price of a margherita and phones one shop
#   with the news. Each shop has a list of other shops it calls straight away
#   when it hears something, and each call takes one minute.
#
#   You want to know how many minutes it will be before every shop knows. If
#   some shop will never hear because nobody calls it, you need to know that
#   too.
#
# THE DATA
#   calls = {
#       "Central": ["North", "East"],
#       "North":   ["Central", "West"],
#       "East":    ["Central"],
#       "West":    ["North"],
#   }
#   start = "Central"    (the shop head office phones, at minute 0)
#
# YOUR TASK
#   minutes_until_everyone_knows(calls, start) returns the number of minutes
#   until the last shop hears the news. Every shop is a key in `calls`.
#   Return -1 if at least one shop never hears.
#
# EXAMPLE
#   minute 0: Central knows
#   minute 1: Central calls North and East
#   minute 2: North calls West
#   Every shop knows after 2 minutes  ->  2
#
#   If there were also a shop "South": [] that nobody calls  ->  -1
#
# HINT
#   BFS from start, remembering the minutes for each shop you reach. At the
#   end, check every shop was reached, and return the biggest minutes.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Rotting Oranges - Leetcode 994 - Python (NeetCode)
#   https://www.youtube.com/watch?v=y704fEOx0s0
#   Same idea as LeetCode 994 Rotting Oranges. The video uses a different story and
#   different names, so watch for the method, not the details.
def minutes_until_everyone_knows(calls, start):
    pass
