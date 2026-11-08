# Pattern 07: Binary search

**Watch first:** [Binary search in 4 minutes](https://www.youtube.com/watch?v=fDKIpRe8GW4) (Michael Sambol). Every problem's video is listed in `b_videos.md`.


## What it does
Binary search finds something in a sorted list much faster than reading the list from the start. It looks at the middle item first, and because the list is in order, that one check tells it which half the answer must be in, so it throws the other half away and repeats on what's left until it finds the item or runs out of list.

It works on anything that's sorted, like order numbers, dates, prices or words in a dictionary, and it can also find the smallest value that makes something work, as long as you can check any single value easily. Because every check halves what's left, a list of a million items needs only about 20 checks. This is called O(log n), which means the work grows very slowly as the list gets bigger.

## A quick example
For example, finding 60 in this sorted list of 15 numbers takes four looks instead of eleven:

`[3, 8, 12, 19, 25, 31, 36, 42, 47, 55, 60, 68, 73, 81, 90]`

| Look | Positions still possible | Middle item | Compared with 60 |
|---|---|---|---|
| 1 | 0 to 14 | 42 (position 7) | smaller, so the answer is to the right |
| 2 | 8 to 14 | 68 (position 11) | bigger, so the answer is to the left |
| 3 | 8 to 10 | 55 (position 9) | smaller, so the answer is to the right |
| 4 | 10 to 10 | 60 (position 10) | found it |

## When to use it
Use binary search when the data is sorted, or when you're hunting for a number and can easily check whether any single guess works, for example:
- the list is **sorted** and you need to find something in it
- "find the **first** one that is at least / after ..."
- "what's the **smallest** (or largest) value that still works?"
- the list is huge and going through every item would be too slow

---

## Worked example: Find an order in the sorted order list

### The problem
Your shop keeps every order number from today in a list, sorted from smallest to biggest. A customer rings up about their order, and you need to find where it sits in the list so you can pull up its details.

On a busy day the list can have hundreds of thousands of orders, so reading through it from the start is too slow while the customer waits on the phone.

Your task is to find the position of an order number in the list, or report that it isn't there.

### The data
```python
order_ids = [101, 104, 108, 115, 120, 133, 140]
#  position:  0    1    2    3    4    5    6
target = 120
```
The answer is `4`, because `order_ids[4]` is `120`. If the number isn't in the list, return `-1`.

### How you'd do it with a pen
Keep two markers, `low` and `high`, for the part of the list the order could still be in. At the start, that's the whole list: positions 0 to 6.

Look at the item in the middle:
- **It's the target:** done.
- **It's smaller than the target:** the target must be to the right, so move `low` past the middle.
- **It's bigger than the target:** the target must be to the left, so move `high` before the middle.

Looking for **120**:

| Step | `low` | `high` | Middle position | Value there | Compare with 120 | What you do |
|---|---|---|---|---|---|---|
| 1 | 0 | 6 | (0 + 6) // 2 = 3 | 115 | smaller | `low` = 4 |
| 2 | 4 | 6 | (4 + 6) // 2 = 5 | 133 | bigger | `high` = 4 |
| 3 | 4 | 4 | (4 + 4) // 2 = 4 | 120 | **equal** | **return 4** |

Looking for **110**, which isn't in the list:

| Step | `low` | `high` | Middle position | Value there | Compare with 110 | What you do |
|---|---|---|---|---|---|---|
| 1 | 0 | 6 | 3 | 115 | bigger | `high` = 2 |
| 2 | 0 | 2 | 1 | 104 | smaller | `low` = 2 |
| 3 | 2 | 2 | 2 | 108 | smaller | `low` = 3 |
| 4 | 3 | 2 | | | `low` is past `high`, nothing left | **return -1** |

### The code
```python
def find_order(order_ids, target):
    low = 0
    high = len(order_ids) - 1

    while low <= high:                    # there is still something to check
        middle = (low + high) // 2
        if order_ids[middle] == target:
            return middle
        elif order_ids[middle] < target:
            low = middle + 1              # target is to the right
        else:
            high = middle - 1             # target is to the left

    return -1                             # low went past high: not in the list
```

### Names used in the code
| Name | What it holds | Example |
|---|---|---|
| `order_ids` | the sorted list of order numbers | `[101, 104, 108, ...]` |
| `target` | the order number you're looking for | `120` |
| `low` | the first position the target could still be at | `4` |
| `high` | the last position the target could still be at | `6` |
| `middle` | the position halfway between `low` and `high` | `5` |

### What to say in the interview
"The list is sorted, so I can use binary search. I look at the middle, and because the list is in order, I know which half the target must be in. I keep halving until I find it or there's nothing left. That's O(log n): about 20 checks for a million orders."

---

## The pattern, in general
```python
low, high = 0, len(items) - 1
while low <= high:
    middle = (low + high) // 2
    if items[middle] == target:
        return middle
    elif items[middle] < target:
        low = middle + 1
    else:
        high = middle - 1
return -1
```

**A second form: "search on the answer".** Sometimes there's no list at all, and the question is "what's the smallest value that works?", like the slowest speed that still finishes on time. As long as you can write a function `works(value)` that answers True or False, and every value above a working one also works, you can binary search the **values** themselves instead of a list. Problem 3 is this kind.

---

## Common mistakes
1. **Using it on an unsorted list.** Binary search gives wrong answers if the list isn't sorted.
2. **`while low < high` instead of `while low <= high`.** In the version above, that skips the last item when `low` and `high` meet.
3. **`low = middle` instead of `low = middle + 1`.** You've already checked `middle`, so leave it out. Otherwise the loop can run forever.
4. **Forgetting the empty list.** `high` starts at -1, so the loop never runs and you return -1. Good, but check that your version does the same.

---

## Python you'll need
| Code | What it does | Example |
|---|---|---|
| `a // b` | divide and round down to a whole number | `7 // 2` gives `3` |
| `bisect.bisect_left(lst, x)` | Python's built-in binary search: the first position where `x` could go to keep the list sorted | `bisect_left([5, 12, 20], 12)` gives `1` |
| `math.ceil(x)` | round up | `math.ceil(2.1)` gives `3` |
| `(a + b - 1) // b` | divide and round **up**, using whole numbers only | `(7 + 3 - 1) // 3` gives `3` |

It's worth writing binary search yourself at least once. In an interview, say "I could also use `bisect`" to show you know it exists.

---

## Now practise
Open `c_practice.py` in this folder:
1. **Problem 1** is the worked example above. Type it in without looking.
2. **Problem 2** (first delivery at or after a time) and **Problem 3** (slowest pizza robot speed) are new.

Test your answers:
```bash
python3 practice.py 7
```

## More practice
Once all 3 problems pass, work through `e_more_practice.md` in this folder: 5 to 7 free LeetCode problems that use the same pattern, easiest first.
