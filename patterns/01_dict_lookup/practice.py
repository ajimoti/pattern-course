"""
PATTERN 01: DICT LOOKUP - PRACTICE
Read lesson.md first. Write your code where it says `pass`.
Test from the pattern_course folder:   python3 practice.py 1
"""


# =============================================================================
# 1. WHICH ORDERS ARRIVED LATE?
# =============================================================================
# THE PROBLEM
#   Your pizza shop promises to deliver every order within 30 minutes. At the
#   end of each night, you need to find out which orders failed to meet that
#   promise.
#
#   You have two lists: one containing every order placed that day, and
#   another containing the drivers' delivery logs, including how long each
#   delivery took. Not every order gets delivered. Order 3 was cancelled, so it
#   doesn't appear in the delivery log.
#
#   A colleague has already written code that works (late_orders_slow, below),
#   but for every order it searches through the entire delivery log to find a
#   match. On a busy night with 1,000 orders, that's 1,000,000 comparisons.
#   Rewrite it so it gives the same result without searching the log again and
#   again.
#
# THE DATA
#   orders = [{"id": 1, "promised": 30}, {"id": 2, "promised": 30},
#             {"id": 3, "promised": 30}, {"id": 4, "promised": 30},
#             {"id": 5, "promised": 30}]
#   deliveries = [{"order_id": 1, "minutes": 25}, {"order_id": 2, "minutes": 40},
#                 {"order_id": 4, "minutes": 31}, {"order_id": 5, "minutes": 30}]
#
# YOUR TASK
#   late_orders_fast(orders, deliveries) returns a list of the order ids that
#   took longer than promised, in the same order as the orders list.
#   Orders that are not in the delivery log are skipped.
#   The tests use 20,000 orders, so it has to be fast.
#
# EXAMPLE
#   Order 1 took 25, promised 30  -> on time
#   Order 2 took 40, promised 30  -> late
#   Order 3 not in the log        -> skip
#   Order 4 took 31, promised 30  -> late
#   Order 5 took 30, promised 30  -> on time (exactly 30 is not late)
#   late_orders_fast(orders, deliveries)  ->  [2, 4]
#
# HINT
#   Put the delivery log into a dict first: {order id: minutes}.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Hash Tables and Hash Functions (Computer Science Lessons)
#   https://www.youtube.com/watch?v=KyUTuwz_b7Q
def late_orders_slow(orders, deliveries):
    late = []
    for o in orders:
        for d in deliveries:
            if o["id"] == d["order_id"] and d["minutes"] > o["promised"]:
                late.append(o["id"])
    return late


def late_orders_fast(orders, deliveries):
    pass


# =============================================================================
# 2. ORDERS NOBODY HAS PAID FOR
# =============================================================================
# THE PROBLEM
#   Every evening the shop matches its orders against the payments that came
#   in from the card machine. Most orders have a payment, but now and then one
#   slips through: a customer walks off, or the card machine drops a payment.
#
#   The manager wants a list of every order that has no payment at all, so
#   someone can follow it up the next morning. There are thousands of orders
#   and thousands of payments, so searching the payments list for every single
#   order would be far too slow.
#
# THE DATA
#   orders = [{"id": 101, "total": 18.50},
#             {"id": 102, "total": 12.00},
#             {"id": 103, "total": 25.00},
#             {"id": 104, "total": 9.50}]
#   payments = [{"order_id": 103, "amount": 25.00},
#               {"order_id": 101, "amount": 18.50}]
#   Payments are in the order they arrived, not the order of the orders list.
#
# YOUR TASK
#   unpaid_orders(orders, payments) returns a list of the ids of orders that
#   have no payment, in the same order as the orders list.
#   If every order is paid, return [].
#
# EXAMPLE
#   Order 101 -> there is a payment for 101  -> paid
#   Order 102 -> no payment for 102          -> unpaid
#   Order 103 -> there is a payment for 103  -> paid
#   Order 104 -> no payment for 104          -> unpaid
#   unpaid_orders(orders, payments)  ->  [102, 104]
#
# HINT
#   You only need to know WHICH orders were paid, not the amounts. A set of
#   paid order ids works, and so does a dict.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Find the Difference of Two Arrays - Leetcode 2215 - Python (NeetCode)
#   https://www.youtube.com/watch?v=a4wqKR-znBE
#   Same idea as LeetCode 2215 Find the Difference of Two Arrays. The video uses a different story and
#   different names, so watch for the method, not the details.
def unpaid_orders(orders, payments):
    pass


# =============================================================================
# 3. TWO ORDERS THAT USE UP A VOUCHER
# =============================================================================
# THE PROBLEM
#   A regular customer has a £20 voucher that can be spread across exactly two
#   of their past orders, but only if the two order totals add up to exactly
#   £20. Anything else and the voucher can't be used.
#
#   You have the customer's order totals in the order they were placed. Find
#   the first two orders that add up to the voucher amount. "First" means: as
#   you go through the list from the start, stop at the earliest order that
#   completes a pair with an order before it.
#
#   Checking every order against every other order works, but the customer has
#   a long history, so do it in one pass through the list.
#
# THE DATA
#   totals = [12, 7, 15, 3, 13]     (whole pounds, in the order placed)
#   voucher = 20
#
# YOUR TASK
#   voucher_pair(totals, voucher) returns (i, j): the positions of the two
#   orders in the list, with i < j. If no two orders add up to the voucher,
#   return None. An order can't be paired with itself.
#
# EXAMPLE
#   Position 0: total 12. Needs 8 to make 20. No 8 seen yet. Remember 12 at 0.
#   Position 1: total 7.  Needs 13. No 13 seen yet.          Remember 7 at 1.
#   Position 2: total 15. Needs 5.  No 5 seen yet.           Remember 15 at 2.
#   Position 3: total 3.  Needs 17. No 17 seen yet.          Remember 3 at 3.
#   Position 4: total 13. Needs 7.  7 was seen at position 1. Stop.
#   voucher_pair(totals, 20)  ->  (1, 4)
#
# HINT
#   Keep a dict of the totals you've already seen: {total: position}.
#   For each order, work out the amount it needs (voucher - total) and look
#   that up in the dict.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Two Sum - Leetcode 1 - HashMap - Python (NeetCode)
#   https://www.youtube.com/watch?v=KLlXCFG5TnA
#   Same idea as LeetCode 1 Two Sum. The video uses a different story and
#   different names, so watch for the method, not the details.
def voucher_pair(totals, voucher):
    pass
