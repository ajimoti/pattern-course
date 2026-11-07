"""
PATTERN 06: STACK - SOLUTIONS
"""


# 1. BALANCED BRACKETS
# Stack of opening brackets. A closing bracket must match the most recent one.
# Speed: O(n), one pass over the note.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Valid Parentheses - Stack - Leetcode 20 - Python (NeetCode)
#   https://www.youtube.com/watch?v=WTzjTskDFMg
#   Same idea as LeetCode 20 Valid Parentheses. The video uses a different story and
#   different names, so watch for the method, not the details.
def is_balanced(note):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in note:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0


# 2. UNDO IN THE ORDER EDITOR
# The order itself is the stack: add = append, undo = pop the most recent.
# Speed: O(n), one pass over the actions.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Backspace String Compare - Leetcode 844 - Python (NeetCodeIO)
#   https://www.youtube.com/watch?v=k2qrymM_DOo
#   Same idea as LeetCode 844 Backspace String Compare. The video uses a different story and
#   different names, so watch for the method, not the details.
def final_order(actions):
    order = []
    for action in actions:
        if action == "undo":
            if order:                       # undo on an empty order does nothing
                order.pop()
        else:
            _, pizza = action.split(" ", 1)  # "add margherita" -> "add", "margherita"
            order.append(pizza)
    return order


# 3. DAYS UNTIL A BUSIER DAY
# `waiting` is a stack of day numbers that haven't found a busier day yet.
# Their order counts go down from bottom to top, so when today is busier than
# the top day, it may also be busier than the next one down - keep popping.
# Each day is pushed once and popped at most once, so it's O(n).
#
# Watch it run on orders = [30, 25, 40, 35, 50]:
#
#   today  count  what happens                                   waiting after  answer after
#   0      30     nothing waiting; day 0 starts waiting          [0]            [0,0,0,0,0]
#   1      25     25 > 30 (day 0)? no; day 1 starts waiting      [0, 1]         [0,0,0,0,0]
#   2      40     40 > 25 (day 1)? yes -> answer[1] = 2-1 = 1
#                 40 > 30 (day 0)? yes -> answer[0] = 2-0 = 2
#                 day 2 starts waiting                           [2]            [2,1,0,0,0]
#   3      35     35 > 40 (day 2)? no; day 3 starts waiting      [2, 3]         [2,1,0,0,0]
#   4      50     50 > 35 (day 3)? yes -> answer[3] = 4-3 = 1
#                 50 > 40 (day 2)? yes -> answer[2] = 4-2 = 2
#                 day 4 starts waiting                           [4]            [2,1,2,1,0]
#   end           day 4 never found a busier day, keeps 0
#
# enumerate(orders) gives (0, 30), (1, 25), (2, 40)... : the day number and its count.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Daily Temperatures - Monotonic Stack - Leetcode 739 - Python (NeetCode)
#   https://www.youtube.com/watch?v=cTBiBSnjO3c
#   Same idea as LeetCode 739 Daily Temperatures. The video uses a different story and
#   different names, so watch for the method, not the details.
def days_until_busier(orders):
    answer = [0] * len(orders)
    waiting = []                                  # day numbers
    for today, count in enumerate(orders):
        while waiting and count > orders[waiting[-1]]:
            day = waiting.pop()
            answer[day] = today - day
        waiting.append(today)
    return answer                                 # days still waiting keep 0
