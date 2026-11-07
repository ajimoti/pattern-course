"""
PATTERN 05: SORT, THEN WALK THROUGH ONCE - SOLUTIONS
"""


# 1. HOW MANY OVENS
# Turn each bake into +1 (in) and -1 (out), sort, keep a running count.
# At the same minute, (10, -1) sorts before (10, 1), so "out" is handled first.
# Speed: O(n log n) because of the sort.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Meeting Rooms II - Leetcode 253 - Python (NeetCode)
#   https://www.youtube.com/watch?v=FdzJmTCVyJU
#   Same idea as LeetCode 253 Meeting Rooms II. The video uses a different story and
#   different names, so watch for the method, not the details.
def min_ovens(bakes):
    timeline = []
    for start, finish in bakes:
        timeline.append((start, 1))
        timeline.append((finish, -1))

    timeline = sorted(timeline)

    in_oven = 0
    most_at_once = 0
    for _, change in timeline:
        in_oven += change
        most_at_once = max(most_at_once, in_oven)
    return most_at_once


# 2. MERGE OVERLAPPING DRIVER SHIFTS
# Sort by start. Compare each shift with the last block built so far:
#   starts at or before that block ends -> stretch the block
#   starts after it ends                -> start a new block
# Speed: O(n log n) because of the sort.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Merge Intervals - Sorting - Leetcode 56 (NeetCode)
#   https://www.youtube.com/watch?v=44H3cEC2fFM
#   Same idea as LeetCode 56 Merge Intervals. The video uses a different story and
#   different names, so watch for the method, not the details.
def merge_shifts(shifts):
    blocks = []
    for start, end in sorted(shifts):
        if blocks and start <= blocks[-1][1]:          # touches the last block
            last_start, last_end = blocks[-1]
            blocks[-1] = (last_start, max(last_end, end))   # max: a shift may sit inside the block
        else:
            blocks.append((start, end))
    return blocks


# 3. CAN ONE DRIVER DO EVERY DELIVERY?
# Sort by leave time. Each delivery must leave at or after the previous one is back.
# Speed: O(n log n) because of the sort.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Meeting Rooms - Leetcode 252 - Python (NeetCode)
#   https://www.youtube.com/watch?v=PaJxqZVPhbg
#   Same idea as LeetCode 252 Meeting Rooms. The video uses a different story and
#   different names, so watch for the method, not the details.
def can_one_driver(deliveries):
    back_at = None
    for leaves, back in sorted(deliveries):
        if back_at is not None and leaves < back_at:
            return False
        back_at = back
    return True
