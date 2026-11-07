"""
PATTERN 02: COUNTING WITH A DICT - SOLUTIONS
"""


# 1. WHAT'S POPULAR RIGHT NOW?
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Top K Frequent Elements - Bucket Sort - Leetcode 347 - Python (NeetCode)
#   https://www.youtube.com/watch?v=YPTqKIgVk-k
#   Same idea as LeetCode 347 Top K Frequent Elements. The video uses a different story and
#   different names, so watch for the method, not the details.
def trending(events, now, k):
    # Step 1: work out when "an hour ago" was
    one_hour_ago = now - 60

    # Step 2: count each pizza ordered after that
    counts = {}
    for minute, pizza in events:
        if minute > one_hour_ago:
            counts[pizza] = counts.get(pizza, 0) + 1

    # Step 3: sort by name first, then by count (biggest first)
    def how_many(p):
        return counts[p]

    alphabetical = sorted(counts)
    ranked = sorted(alphabetical, key=how_many, reverse=True)

    # Step 4: keep the top k
    return ranked[:k]
# Speed: one pass through the orders, then a sort of the different pizza
# names (a small number).


# 2. THE FIRST CUSTOMER WHO ONLY ORDERED ONCE
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Leetcode 387 - First Unique Character in a String - Python Solution (Data Engineering Studies)
#   https://www.youtube.com/watch?v=jKI5nClXQDM
#   Same idea as LeetCode 387 First Unique Character in a String. The video uses a different story and
#   different names, so watch for the method, not the details.
def first_one_time_customer(orders):
    # Pass 1: count every customer
    counts = {}
    for name in orders:
        counts[name] = counts.get(name, 0) + 1

    # Pass 2: go through in the original order, return the first with count 1
    for name in orders:
        if counts[name] == 1:
            return name
    return None
# Speed: two passes through the list. Counting each name by scanning the
# whole list again would be list length x list length.


# 3. ORDERS WITH THE SAME TOPPINGS
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Group Anagrams - Categorize Strings by Count - Leetcode 49 (NeetCode)
#   https://www.youtube.com/watch?v=vzdNOK2oB2E
#   Same idea as LeetCode 49 Group Anagrams. The video uses a different story and
#   different names, so watch for the method, not the details.
def group_same_toppings(orders):
    groups = {}                                  # toppings (A to Z) -> order ids
    for order_id, toppings in orders:
        key = tuple(sorted(toppings))            # same toppings -> same key
        if key not in groups:
            groups[key] = []
        groups[key].append(order_id)
    return list(groups.values())
# Speed: one pass through the orders (plus sorting each order's few toppings).
# A dict remembers the order keys were added, so the groups come out in the
# order their first order appeared.
