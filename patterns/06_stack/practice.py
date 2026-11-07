"""
PATTERN 06: STACK
Read lesson.md first. Test your answers with:  python3 practice.py 6
"""


# =============================================================================
# 1. ARE THE BRACKETS IN AN ORDER NOTE BALANCED?
# =============================================================================
# THE PROBLEM
#   Customers can add a note to their order, and the kitchen's printer uses
#   brackets to format it: ( ), [ ] and { }. If a note has a bracket that's
#   never closed, or closed with the wrong type, the printer jams.
#
#   Before a note is sent to the kitchen, you want to check that every bracket
#   is closed, by the right type, in the right order. Any other characters in
#   the note don't matter.
#
# THE DATA
#   note = "(extra cheese [no onions]) {ring bell}"
#
# YOUR TASK
#   is_balanced(note) returns True or False.
#   A note with no brackets at all is balanced (True).
#
# EXAMPLE
#   "(extra cheese [no onions]) {ring bell}"  ->  True
#   "(extra cheese"                           ->  False  (never closed)
#   "no onions)"                              ->  False  (nothing to close)
#   "[well done)"                             ->  False  (wrong type)
#   "([)]"                                    ->  False  ([ must close before ( )
#
# HINT
#   Keep a list of opening brackets. A closing bracket must match the LAST one.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Valid Parentheses - Stack - Leetcode 20 - Python (NeetCode)
#   https://www.youtube.com/watch?v=WTzjTskDFMg
#   Same idea as LeetCode 20 Valid Parentheses. The video uses a different story and
#   different names, so watch for the method, not the details.
def is_balanced(note):
    pass


# =============================================================================
# 2. UNDO IN THE ORDER EDITOR
# =============================================================================
# THE PROBLEM
#   The app lets customers build an order one pizza at a time. There's also an
#   undo button, which takes away the most recent pizza they added. Pressing
#   undo again takes away the one before that, and so on. Pressing undo when
#   the order is empty does nothing.
#
#   You get a list of everything the customer tapped, in order.
#
#   Your task is to work out what's in the order at the end.
#
# THE DATA
#   actions = ["add margherita", "add pepperoni", "add hawaiian",
#              "undo", "add veggie", "undo", "undo"]
#   Each action is either "add <pizza name>" or "undo".
#
# YOUR TASK
#   final_order(actions) returns the list of pizza names left, in the order
#   they were added.
#
# EXAMPLE
#   add margherita  -> [margherita]
#   add pepperoni   -> [margherita, pepperoni]
#   add hawaiian    -> [margherita, pepperoni, hawaiian]
#   undo            -> [margherita, pepperoni]
#   add veggie      -> [margherita, pepperoni, veggie]
#   undo            -> [margherita, pepperoni]
#   undo            -> [margherita]
#
#   final_order(actions)  ->  ["margherita"]
#
# HINT
#   "add margherita".split(" ", 1) gives ["add", "margherita"].
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Backspace String Compare - Leetcode 844 - Python (NeetCodeIO)
#   https://www.youtube.com/watch?v=k2qrymM_DOo
#   Same idea as LeetCode 844 Backspace String Compare. The video uses a different story and
#   different names, so watch for the method, not the details.
def final_order(actions):
    pass


# =============================================================================
# 3. HOW MANY DAYS UNTIL A BUSIER DAY?
# =============================================================================
# THE PROBLEM
#   You've got the number of orders the shop took each day for the last week.
#   For staff planning, the manager wants to know, for each day, how many days
#   she'd have to wait until a day with MORE orders than that one.
#
#   If there's no busier day after it in the list, the answer for that day
#   is 0.
#
# THE DATA
#   orders = [30, 25, 40, 35, 50]
#   orders[0] is day 0, orders[1] is day 1, and so on.
#
# YOUR TASK
#   days_until_busier(orders) returns a list the same length as orders.
#
# EXAMPLE
#   Day 0 (30): the next day with more than 30 is day 2 (40)  -> 2 days
#   Day 1 (25): day 2 (40) is busier                          -> 1 day
#   Day 2 (40): day 4 (50) is busier                          -> 2 days
#   Day 3 (35): day 4 (50) is busier                          -> 1 day
#   Day 4 (50): nothing after it is busier                    -> 0
#
#   days_until_busier(orders)  ->  [2, 1, 2, 1, 0]
#
# HINT
#   The slow way checks every later day for every day: O(n squared).
#   The fast way keeps a stack of day numbers still waiting for a busier day.
#   When today is busier than the day on top of the stack, that day's wait
#   is over: pop it and work out its answer.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Daily Temperatures - Monotonic Stack - Leetcode 739 - Python (NeetCode)
#   https://www.youtube.com/watch?v=cTBiBSnjO3c
#   Same idea as LeetCode 739 Daily Temperatures. The video uses a different story and
#   different names, so watch for the method, not the details.
def days_until_busier(orders):
    pass
