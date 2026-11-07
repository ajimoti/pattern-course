"""
PATTERN 12: FASTEST ROUTE (DIJKSTRA) - SOLUTIONS
"""
import heapq


# =============================================================================
# 1. THE FASTEST WAY TO A CUSTOMER
# =============================================================================
# Idea: always carry on from the place you can reach soonest (the heap gives
# you that). For each road out of it, update the next place if this way is
# quicker, and remember where you came from. When you pick the customer,
# that time is the fastest. Walk back through came_from to get the route.
# Speed: roughly (number of roads) x log(number of roads). Fast.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Implement Dijkstra's Algorithm (NeetCodeIO)
#   https://www.youtube.com/watch?v=XEb7_z5dG3c
#   Same idea as LeetCode Dijkstra in Python. The video uses a different story and
#   different names, so watch for the method, not the details.
def fastest_route(roads, start, end):
    # Step 1: for each place, list the roads leaving it (roads go both ways)
    roads_from = {}
    for a, b, minutes in roads:
        if a not in roads_from:
            roads_from[a] = []
        if b not in roads_from:
            roads_from[b] = []
        roads_from[a].append((b, minutes))
        roads_from[b].append((a, minutes))

    best = {start: 0}          # quickest time found so far to each place
    came_from = {}             # the place before it on that quickest route
    done = set()               # places we've finished with
    to_visit = [(0, start)]    # heap of (time to get there, place)

    while to_visit:
        time, place = heapq.heappop(to_visit)      # the place we can reach soonest
        if place in done:
            continue                               # old entry, skip it
        done.add(place)

        if place == end:
            route = [end]
            while route[-1] != start:
                route.append(came_from[route[-1]])
            route.reverse()
            return time, route

        for next_place, minutes in roads_from.get(place, []):
            new_time = time + minutes
            if next_place not in best or new_time < best[next_place]:
                best[next_place] = new_time
                came_from[next_place] = place
                heapq.heappush(to_visit, (new_time, next_place))

    return -1, []


# =============================================================================
# 2. FASTEST TIME FROM THE SHOP TO EVERY PLACE
# =============================================================================
# Idea: exactly problem 1, but don't stop at a customer. Keep going until the
# heap is empty. Every place you could reach ends up in `best` with its
# fastest time. Places you can't reach never get added.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Dijkstra Algorithm - Single Source Shortest Path - Greedy Method (Abdul Bari)
#   https://www.youtube.com/watch?v=XB4MIexjvY0
#   Same idea as LeetCode Shortest path to every place. The video uses a different story and
#   different names, so watch for the method, not the details.
def fastest_times(roads, start):
    roads_from = {}
    for a, b, minutes in roads:
        roads_from.setdefault(a, []).append((b, minutes))
        roads_from.setdefault(b, []).append((a, minutes))

    best = {start: 0}
    done = set()
    to_visit = [(0, start)]

    while to_visit:
        time, place = heapq.heappop(to_visit)
        if place in done:
            continue
        done.add(place)

        for next_place, minutes in roads_from.get(place, []):
            new_time = time + minutes
            if next_place not in best or new_time < best[next_place]:
                best[next_place] = new_time
                heapq.heappush(to_visit, (new_time, next_place))

    return best


# =============================================================================
# 3. WHEN HAS EVERY SHOP GOT THE PROMO MESSAGE?
# =============================================================================
# Idea: find the fastest time the message reaches each shop (same as problem
# 2, but links only go ONE way). Every shop has it once the slowest one does,
# so the answer is the biggest of those times. If any shop is never reached,
# return -1.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Network Delay Time - Dijkstra's algorithm - Leetcode 743 (NeetCode)
#   https://www.youtube.com/watch?v=EaphyqKU4PQ
#   Same idea as LeetCode 743 Network Delay Time. The video uses a different story and
#   different names, so watch for the method, not the details.
def everyone_has_message(links, shops, start):
    links_from = {}
    for sender, receiver, minutes in links:
        links_from.setdefault(sender, []).append((receiver, minutes))   # one way only

    best = {start: 0}
    done = set()
    to_visit = [(0, start)]

    while to_visit:
        time, shop = heapq.heappop(to_visit)
        if shop in done:
            continue
        done.add(shop)

        for next_shop, minutes in links_from.get(shop, []):
            new_time = time + minutes
            if next_shop not in best or new_time < best[next_shop]:
                best[next_shop] = new_time
                heapq.heappush(to_visit, (new_time, next_shop))

    for shop in shops:
        if shop not in best:
            return -1                              # this shop never gets it
    return max(best[shop] for shop in shops)
