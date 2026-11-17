"""
PATTERN 04: SLIDING WINDOW - PRACTICE
Read a_lesson.md first. Write your code where it says `pass`.
Test from the pattern_course folder:   python3 practice.py 4
"""


# =============================================================================
# 1. THE BEST THREE DAYS IN A ROW
# =============================================================================
# THE PROBLEM
#   The owner of your pizza shop is planning a three-day promotion for next
#   year and wants to copy the timing of this year's best three-day stretch.
#   She has the takings (money taken) for each day and wants to know which
#   three days in a row brought in the most money.
#
#   Her real figures cover a whole year (THE DATA below is a short sample), so
#   adding up every stretch from scratch would mean a lot of repeated adding.
#   As the stretch moves along by one day, add the day that joins and take
#   away the day that drops off.
#
# THE DATA
#   revenue = [120, 80, 200, 150, 90, 300]    takings for day 0 ... day 5
#   k = 3                                     days in a row
#
# YOUR TASK
#   best_run(revenue, k) returns (start day, total) for the k days in a row
#   with the highest total. If two stretches tie, return the earlier one.
#   If k is 0 or less, or bigger than len(revenue), return None.
#
# EXAMPLE
#   Days 0-2: 120 + 80 + 200       = 400
#   Days 1-3: 400 - 120 + 150      = 430
#   Days 2-4: 430 - 80  + 90       = 440
#   Days 3-5: 440 - 200 + 300      = 540   <- best
#   best_run(revenue, 3)  ->  (3, 540)
#
# HINT
#   Add up the first k days once with sum(revenue[:k]). Then loop new_day
#   (the day that joins) from k to the last day. The day dropping off is
#   new_day - k.
#
# VIDEO (try the problem yourself for 20-30 minutes first, then watch)
#   Maximum Average Subarray I - LeetCode 643 - Python (Deepti Talesra)
#   https://www.youtube.com/watch?v=etiqMUxUEmc
#   This problem uses the same method as LeetCode 643 Maximum Average Subarray I. The
#   video uses a different story and different names, so watch for the method, not the
#   details.
def best_run(revenue, k):
    pass


# =============================================================================
# 2. HOW MANY STRETCHES HIT THE TARGET?
# =============================================================================
# THE PROBLEM
#   Your pizza shop belongs to a chain. Head office gives each shop a bonus
#   for every three-day stretch where the takings (money taken) reach £435 or
#   more. Stretches can overlap: days 1-3 and days 2-4 both count if they
#   both reach the target.
#
#   Your shop's owner wants to know how many bonuses she's earned this week.
#
# THE DATA
#   revenue = [120, 80, 200, 150, 90, 300]
#   k = 3
#   target = 435
#
# YOUR TASK
#   count_good_stretches(revenue, k, target) returns how many runs of k days
#   in a row have a total of target or more.
#   If k is 0 or less, or bigger than len(revenue), return 0.
#
# EXAMPLE
#   Days 0-2: 400  -> below 435
#   Days 1-3: 430  -> below 435
#   Days 2-4: 440  -> reaches 435   count 1
#   Days 3-5: 540  -> reaches 435   count 2
#   count_good_stretches(revenue, 3, 435)  ->  2
#
# HINT
#   Keep a running total the same way as in problem 1 in this file: add the
#   day that joins, take away the day that drops off. Check the first
#   stretch too, not just the ones inside the loop.
#
# VIDEO (try the problem yourself for 20-30 minutes first, then watch)
#   Number of Subarrays of size K and Average >= Threshold - Leetcode 1343 (NeetCodeIO)
#   https://www.youtube.com/watch?v=D8B4tKxMTnY
#   This problem uses the same method as LeetCode 1343 Sub-arrays of Size K with Average
#   >= Threshold. The video uses a different story and different names, so watch for the
#   method, not the details.
def count_good_stretches(revenue, k, target):
    pass


# =============================================================================
# 3. THE LONGEST STRETCH WITH AT MOST K LATE DELIVERIES
# =============================================================================
# THE PROBLEM
#   Your pizza shop's drivers get a weekly award for their longest run of
#   deliveries where no more than one was late. Each delivery is marked "O"
#   for on time or "L" for late, in the order they happened.
#
#   The length of the run isn't fixed. Keep making the run longer from the
#   end, and whenever it has too many late deliveries, drop deliveries from
#   the front until it's back within the limit. Read the "grows and shrinks"
#   section in a_lesson.md first.
#
# THE DATA
#   deliveries = ["O", "L", "O", "O", "L", "L", "O"]
#   k = 1          the most late deliveries allowed in the run
#
# YOUR TASK
#   longest_stretch(deliveries, k) returns the length of the longest run of
#   deliveries next to each other with k or fewer "L"s in it.
#   No deliveries -> 0.
#
# EXAMPLE
#   Positions 0 to 3: O, L, O, O  -> one late, length 4   <- longest
#   Positions 2 to 4: O, O, L     -> one late, length 3
#   Positions 0 to 4 would have two late deliveries, which is too many.
#   longest_stretch(deliveries, 1)  ->  4
#
# HINT
#   Keep left = 0 (front of the run) and late = 0 (late deliveries in the
#   run). Loop right (end of the run) over every position: add
#   deliveries[right], then `while late > k:` remove deliveries[left] and
#   move left on. The run's length is right - left + 1.
#
# VIDEO (try the problem yourself for 20-30 minutes first, then watch)
#   Max Consecutive Ones III (Deepti Talesra)
#   https://www.youtube.com/watch?v=ZpsdDNbCgc0
#   This problem uses the same method as LeetCode 1004 Max Consecutive Ones III. The
#   video uses a different story and different names, so watch for the method, not the
#   details.
def longest_stretch(deliveries, k):
    pass
