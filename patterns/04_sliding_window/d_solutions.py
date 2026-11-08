"""
PATTERN 04: SLIDING WINDOW - SOLUTIONS
"""


# 1. THE BEST THREE DAYS IN A ROW
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Maximum Average Subarray I - LeetCode 643 - Python (Deepti Talesra)
#   https://www.youtube.com/watch?v=etiqMUxUEmc
#   Same idea as LeetCode 643 Maximum Average Subarray I. The video uses a different story and
#   different names, so watch for the method, not the details.
def best_run(revenue, k):
    if k <= 0 or k > len(revenue):
        return None

    total = sum(revenue[:k])                  # the first k days
    best_total = total
    best_start = 0

    for new_day in range(k, len(revenue)):
        old_day = new_day - k                 # drops off the front
        total = total + revenue[new_day] - revenue[old_day]
        start = old_day + 1
        if total > best_total:                # > keeps the earlier one on a tie
            best_total = total
            best_start = start

    return (best_start, best_total)
# Speed: one pass through the list, whatever k is. Adding each stretch from
# scratch would be (number of days) x k additions.


# 2. HOW MANY STRETCHES HIT THE TARGET?
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Number of Subarrays of size K and Average >= Threshold - Leetcode 1343 (NeetCodeIO)
#   https://www.youtube.com/watch?v=D8B4tKxMTnY
#   Same idea as LeetCode 1343 Sub-arrays of Size K with Average >= Threshold. The video uses a different story and
#   different names, so watch for the method, not the details.
def count_good_stretches(revenue, k, target):
    if k <= 0 or k > len(revenue):
        return 0

    total = sum(revenue[:k])
    count = 1 if total >= target else 0      # don't forget the first stretch

    for new_day in range(k, len(revenue)):
        total = total + revenue[new_day] - revenue[new_day - k]
        if total >= target:
            count += 1

    return count
# Speed: one pass through the list.


# 3. THE LONGEST STRETCH WITH AT MOST K LATE DELIVERIES
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Max Consecutive Ones III (Deepti Talesra)
#   https://www.youtube.com/watch?v=ZpsdDNbCgc0
#   Same idea as LeetCode 1004 Max Consecutive Ones III. The video uses a different story and
#   different names, so watch for the method, not the details.
def longest_stretch(deliveries, k):
    left = 0                                  # front of the window
    late = 0                                  # late deliveries in the window
    best = 0

    for right in range(len(deliveries)):      # right = end of the window
        if deliveries[right] == "L":
            late += 1

        while late > k:                       # too many late: shrink from the front
            if deliveries[left] == "L":
                late -= 1
            left += 1

        best = max(best, right - left + 1)    # window length

    return best
# Speed: every delivery joins the window once and leaves at most once, so it's
# one pass. Checking every possible run would be list length x list length.
