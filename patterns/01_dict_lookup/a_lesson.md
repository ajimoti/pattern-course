# Pattern 01: Dict lookup

**Watch first:** [Python Tutorial for Beginners 5: Dictionaries](https://www.youtube.com/watch?v=daefaLgNkw0) (Corey Schafer, 10 min), then [Lists vs Sets (for lookup efficiency)](https://www.youtube.com/watch?v=xzDEEzH8XWk) (BugBytes, 7 min). Every problem's video is listed in `b_videos.md`.


## What it does
A dict lookup speeds up code that keeps searching through the same list to find matching items. It works for anything you match up by a shared value, like orders and their payments, students and their grades, or products and their prices, because you can store one side in a dict once and then find any item in it straight away instead of searching.

Without a dict, every search starts at the top of the list and checks item after item until it finds a match, so searching a long list many times gets very slow. With a dict, you go through that list once to fill the dict, and after that each lookup jumps straight to the item you asked for.

## A quick example
As an example, say you have 3 orders and a list of payments, and you want to know which orders were paid. You put the payments into a dict once, then look up each order in it:

| Order | Look it up in the payments dict | Paid? |
|---|---|---|
| 101 | found | Yes |
| 102 | not found | No |
| 103 | found | Yes |

Each order is one lookup, so you never read through the payments list again.

## When to use it
Reach for a dict whenever your code would otherwise search one list over and over to match things up. Look out for:
- a loop inside another loop, where the inner loop is only there to **find a match** (same id, same name, same value)
- "for each order, find its delivery / payment / customer"
- "make this slow code faster"
- "is there another item that ...?", for example another order that makes up the rest of a total

---

## Worked example: Which orders arrived late?

### The problem
Your pizza shop promises to deliver every order within 30 minutes. At the end of each night, you need to find out which orders failed to meet that promise.

To do this, you have two lists: one containing every order placed that day, and another containing the drivers' delivery logs, including how long each delivery took.

Not every order gets delivered. For example, order 3 was cancelled, so it doesn't appear in the delivery log.

A colleague has already written some code to identify orders that took longer than promised. The code works correctly, but there's a problem: for every order, it searches through the entire delivery log to find a match.

With just five orders, this isn't a big deal. But on a busy night with 1,000 orders, the code could end up making 1,000,000 comparisons.

**Your task is to optimise the existing code so it produces the same result without repeatedly searching through the delivery log.**

### The data
```python
orders = [
    {"id": 1, "promised": 30},
    {"id": 2, "promised": 30},
    {"id": 3, "promised": 30},
    {"id": 4, "promised": 30},
    {"id": 5, "promised": 30},
]

deliveries = [
    {"order_id": 1, "minutes": 25},
    {"order_id": 2, "minutes": 40},
    {"order_id": 4, "minutes": 31},
    {"order_id": 5, "minutes": 30},
]
```
The answer should be `[2, 4]`.

The slow code you are given:
```python
def late_orders_slow(orders, deliveries):
    late = []
    for o in orders:
        for d in deliveries:
            if o["id"] == d["order_id"] and d["minutes"] > o["promised"]:
                late.append(o["id"])
    return late
```
For order 1 it reads every line of the delivery log, then for order 2 it reads the whole log again, and it keeps doing that for every order, so the number of checks is orders times deliveries.

| Orders | Deliveries | Checks the slow code makes |
|---|---|---|
| 5 | 4 | 5 × 4 = 20 |
| 1,000 | 1,000 | 1,000 × 1,000 = 1,000,000 |

### How you'd do it with a pen
1. Read the delivery log once, and write down each order number with its minutes: order 1 took 25, order 2 took 40, order 4 took 31, order 5 took 30.
2. Go down the orders list once. For each order, look up its minutes in what you wrote down and compare them with the promise.

| Order | Minutes it took | Promised | Late? |
|---|---|---|---|
| 1 | 25 | 30 | No |
| 2 | 40 | 30 | **Yes** |
| 3 | not delivered | 30 | Skip |
| 4 | 31 | 30 | **Yes** |
| 5 | 30 | 30 | No (exactly on time is not late) |

### The code
```python
def late_orders_fast(orders, deliveries):
    # Step 1: turn the delivery log into a dict (order number -> minutes)
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
```

### Names used in the code
| Name | What it holds | Example |
|---|---|---|
| `orders` | every order, with the minutes it was promised in | `{"id": 2, "promised": 30}` |
| `deliveries` | every delivery, with the minutes it took | `{"order_id": 2, "minutes": 40}` |
| `minutes` | dict built from the delivery log: order number → minutes it took | `{1: 25, 2: 40, 4: 31, 5: 30}` |
| `d` | one line of the delivery log | `{"order_id": 1, "minutes": 25}` |
| `o` | one order | `{"id": 1, "promised": 30}` |
| `order_id` | the number of the order being checked | `2` |
| `late` | the order numbers that were late | `[2, 4]` |

### Watch it run
After step 1, `minutes = {1: 25, 2: 40, 4: 31, 5: 30}`.

| Order | `order_id in minutes`? | `minutes[order_id]` | Promised | Late? | `late` after |
|---|---|---|---|---|---|
| 1 | Yes | 25 | 30 | No | `[]` |
| 2 | Yes | 40 | 30 | Yes | `[2]` |
| 3 | No | | 30 | Skip | `[2]` |
| 4 | Yes | 31 | 30 | Yes | `[2, 4]` |
| 5 | Yes | 30 | 30 | No | `[2, 4]` |

The new code reads the delivery log once (4 steps) and the orders once (5 steps): 9 steps instead of 20. With 1,000 of each, it is 2,000 steps instead of 1,000,000.

### What to say in the interview
"The original loops through every delivery for every order, so the work grows as orders times deliveries. I'll put the deliveries into a dict first, so finding an order's delivery is a single lookup, and I only go through each list once."

---

## The pattern, in general
```python
# 1. Go through the list you keep searching, ONCE, and store it in a dict.
lookup = {}
for item in list_you_search:
    lookup[item["key"]] = item["value"]

# 2. Go through the other list once, and use the dict instead of searching.
for thing in other_list:
    if thing["key"] in lookup:            # is there a match?
        value = lookup[thing["key"]]      # get it straight away
        ...
```
This is fast because a list has to be checked item by item to find something, while a dict goes straight to the key you ask for.

## Common mistakes
1. **Looking up a key that isn't there.** `minutes[3]` crashes with `KeyError` because order 3 was never delivered. Check `if order_id in minutes` first, or use `minutes.get(order_id)` which gives `None` instead of crashing.
2. **Comparing `None` with a number.** `minutes.get(3) > 30` crashes, because `.get()` gave `None`. Skip missing keys before comparing.
3. **Writing a fixed number instead of reading it from the data.** Use `o["promised"]`, not `30`. The test data may use different promises.
4. **Building the dict inside the loop.** If you build the dict inside the `for o in orders` loop, you are back to the slow version. Build it once, before the loop.

## Python you'll need
| Code | What it does | Example |
|---|---|---|
| `d = {}` | an empty dict | |
| `d[key] = value` | store a value under a key | `minutes[1] = 25` |
| `key in d` | is this key in the dict? | `3 in minutes` gives `False` |
| `d[key]` | get the value (crashes if the key is missing) | `minutes[2]` gives `40` |
| `d.get(key)` | get the value, or `None` if the key is missing | `minutes.get(3)` gives `None` |
| `s = set()` | an empty set: like a dict with keys but no values | |
| `s.add(x)` | put `x` in the set | `paid.add(103)` |
| `x in s` | is `x` in the set? (instant, like a dict) | `102 in paid` gives `False` |

## Now practise
Open `c_practice.py` in this folder:
- **Problem 1** is the example above. Type it in without looking.
- **Problem 2** (orders nobody has paid for) and **Problem 3** (two orders that use up a voucher) use the same idea.

Test your answers from the `pattern_course` folder:
```bash
python3 practice.py 1
```

## More practice
Once all 3 problems pass, work through `e_more_practice.md` in this folder: 5 to 7 free LeetCode problems that use the same pattern, easiest first.
