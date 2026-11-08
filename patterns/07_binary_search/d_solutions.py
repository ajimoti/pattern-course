"""
PATTERN 07: BINARY SEARCH - SOLUTIONS
"""


# 1. FIND AN ORDER
# Check the middle, keep the half the target must be in. O(log n).
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Binary Search - Leetcode 704 - Python (NeetCode)
#   https://www.youtube.com/watch?v=s4DPM8ct1pI
#   Same idea as LeetCode 704 Binary Search. The video uses a different story and
#   different names, so watch for the method, not the details.
def find_order(order_ids, target):
    low = 0
    high = len(order_ids) - 1
    while low <= high:
        middle = (low + high) // 2
        if order_ids[middle] == target:
            return middle
        elif order_ids[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1


# 2. FIRST DELIVERY AT OR AFTER A TIME
# Same loop, but when the middle time is late enough, remember it as the best
# answer so far and keep looking LEFT for an earlier one. O(log n).
#
# Watch it run: leave_times = [5, 12, 12, 20, 31], ready = 13
#   low high middle value  >= 13?  best  next
#   0   4    2      12     no      -1    low = 3
#   3   4    3      20     yes     20    high = 2
#   3   2    stop (low past high)  -> return 20
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   BS-2. Implement Lower Bound and Upper Bound | Search Insert Position (take U forward)
#   https://www.youtube.com/watch?v=6zhGS79oQ4k
#   Same idea as LeetCode 35 Search Insert Position. The video uses a different story and
#   different names, so watch for the method, not the details.
def first_departure(leave_times, ready):
    low = 0
    high = len(leave_times) - 1
    best = -1
    while low <= high:
        middle = (low + high) // 2
        if leave_times[middle] >= ready:
            best = leave_times[middle]   # a possible answer...
            high = middle - 1            # ...but look left for an earlier one
        else:
            low = middle + 1
    return best


# The same thing with Python's built-in binary search:
#   import bisect
#   i = bisect.bisect_left(leave_times, ready)
#   return leave_times[i] if i < len(leave_times) else -1


# 3. SLOWEST ROBOT SPEED
# There's no list to search, so search the possible SPEEDS instead (1 to the biggest pile).
# If a speed works, every faster speed works too, so we can halve the range each time.
# Speed: O(n log m), where n = number of shops and m = biggest pile.
#
# Watch it run: piles = [3, 6, 7, 11], hours = 8
#   low high middle  hours_needed(middle)          fits?  next
#   1   11   6       1+1+2+2 = 6                   yes    answer = 6, high = 5
#   1   5    3       1+2+3+4 = 10                  no     low = 4
#   4   5    4       1+2+2+3 = 8                   yes    answer = 4, high = 3
#   4   3    stop -> return 4
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Koko Eating Bananas - Binary Search - Leetcode 875 - Python (NeetCode)
#   https://www.youtube.com/watch?v=U2SozAs9RzA
#   Same idea as LeetCode 875 Koko Eating Bananas. The video uses a different story and
#   different names, so watch for the method, not the details.
def slowest_speed(piles, hours):
    def hours_needed(speed):
        total = 0
        for pile in piles:
            total += (pile + speed - 1) // speed     # divide and round up
        return total

    low = 1
    high = max(piles)
    answer = high
    while low <= high:
        middle = (low + high) // 2
        if hours_needed(middle) <= hours:
            answer = middle            # this speed works...
            high = middle - 1          # ...try slower
        else:
            low = middle + 1           # too slow, try faster
    return answer
