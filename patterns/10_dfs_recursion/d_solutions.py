"""
PATTERN 10: DFS and recursion - solutions
"""


# 1. HOW MANY PIZZAS ARE IN THIS DEAL?
# A deal's total = its own pizzas + the total of each deal inside it.
# Stopping point: a deal that contains nothing (the loop runs zero times).
# Speed: each deal is visited once.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   5 Simple Steps for Solving Any Recursive Problem (Reducible)
#   https://www.youtube.com/watch?v=ngCos392W4w
def total_pizzas(deal):
    total = deal["pizzas"]
    for inner_deal in deal["contains"]:
        total += total_pizzas(inner_deal)
    return total


# 2. HOW MANY DIFFERENT ROUTES ARE THERE?
# Routes from a place = sum of the routes from each place its streets lead to.
# Stopping point: being at the end counts as 1 route.
# Speed: fine for small maps. On big maps the same place gets counted many
# times; you'd remember answers in a dict (that's Pattern 14, dynamic programming).
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Learn Depth First Search in 7 minutes (Bro Code)
#   https://www.youtube.com/watch?v=by93qH4ACxo
#   Same idea as LeetCode 797 All Paths From Source to Target. The video uses a different story and
#   different names, so watch for the method, not the details.
def count_routes(roads, start, end):
    if start == end:
        return 1
    total = 0
    for next_place in roads.get(start, []):
        total += count_routes(roads, next_place, end)
    return total


# 3. HOW MANY SEPARATE NEIGHBOURHOODS ARE THERE?
# Go through every square. A road square not yet seen starts a new
# neighbourhood: count it, then explore() marks everything connected to it.
# Speed: each square is visited once.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Number of Islands - Leetcode 200 - Graphs (Python) (Greg Hogg)
#   https://www.youtube.com/watch?v=gCswsDauXPc
#   Same idea as LeetCode 200 Number of Islands. The video uses a different story and
#   different names, so watch for the method, not the details.
def count_neighbourhoods(grid):
    if not grid:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    seen = set()

    def explore(row, col):
        if not (0 <= row < rows and 0 <= col < cols):
            return                                   # off the map
        if grid[row][col] == "#" or (row, col) in seen:
            return                                   # building, or already done
        seen.add((row, col))
        explore(row - 1, col)                        # up
        explore(row + 1, col)                        # down
        explore(row, col - 1)                        # left
        explore(row, col + 1)                        # right

    count = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != "#" and (row, col) not in seen:
                count += 1
                explore(row, col)
    return count
