# Pattern 03: Two pointers

**Watch first:** [Two Pointers Was Hard Until I Learned These Patterns](https://www.youtube.com/watch?v=rQhNcycbf8w) (AlgoMonster). Every problem's video is listed in `videos.md`.


## What it does
Two pointers finds pairs or compares items in a list by keeping track of two positions at once, instead of checking every item against every other item. It works on sorted lists of numbers, on words and codes you want to compare from both ends, and on two sorted lists you want to combine, because in each case you can tell which position to move next just by looking at the two items you're on.

Usually one position starts at the beginning and the other at the end, and you move them towards each other one step at a time until they meet, so you only go through the list once. A "pointer" here just means a variable holding a position in the list, like `left = 0`.

## A quick example
As an example, to check whether the code `"abcba"` reads the same backwards, you compare the first and last letters, then move both one step inwards:

| Left letter | Right letter | Same? |
|---|---|---|
| a | a | Yes |
| b | b | Yes |
| c (they've met) | | done: it reads the same backwards |

## When to use it
Use two pointers when the question is about pairs in a sorted list, about comparing the two ends of something, or about walking through two sorted lists together. Look out for:
- a **sorted** list (or one you're allowed to sort) and a question about **pairs**: "two items that add up to", "closest pair"
- comparing the **start and end** of something: "reads the same backwards"
- **two sorted lists** you have to combine or compare

---

## Worked example: Two pizzas that use up a budget exactly

### The problem
A customer has a gift card worth exactly £20 and wants to spend all of it on two different pizzas. The menu prices are listed from cheapest to most expensive.

Checking every pizza against every other pizza would work, but the full menu is long and the app has to answer instantly. Because the prices are already in order, there's a way to do it in one pass.

**Your task is to find two different pizzas whose prices add up to exactly the gift card amount.**

### The data
```python
prices = [4, 6, 9, 11, 15]    # sorted, cheapest first
budget = 20
```
The answer should be `(9, 11)`. If no two prices add up to the budget, return `None`.

### How you'd do it with a pen
Start with two prices: the cheapest (4, the first in the list) and the most expensive (15, the last in the list). Add them up:
- **Too small?** Swap the cheap price for the next one along (4 → 6). That's the only way to make the total bigger, because every later price in the list is bigger.
- **Too big?** Swap the expensive price for the one before it (15 → 11). That's the only way to make the total smaller.
- **Exactly right?** Done.
- **Both are now the same price in the list?** There's no pair.

| Left price | Right price | Total | Compared with 20 | What you do |
|---|---|---|---|---|
| 4 | 15 | 19 | too small | move left: 4 → 6 |
| 6 | 15 | 21 | too big | move right: 15 → 11 |
| 6 | 11 | 17 | too small | move left: 6 → 9 |
| 9 | 11 | 20 | exact | **answer: (9, 11)** |

You never miss the answer this way. When 4 + 15 = 19 is too small, 4 plus any other price would be even smaller, because 15 is the biggest price, so 4 can't be part of any pair and it's safe to move past it. Each move rules out one price for good.

### The code
```python
def two_prices(prices, budget):
    left = 0                      # position of the cheapest price still in play
    right = len(prices) - 1       # position of the most expensive price still in play

    while left < right:           # stop when they meet: no pair left to try
        total = prices[left] + prices[right]
        if total == budget:
            return (prices[left], prices[right])
        elif total < budget:
            left += 1             # too small: try a bigger price on the left
        else:
            right -= 1            # too big: try a smaller price on the right

    return None
```

### Names used in the code
| Name | What it holds | Example |
|---|---|---|
| `prices` | the menu prices, cheapest first | `[4, 6, 9, 11, 15]` |
| `budget` | the gift card amount | `20` |
| `left` | a position in `prices`, starting at the first one | `0` (price 4) |
| `right` | a position in `prices`, starting at the last one | `4` (price 15) |
| `total` | the two prices at `left` and `right` added together | `19` |

### Watch it run
| `left` | `prices[left]` | `right` | `prices[right]` | `total` | Action |
|---|---|---|---|---|---|
| 0 | 4 | 4 | 15 | 19 | less than 20: `left` becomes 1 |
| 1 | 6 | 4 | 15 | 21 | more than 20: `right` becomes 3 |
| 1 | 6 | 3 | 11 | 17 | less than 20: `left` becomes 2 |
| 2 | 9 | 3 | 11 | 20 | equal: return `(9, 11)` |

That took four steps, while checking every pair of five prices would take ten.

### What to say in the interview
"The prices are sorted, so I start with the cheapest and the most expensive. If the total is too small, I move up from the cheap end. If it's too big, I move down from the expensive end. Each step rules one price out, so it's a single pass through the list, instead of checking every pair."

---

## The pattern, in general
Two shapes come up most often:

```python
# Shape 1: from both ends towards the middle (pairs, mirror checks)
left, right = 0, len(items) - 1
while left < right:
    # look at items[left] and items[right]
    # decide whether to move left += 1, right -= 1, or both

# Shape 2: one pointer in each of two sorted lists (merging, comparing)
i, j = 0, 0
while i < len(a) and j < len(b):
    # take the smaller of a[i] and b[j], and move that pointer on
# then add whatever is left over in a or b
```
Each step moves at least one pointer, so the work grows in step with the length of the list rather than with the number of pairs.

## Common mistakes
1. **Using it on an unsorted list.** The "too small, so move left" reasoning only works if the list is sorted.
2. **`while left <= right` when you need two different items.** With `<=`, `left` and `right` can be the same position, so one pizza gets counted twice. Use `<`.
3. **Forgetting the leftovers when merging.** When one list runs out, the rest of the other list still needs adding.
4. **Starting `right` at `len(prices)`.** The last position is `len(prices) - 1`. Using `len(prices)` crashes with `IndexError`.

## Python you'll need
| Code | What it does | Example |
|---|---|---|
| `len(x) - 1` | the position of the last item | `len([4, 6, 9]) - 1` gives `2` |
| `x += 1` / `x -= 1` | add 1 / take 1 away | `left += 1` |
| `my_list[i:]` | everything from position `i` to the end | `[5, 8, 12][1:]` gives `[8, 12]` |
| `a.extend(b)` | add every item of `b` to the end of `a` | |
| `s.lower()` | the text in lowercase | `"AbC".lower()` gives `"abc"` |

## Now practise
Open `practice.py` in this folder:
- **Problem 1** is the example above. Type it in without looking.
- **Problem 2** (an order code that reads the same backwards) uses two pointers from both ends.
- **Problem 3** (merging two sorted lists of order times) uses one pointer in each list.

Test your answers from the `pattern_course` folder:
```bash
python3 practice.py 3
```

## More practice
Once all 3 problems pass, work through `more_practice.md` in this folder: 5 to 7 free LeetCode problems that use the same pattern, easiest first.
