"""
PATTERN 08: HEAP - SOLUTIONS
"""
import heapq


# 1. GIVING ORDERS TO DRIVERS
# Heap of "minute each driver is back". Pop the soonest, push them back with
# their new return time. O(n log d): n orders, d drivers.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Single-Threaded CPU - Priority Queue - Leetcode 1834 - Python (NeetCode)
#   https://www.youtube.com/watch?v=RR1n-d4oYqE
#   Same idea as LeetCode 1834 Single-Threaded CPU (similar idea). The video uses a different story and
#   different names, so watch for the method, not the details.
def dispatch(orders, drivers, trip):
    back_at = [0] * drivers
    leaves = {}
    for order_id, ready in orders:
        soonest = heapq.heappop(back_at)
        leave_time = max(ready, soonest)
        leaves[order_id] = leave_time
        heapq.heappush(back_at, leave_time + trip)
    return leaves


# 2. THE CLOSEST CUSTOMERS
# Push (distance, name) so the heap sorts by distance, then by name on a tie.
# Pop k times. O(n log n) for the pushes.
#
# Watch it run: after pushing everything, popping gives
#   (1.2, "Ben"), (1.2, "Dev"), (3.0, "Chloe"), ...   -> keep the first 3 names
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   K Closest Points to Origin - Heap / Priority Queue - Leetcode 973 (NeetCode)
#   https://www.youtube.com/watch?v=rI2EBUEMfTk
#   Same idea as LeetCode 973 K Closest Points to Origin. The video uses a different story and
#   different names, so watch for the method, not the details.
def closest_customers(customers, k):
    heap = []
    for name, distance in customers:
        heapq.heappush(heap, (distance, name))

    result = []
    for _ in range(min(k, len(heap))):
        distance, name = heapq.heappop(heap)
        result.append(name)
    return result

# Shortcut you can mention in an interview:
#   [name for name, d in heapq.nsmallest(k, customers, key=lambda c: (c[1], c[0]))]


# 3. MERGE SORTED ORDER LISTS
# Heap holds one item per list: (minute, which list, position in that list).
# Pop the smallest, then push the next item from the same list.
# O(N log s): N = all minutes, s = number of shops.
#
# Watch it run on [[1, 5, 9], [2, 3, 10], [4]]
#   pop          result so far          push next from same list   heap after (minutes)
#   (1, 0, 0)    [1]                    (5, 0, 1)                   2, 4, 5
#   (2, 1, 0)    [1, 2]                 (3, 1, 1)                   3, 4, 5
#   (3, 1, 1)    [1, 2, 3]              (10, 1, 2)                  4, 5, 10
#   (4, 2, 0)    [1, 2, 3, 4]           list 2 has no more          5, 10
#   (5, 0, 1)    [1, 2, 3, 4, 5]        (9, 0, 2)                   9, 10
#   (9, 0, 2)    [..., 9]               list 0 has no more          10
#   (10, 1, 2)   [..., 9, 10]           list 1 has no more          empty -> done
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Merge K Sorted Lists - Leetcode 23 - Python (NeetCode)
#   https://www.youtube.com/watch?v=q5a5OiGbT6Q
#   Same idea as LeetCode 23 Merge k Sorted Lists. The video uses a different story and
#   different names, so watch for the method, not the details.
def merge_order_lists(shop_lists):
    heap = []
    for which, shop in enumerate(shop_lists):
        if shop:                                         # skip empty lists
            heapq.heappush(heap, (shop[0], which, 0))

    merged = []
    while heap:
        minute, which, position = heapq.heappop(heap)
        merged.append(minute)
        next_position = position + 1
        if next_position < len(shop_lists[which]):
            next_minute = shop_lists[which][next_position]
            heapq.heappush(heap, (next_minute, which, next_position))
    return merged

# Python also has this built in: list(heapq.merge(*shop_lists))
