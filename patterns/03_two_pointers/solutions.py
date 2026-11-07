"""
PATTERN 03: TWO POINTERS - SOLUTIONS
"""


# 1. TWO PIZZAS THAT USE UP A BUDGET EXACTLY
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Two Sum II - Leetcode 167 - Python (NeetCode)
#   https://www.youtube.com/watch?v=cQ1Oz4ckceM
#   Same idea as LeetCode 167 Two Sum II. The video uses a different story and
#   different names, so watch for the method, not the details.
def two_prices(prices, budget):
    left = 0                      # cheapest price still in play
    right = len(prices) - 1       # most expensive price still in play

    while left < right:           # stop when they meet
        total = prices[left] + prices[right]
        if total == budget:
            return (prices[left], prices[right])
        elif total < budget:
            left += 1             # too small: bigger price on the left
        else:
            right -= 1            # too big: smaller price on the right

    return None
# Speed: one pass through the list. Checking every pair would be about
# (list length x list length) / 2 checks.


# 2. AN ORDER CODE THAT READS THE SAME BACKWARDS
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Valid Palindrome - Leetcode 125 - Python (NeetCode)
#   https://www.youtube.com/watch?v=jJXJ16kPFWg
#   Same idea as LeetCode 125 Valid Palindrome. The video uses a different story and
#   different names, so watch for the method, not the details.
def is_mirror_code(code):
    code = code.lower()
    left = 0
    right = len(code) - 1

    while left < right:
        if code[left] != code[right]:
            return False          # one mismatch is enough
        left += 1
        right -= 1

    return True
# Speed: one pass, and it stops at the first mismatch.
# (The one-line version, code.lower() == code.lower()[::-1], also works, but
#  interviewers often ask for the two-pointer version.)


# 3. MERGING TWO SORTED LISTS OF ORDER TIMES
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Merge Sorted Array - Leetcode 88 - Python (NeetCode)
#   https://www.youtube.com/watch?v=P1Ic85RarKY
#   Same idea as LeetCode 88 Merge Sorted Array. The video uses a different story and
#   different names, so watch for the method, not the details.
def merge_orders(app, phone):
    merged = []
    i = 0                         # next unused time in app
    j = 0                         # next unused time in phone

    while i < len(app) and j < len(phone):
        if app[i] <= phone[j]:
            merged.append(app[i])
            i += 1
        else:
            merged.append(phone[j])
            j += 1

    # one list has run out; add what's left of the other
    merged.extend(app[i:])
    merged.extend(phone[j:])
    return merged
# Speed: every time is looked at once, so it grows in step with the total
# number of times. Sorting the joined list would do more work.
