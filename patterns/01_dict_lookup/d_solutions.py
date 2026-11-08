"""
PATTERN 01: DICT LOOKUP - SOLUTIONS
"""


# 1. WHICH ORDERS ARRIVED LATE?
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Lists vs Sets (for lookup efficiency) (BugBytes)
#   https://www.youtube.com/watch?v=xzDEEzH8XWk
def late_orders_slow(orders, deliveries):
    late = []
    for o in orders:
        for d in deliveries:
            if o["id"] == d["order_id"] and d["minutes"] > o["promised"]:
                late.append(o["id"])
    return late


def late_orders_fast(orders, deliveries):
    # Step 1: turn the delivery log into a dict (order id -> minutes it took)
    minutes = {}
    for d in deliveries:
        minutes[d["order_id"]] = d["minutes"]

    # Step 2: go through the orders once
    late = []
    for o in orders:
        order_id = o["id"]
        if order_id in minutes:                       # was it delivered?
            if minutes[order_id] > o["promised"]:     # did it take too long?
                late.append(order_id)
    return late
# Speed: one pass through each list. With 1,000 of each, about 2,000 steps
# instead of 1,000,000.


# 2. ORDERS NOBODY HAS PAID FOR
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Find the Difference of Two Arrays - Leetcode 2215 - Python (NeetCode)
#   https://www.youtube.com/watch?v=a4wqKR-znBE
#   Same idea as LeetCode 2215 Find the Difference of Two Arrays. The video uses a different story and
#   different names, so watch for the method, not the details.
def unpaid_orders(orders, payments):
    # Step 1: collect every order id that has a payment
    paid = set()
    for p in payments:
        paid.add(p["order_id"])

    # Step 2: keep the orders that are not in that set
    unpaid = []
    for o in orders:
        if o["id"] not in paid:
            unpaid.append(o["id"])
    return unpaid
# Speed: one pass through each list. A set answers "is this in here?"
# straight away, the same way a dict does.


# 3. TWO ORDERS THAT USE UP A VOUCHER
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Two Sum - Leetcode 1 - HashMap - Python (NeetCode)
#   https://www.youtube.com/watch?v=KLlXCFG5TnA
#   Same idea as LeetCode 1 Two Sum. The video uses a different story and
#   different names, so watch for the method, not the details.
def voucher_pair(totals, voucher):
    seen = {}                                # total -> position where we saw it
    for j in range(len(totals)):
        needed = voucher - totals[j]         # the other order must be this much
        if needed in seen:
            return (seen[needed], j)
        if totals[j] not in seen:            # keep the earliest position
            seen[totals[j]] = j
    return None
# Speed: one pass through the list. Checking every pair would be
# len(totals) x len(totals) steps.
# Note: we check the dict BEFORE storing the current total, so an order is
# never paired with itself (a 10 on its own doesn't make 20).
