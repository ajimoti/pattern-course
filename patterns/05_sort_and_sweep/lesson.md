# Pattern 05: Sort, then walk through once

**Watch first:** [Merge Interval Algorithm In 4 Minutes](https://www.youtube.com/watch?v=hG9QDwiE28w) (Kantan Coding). Every problem's video is listed in `videos.md`.


## In one sentence
Put the items in order first, then go through them a single time, keeping a running count or a "current" value as you go.

## How to spot it
Look for questions about **times, ranges or things that overlap**:
- "How many are happening **at the same time**?"
- "**Merge** the overlapping shifts / bookings / slots"
- "Can one person do **all of them** without a clash?"
- The data is a list of `(start, end)` pairs.

When the items are in time order, each one only needs to be compared with what came just before it. That's why sorting first makes the rest easy.

---

## Worked example: How many ovens does the shop need?

### The problem
Your pizza shop is getting busier, and you need to figure out how many ovens are required to handle all the orders.

Each pizza has a scheduled time to go into the oven and a time when it finishes baking.

An oven can only bake one pizza at a time. However, as soon as a pizza comes out, another can go straight in.

You have a list showing the start and finish times for every pizza.

Your task is to calculate the minimum number of ovens the shop needs to bake every pizza at its scheduled time without making any order wait.

### The data
```python
bakes = [(0, 10), (5, 15), (10, 20), (12, 14)]
```
Each pizza is `(minute it goes in, minute it comes out)`. The answer is `3`.

### The slow idea first
The number of ovens you need is **the most pizzas baking at the same moment**.

A first idea: for each pizza's start time, count how many pizzas are in an oven at that minute, and keep the biggest count. That works, but for every pizza it checks every other pizza. With 1,000 pizzas that's 1,000 × 1,000 = 1,000,000 checks. This is called O(n²): the work grows with the number of items multiplied by itself.

It's fine to say this idea out loud in an interview, then improve it.

### How you'd do it with a pen
Write down every moment a pizza **goes in** (+1) or **comes out** (−1), in time order. Keep a running count of pizzas in the ovens, and note the highest it reaches.

| Minute | What happens | Change | Pizzas in ovens | Highest so far |
|---|---|---|---|---|
| 0 | pizza (0, 10) goes in | +1 | 1 | 1 |
| 5 | pizza (5, 15) goes in | +1 | 2 | 2 |
| 10 | pizza (0, 10) comes out | −1 | 1 | 2 |
| 10 | pizza (10, 20) goes in | +1 | 2 | 2 |
| 12 | pizza (12, 14) goes in | +1 | **3** | **3** |
| 14 | pizza (12, 14) comes out | −1 | 2 | 3 |
| 15 | pizza (5, 15) comes out | −1 | 1 | 3 |
| 20 | pizza (10, 20) comes out | −1 | 0 | 3 |

**Answer: 3.**

At minute 10, one pizza comes out and another goes in. The problem says the new one can go straight in, so "comes out" must be handled **before** "goes in" at the same minute.

### The code
```python
def min_ovens(bakes):
    # Step 1: every pizza going in (+1) and coming out (-1)
    timeline = []
    for start, finish in bakes:
        timeline.append((start, 1))
        timeline.append((finish, -1))

    # Step 2: sort by minute. At the same minute, -1 comes before 1,
    # so "comes out" is handled before "goes in".
    timeline = sorted(timeline)

    # Step 3: walk through once, keeping a running count
    in_oven = 0
    most_at_once = 0
    for _, change in timeline:
        in_oven += change
        most_at_once = max(most_at_once, in_oven)

    return most_at_once
```

### Names used in the code
| Name | What it holds | Example |
|---|---|---|
| `bakes` | every pizza as (start, finish) | `[(0, 10), (5, 15), ...]` |
| `timeline` | every (minute, +1 or −1) | `[(0, 1), (5, 1), (10, -1), ...]` |
| `in_oven` | pizzas baking right now | `2` |
| `most_at_once` | the highest `in_oven` has been | `3` |
| `_` | the minute; we don't need it in the loop, so it gets a throwaway name | `10` |

### Watch it run
After sorting, `timeline` is:
`[(0, 1), (5, 1), (10, -1), (10, 1), (12, 1), (14, -1), (15, -1), (20, -1)]`

| Entry | `change` | `in_oven` after | `most_at_once` after |
|---|---|---|---|
| (0, 1) | +1 | 1 | 1 |
| (5, 1) | +1 | 2 | 2 |
| (10, -1) | −1 | 1 | 2 |
| (10, 1) | +1 | 2 | 2 |
| (12, 1) | +1 | 3 | 3 |
| (14, -1) | −1 | 2 | 3 |
| (15, -1) | −1 | 1 | 3 |
| (20, -1) | −1 | 0 | 3 |

Returns **3**.

### What to say in the interview
"The number of ovens is the most pizzas baking at once. The simple way checks every pizza against every other, which is O(n²). Instead I turn each bake into two events, +1 going in and −1 coming out, sort them by time with 'out' before 'in' at the same minute, and keep a running count. The answer is the highest count. Sorting is the slowest step, so it's O(n log n)."

O(n log n) means a little more than the number of items, because of the sort. It's far quicker than O(n²) for big lists.

---

## The pattern, in general
```python
def sort_and_sweep(items):
    items = sorted(items)            # 1. put them in order
    state = starting_value           # 2. something to keep track of
    for item in items:               # 3. one walk through
        # compare item with state, then update state
        ...
    return answer
```

---

## Common mistakes
1. **Forgetting to sort.** The walk only works if the items are in order. Test data is often given out of order on purpose.
2. **Getting the "same minute" case wrong.** Decide what happens when one thing ends at minute 10 and another starts at minute 10, and check your code does that.
3. **Changing a list while looping over it.** Build a new list instead.
4. **Forgetting the empty case.** With no items, the answer is usually `0`, `[]` or `True`.

---

## Python you'll need
| Code | What it does | Example |
|---|---|---|
| `sorted(list)` | a new list in order; pairs are compared by the first value, then the second | `sorted([(10, 1), (10, -1)])` gives `[(10, -1), (10, 1)]` |
| `sorted(list, key=lambda x: x[0])` | sort pairs by the first value only | |
| `max(a, b)` | the bigger of two values | `max(2, 3)` gives `3` |
| `list[-1]` | the last item in a list | `[1, 2, 3][-1]` gives `3` |

---

## Now practise
Open `practice.py` in this folder:
1. **Problem 1** is the worked example above. Type it in without looking.
2. **Problem 2** (merge driver shifts) and **Problem 3** (can one driver do every delivery?) are new.

Test your answers:
```bash
python3 practice.py 5
```

## More practice
Once all 3 problems pass, work through `more_practice.md` in this folder: 5 to 7 free LeetCode problems that use the same pattern, easiest first.
