"""
PATTERN 09: BFS - solutions
"""
from collections import deque


# 1. NEAREST CUSTOMER ON THE MAP
# Build the graph (square -> squares one move away), then BFS from the shop
# carrying the minutes. The first customer taken off the queue is the nearest.
# Speed: every square is checked at most once, so it grows with the size of the map.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Breadth First Search grid shortest path (WilliamFiset)
#   https://www.youtube.com/watch?v=KiCBXu4P-2Y
#   Same idea as LeetCode 1091 Shortest Path in Binary Matrix. The video uses a different story and
#   different names, so watch for the method, not the details.
def build_graph(grid):
    rows = len(grid)
    cols = len(grid[0])
    graph = {}
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "#":
                continue
            nearby = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            graph[(row, col)] = []
            for r, c in nearby:
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] != "#":
                    graph[(row, col)].append((r, c))
    return graph


def nearest_customer(grid):
    graph = build_graph(grid)

    for (row, col) in graph:
        if grid[row][col] == "S":
            shop = (row, col)

    search_queue = deque()
    search_queue.append((shop, 0))
    searched = set()

    while search_queue:
        square, minutes = search_queue.popleft()
        if square not in searched:
            row, col = square
            if grid[row][col] == "C":
                return minutes
            else:
                for next_square in graph[square]:
                    search_queue.append((next_square, minutes + 1))
                searched.add(square)
    return -1


# 2. HOW MANY REFERRAL STEPS BETWEEN TWO CUSTOMERS?
# The links dict is already the graph. BFS from start, carrying the steps.
# Speed: each customer and each link is looked at once.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Breadth First Search Algorithm (Shortest Path, Graph Theory) (WilliamFiset)
#   https://www.youtube.com/watch?v=oDqjPvD54Ss
#   Same idea as LeetCode BFS shortest path. The video uses a different story and
#   different names, so watch for the method, not the details.
def referral_steps(links, start, target):
    search_queue = deque()
    search_queue.append((start, 0))
    searched = set()

    while search_queue:
        person, steps = search_queue.popleft()
        if person in searched:
            continue
        searched.add(person)

        if person == target:
            return steps

        for friend in links.get(person, []):
            search_queue.append((friend, steps + 1))
    return -1


# 3. HOW LONG UNTIL EVERY SHOP HEARS THE NEWS?
# BFS from start, recording the minute each shop first hears. If any shop is
# missing at the end, it never heard. Otherwise the answer is the latest minute.
# Speed: each shop and each call is looked at once.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Rotting Oranges - Leetcode 994 - Python (NeetCode)
#   https://www.youtube.com/watch?v=y704fEOx0s0
#   Same idea as LeetCode 994 Rotting Oranges. The video uses a different story and
#   different names, so watch for the method, not the details.
def minutes_until_everyone_knows(calls, start):
    heard_at = {}                         # shop -> minute it first heard
    search_queue = deque()
    search_queue.append((start, 0))

    while search_queue:
        shop, minute = search_queue.popleft()
        if shop in heard_at:
            continue
        heard_at[shop] = minute

        for other in calls.get(shop, []):
            search_queue.append((other, minute + 1))

    if len(heard_at) < len(calls):        # some shop never heard
        return -1
    return max(heard_at.values())
