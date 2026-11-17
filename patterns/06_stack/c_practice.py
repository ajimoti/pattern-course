"""
PATTERN 06: STACK - PRACTICE
Read a_lesson.md first. Write your code where it says `pass`.
Test from the pattern_course folder:   python3 practice.py 6
"""


# =============================================================================
# 1. ARE THE BRACKETS IN AN ORDER NOTE BALANCED?
# =============================================================================
# THE PROBLEM
#   You run the ordering app for a pizza shop. Customers can add a note to
#   their order, and a printer in the kitchen uses brackets to format it:
#   ( ), [ ] and { }. If a note has a bracket that's never closed, or closed
#   with the wrong type, the printer jams.
#
#   Before a note is sent to the kitchen, you want to check that every bracket
#   is closed, by the right type, in the right order. Any other characters in
#   the note don't matter.
#
# THE DATA
#   note = "(extra cheese [no onions]) {ring bell}"
#
# YOUR TASK
#   is_balanced(note) returns True if every bracket in note is closed by the
#   right type in the right order, and False otherwise.
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
#   Keep a list of the opening brackets you've seen. A closing bracket must
#   match the LAST opening bracket in that list.
#
# VIDEO (try the problem yourself for 20-30 minutes first, then watch)
#   Valid Parentheses - Stack - Leetcode 20 - Python (NeetCode)
#   https://www.youtube.com/watch?v=WTzjTskDFMg
#   This problem uses the same method as LeetCode 20 Valid Parentheses. The video uses a
#   different story and different names, so watch for the method, not the details.
def is_balanced(note):
    pass


# =============================================================================
# 2. UNDO IN THE ORDER EDITOR
# =============================================================================
# THE PROBLEM
#   Your pizza shop's app lets customers build an order one pizza at a time.
#   There's also an undo button, which takes away the most recent pizza they
#   added. Pressing undo again takes away the one before that, and so on.
#   Pressing undo when the order is empty does nothing.
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
#   final_order(actions) returns a list of the pizza names still in the
#   customer's order at the end, in the order they were added.
#   If nothing is left, it returns [].
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
# VIDEO (try the problem yourself for 20-30 minutes first, then watch)
#   Backspace String Compare - Leetcode 844 - Python (NeetCodeIO)
#   https://www.youtube.com/watch?v=k2qrymM_DOo
#   This problem uses the same method as LeetCode 844 Backspace String Compare. The
#   video uses a different story and different names, so watch for the method, not the
#   details.
def final_order(actions):
    pass


# =============================================================================
# 3. HOW MANY DAYS UNTIL A BUSIER DAY?
# =============================================================================
# THE PROBLEM
#   You run a pizza shop, and you have the number of orders it took each day
#   for the last week. For staff planning, your manager wants to know, for
#   each day, how many days she'd have to wait until a day with MORE orders
#   than that one.
#
#   If no later day is busier, the answer for that day is 0.
#
# THE DATA
#   orders = [30, 25, 40, 35, 50]
#   orders[0] is day 0, orders[1] is day 1, and so on.
#
# YOUR TASK
#   days_until_busier(orders) returns a list the same length as orders.
#   Each entry is how many days that day waits for a busier day, or 0 if no
#   later day is busier.
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
#   The slow way checks every later day for every day: O(n squared), where n
#   is the number of days.
#   The fast way keeps a stack (a list you only add to and take from at the
#   end) of day numbers still waiting for a busier day. As you go through the
#   days, when the current day is busier than the day on top of the stack (its
#   last item), that day's wait is over: pop it (remove it from the end) and
#   work out its answer.
#
# VIDEO (try the problem yourself for 20-30 minutes first, then watch)
#   Daily Temperatures - Monotonic Stack - Leetcode 739 - Python (NeetCode)
#   https://www.youtube.com/watch?v=cTBiBSnjO3c
#   This problem uses the same method as LeetCode 739 Daily Temperatures. The video uses
#   a different story and different names, so watch for the method, not the details.
def days_until_busier(orders):
    pass
