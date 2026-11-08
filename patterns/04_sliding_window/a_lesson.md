# Pattern 04: Sliding window

**Watch first:** [Introduction to Sliding Window and 2 Pointers (C++/Java, idea is the same)](https://www.youtube.com/watch?v=9kdHxplyl5I) (take U forward). Every problem's video is listed in `b_videos.md`.


## What it does
A sliding window answers questions about groups of items that sit next to each other in a list, like the best three days in a row, the longest stretch of on-time deliveries, or the longest run of letters with no repeats. Instead of adding up every group from scratch, it works out the first group once and then slides along, adding the new item that comes in and taking away the one that drops out. The "window" is simply the group of items you're looking at right now.

Sometimes the window is always the same size, like "any 3 days in a row", which is what the worked example below uses. Other times it grows and shrinks: it gets longer until it breaks a rule, then gives up items from the front until the rule is met again, like "the longest stretch with at most 1 late delivery". That second kind is explained further down and used in problem 3.

## A quick example
As an example, here are the first two three-day stretches of a week's takings, `[120, 80, 200, 150, ...]`. The second total comes straight from the first one:

| Days | How you get the total |
|---|---|
| 0 to 2 | add them once: 120 + 80 + 200 = 400 |
| 1 to 3 | 400 − day 0 (120) + day 3 (150) = 430 |

## When to use it
Use a sliding window when the question is about a run of items next to each other and you want the best, longest or shortest one. Look out for:
- **"in a row"**, **"consecutive"**, **"a stretch of"**, **"any k days"**, **"longest run"**
- the **best / longest / shortest** group of items next to each other
- the urge to write a loop that adds up `k` items inside a loop over every starting position

---

## Worked example: The best three days in a row

### The problem
The shop owner is planning a three-day promotion for next year and wants to copy the timing of this year's best stretch. She has the takings for each day this week and wants to know which three days in a row brought in the most money.

There are only six days in this example, but the real report covers a whole year, so adding up every three-day stretch from scratch would mean a lot of repeated adding.

**Your task is to find the three consecutive days with the highest total takings, and say which day the stretch started on.**

### The data
```python
revenue = [120, 80, 200, 150, 90, 300]   # takings for day 0, day 1, ... day 5
k = 3                                    # how many days in a row
```
The answer should be `(3, 540)`: the stretch starting on day 3 (days 3, 4 and 5) took £540.

If `k` is 0 or less, or bigger than the number of days, return `None`. If two stretches tie, keep the earlier one.

### How you'd do it with a pen
Write out every three-day stretch:

| Starts on day | Days | Total |
|---|---|---|
| 0 | 120 + 80 + 200 | 400 |
| 1 | 80 + 200 + 150 | 430 |
| 2 | 200 + 150 + 90 | 440 |
| 3 | 150 + 90 + 300 | **540** |

Now look at how each total relates to the one before it. When you move from the stretch starting on day 0 to the one starting on day 1, day 0 (120) drops off the front and day 3 (150) joins at the end, while days 1 and 2 are in both stretches, so they don't need adding again.

That gives 400 − 120 + 150 = 430: one subtraction and one addition, however long the stretch is.

### The code
```python
def best_run(revenue, k):
    if k <= 0 or k > len(revenue):
        return None

    # Step 1: add up the first k days
    total = sum(revenue[:k])
    best_total = total
    best_start = 0

    # Step 2: move the stretch along one day at a time
    for new_day in range(k, len(revenue)):
        old_day = new_day - k                    # the day that drops off the front
        total = total + revenue[new_day] - revenue[old_day]
        start = old_day + 1                      # where the stretch starts now
        if total > best_total:                   # > not >=, so ties keep the earlier one
            best_total = total
            best_start = start

    return (best_start, best_total)
```

### Names used in the code
| Name | What it holds | Example |
|---|---|---|
| `revenue` | takings for each day, day 0 first | `[120, 80, 200, 150, 90, 300]` |
| `k` | how many days in a row | `3` |
| `total` | the total for the stretch we're looking at now | `400` |
| `best_total` | the highest total found so far | `540` |
| `best_start` | the day the best stretch starts on | `3` |
| `new_day` | the day joining at the end of the stretch | `3` |
| `old_day` | the day dropping off the front | `0` |
| `start` | the first day of the stretch we're looking at now | `1` |

### Watch it run
Step 1: `total = 120 + 80 + 200 = 400`, `best_total = 400`, `best_start = 0`.

| `new_day` | joins | `old_day` | drops off | `total` | `start` | Best so far |
|---|---|---|---|---|---|---|
| 3 | 150 | 0 | 120 | 400 + 150 − 120 = 430 | 1 | (1, 430) |
| 4 | 90 | 1 | 80 | 430 + 90 − 80 = 440 | 2 | (2, 440) |
| 5 | 300 | 2 | 200 | 440 + 300 − 200 = 540 | 3 | **(3, 540)** |

With a year of data and a 7-day stretch, adding every stretch from scratch takes about 365 × 7 additions, while the sliding version takes about 365 × 2.

### What to say in the interview
"Instead of adding up every stretch from scratch, I add up the first k days once. Then each time the stretch moves along a day, I add the new day and subtract the day that dropped off. That's one pass through the list."

---

## The second kind: a window that grows and shrinks
Problem 3 asks for the **longest** stretch of deliveries with **at most k late ones**. Because the length isn't fixed, the window works a little differently, repeating these steps for each delivery:

1. Add the next delivery to the end of the window, and if it's late, add 1 to `late`.
2. While the window has too many late deliveries, remove deliveries from the front, taking 1 off `late` whenever a removed one was late.
3. The window now follows the rule, so check whether it's the longest so far.

The window runs from position `left` to position `right`, so its length is `right - left + 1`.

```python
def longest_stretch(deliveries, k):
    left = 0
    late = 0
    best = 0
    for right in range(len(deliveries)):
        if deliveries[right] == "L":
            late += 1
        while late > k:                          # too many late: shrink from the front
            if deliveries[left] == "L":
                late -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
```

With `deliveries = ["O", "L", "O", "O", "L", "L", "O"]` (O = on time, L = late) and `k = 1`:

| `right` | Delivery added | `late` | Too many? Remove from the front | Window (`left` to `right`) | Length | `best` |
|---|---|---|---|---|---|---|
| 0 | O | 0 | no | 0 to 0 | 1 | 1 |
| 1 | L | 1 | no | 0 to 1 | 2 | 2 |
| 2 | O | 1 | no | 0 to 2 | 3 | 3 |
| 3 | O | 1 | no | 0 to 3 | 4 | **4** |
| 4 | L | 2 | yes: remove position 0 (O), then position 1 (L), `late` = 1 | 2 to 4 | 3 | 4 |
| 5 | L | 2 | yes: remove positions 2 (O), 3 (O), 4 (L), `late` = 1 | 5 to 5 | 1 | 4 |
| 6 | O | 1 | no | 5 to 6 | 2 | 4 |

The answer is **4**: positions 0 to 3 (O, L, O, O).

Every delivery is added once and removed at most once, so this is still a single pass through the list.

---

## The pattern, in general
```python
# Fixed size k
total = sum(items[:k])
for new in range(k, len(items)):
    total += items[new] - items[new - k]      # add the new one, remove the old one
    # check total

# Grows and shrinks
left = 0
for right in range(len(items)):
    # add items[right] to whatever you're tracking
    while the_window_breaks_the_rule:
        # remove items[left] from what you're tracking
        left += 1
    # the window from left to right is valid: check its length
```

## Common mistakes
1. **Off by one on the window's start.** After adding `new_day`, the stretch starts at `new_day - k + 1`, not `new_day - k`. Write the trace table out for the first step to check.
2. **Recalculating with `sum()` inside the loop.** `sum(revenue[start:start + k])` in the loop works, but it's the slow version.
3. **Using `if` instead of `while` when shrinking.** One removal might not be enough. Keep removing until the rule is met.
4. **Window length.** The length from `left` to `right` is `right - left + 1`. From position 2 to position 4 is 3 items: 2, 3 and 4.
5. **Forgetting the edge cases:** an empty list, `k` bigger than the list, `k` of 0.

## Python you'll need
| Code | What it does | Example |
|---|---|---|
| `sum(my_list)` | adds up a list | `sum([120, 80, 200])` gives `400` |
| `my_list[:k]` | the first k items | `[120, 80, 200, 150][:3]` gives `[120, 80, 200]` |
| `range(k, n)` | the numbers k, k+1, ... up to n−1 | `range(3, 6)` gives 3, 4, 5 |
| `max(a, b)` | the bigger of two numbers | `max(3, 4)` gives `4` |

## Now practise
Open `c_practice.py` in this folder:
- **Problem 1** is the worked example. Type it in without looking.
- **Problem 2** (how many three-day stretches hit a target) is a fixed-size window.
- **Problem 3** (the longest stretch with at most k late deliveries) is the window that grows and shrinks, explained just above.

Test your answers from the `pattern_course` folder:
```bash
python3 practice.py 4
```

## More practice
Once all 3 problems pass, work through `e_more_practice.md` in this folder: 5 to 7 free LeetCode problems that use the same pattern, easiest first.
