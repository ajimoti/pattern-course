# Pattern 14: Dynamic programming (build answers from smaller answers)

**Watch first:** [Dynamic Programming 1D - Full Course - Python](https://www.youtube.com/watch?v=_i4Yxeh5ceQ) (NeetCode). Every problem's video is listed in `videos.md`.


## In one sentence
Work out the answer for the smallest version of the problem, store it, then use the stored answers to work out the next size up, until you reach the size you were asked about.

The name "dynamic programming" (often shortened to **DP**) doesn't describe the idea well. In practice it means: **fill in a table of answers, smallest first.**

## How to spot it
- The question asks for the **fewest**, **most**, **cheapest** or **number of ways**.
- The obvious "grab the biggest / best thing first" approach gives the **wrong** answer in some cases.
- You can describe the answer for a big amount using answers for **smaller amounts**. For example: "the fewest boxes for 8 slices is 1 box plus the fewest boxes for whatever's left."

---

## Worked example: The fewest boxes for an order of slices

### The problem
Your shop sells pizza by the slice, and slices go out in boxes that hold 1, 4 or 6 slices. Every box has to go out full, so no half-empty boxes.

Boxes cost money, so for each order you want to use as few boxes as possible. Sometimes the obvious choice isn't the best one. For 8 slices, grabbing the biggest box first gives 6 + 1 + 1 (three boxes), but 4 + 4 is only two.

Some orders can't be made up exactly with the boxes you have. When that happens, you need to know.

### The data
```python
slices = 8
box_sizes = [1, 4, 6]
```
The answer should be `2`. If an amount can't be made, return `-1`.

### Why "biggest box first" doesn't work
| Method | Boxes for 8 slices | Count |
|---|---|---|
| Biggest first | 6, then 1, then 1 | 3 |
| Best possible | 4, then 4 | **2** |

So we can't just grab boxes greedily. We need to compare the options properly.

### The key idea
Say you're packing 8 slices. **The last box you add** is a 1, a 4 or a 6.

| If the last box is | Slices left before it | Total boxes |
|---|---|---|
| 1 | 8 − 1 = 7 | 1 + (fewest boxes for 7) |
| 4 | 8 − 4 = 4 | 1 + (fewest boxes for 4) |
| 6 | 8 − 6 = 2 | 1 + (fewest boxes for 2) |

The best answer for 8 is the smallest of those three. **But that needs the answers for 7, 4 and 2.** So work them out first, starting from 0 and going up, and store each answer in a list called `best`:

- `best[0]` = fewest boxes for 0 slices = 0
- `best[1]` = fewest boxes for 1 slice
- ... and so on, up to `best[8]`.

### How you'd do it with a pen
For each amount, try each box size that fits. "Uses" means 1 box plus the stored answer for what's left.

| Amount | Try a 1-box | Try a 4-box | Try a 6-box | best |
|---|---|---|---|---|
| 0 | | | | **0** |
| 1 | 1 + best[0] = 1 | too big | too big | **1** |
| 2 | 1 + best[1] = 2 | too big | too big | **2** |
| 3 | 1 + best[2] = 3 | too big | too big | **3** |
| 4 | 1 + best[3] = 4 | 1 + best[0] = **1** | too big | **1** |
| 5 | 1 + best[4] = 2 | 1 + best[1] = 2 | too big | **2** |
| 6 | 1 + best[5] = 3 | 1 + best[2] = 3 | 1 + best[0] = **1** | **1** |
| 7 | 1 + best[6] = 2 | 1 + best[3] = 4 | 1 + best[1] = 2 | **2** |
| 8 | 1 + best[7] = 3 | 1 + best[4] = **2** | 1 + best[2] = 3 | **2** |

**best[8] = 2.** Every number in a row comes from rows above it that are already filled in.

### When it's impossible
With box sizes `[4, 6]` and 7 slices, rows 1, 2, 3, 5 and 7 have no way to make them. We mark those as **infinity** (`float("inf")`), meaning "can't be done". Any number is smaller than infinity, so a real answer always replaces it. If `best[7]` is still infinity at the end, return -1.

### The code
```python
def fewest_boxes(slices, box_sizes):
    # best[amount] = fewest boxes for that amount. Start with "can't be done".
    best = [0] + [float("inf")] * slices

    for amount in range(1, slices + 1):          # 1, 2, 3, ... up to slices
        for size in box_sizes:                   # try each box as the last one
            if size <= amount:                   # the box has to fit
                with_this_box = best[amount - size] + 1
                if with_this_box < best[amount]:
                    best[amount] = with_this_box

    if best[slices] == float("inf"):
        return -1                                # no mix of boxes works
    return best[slices]
```

### Names used in the code
| Name | What it holds | Example |
|---|---|---|
| `slices` | the order size | `8` |
| `box_sizes` | the box sizes available | `[1, 4, 6]` |
| `best` | list: `best[amount]` = fewest boxes for that amount | `[0, 1, 2, 3, 1, 2, 1, 2, 2]` at the end |
| `amount` | the amount being worked out right now | `8` |
| `size` | the box being tried as the last box | `4` |
| `amount - size` | slices left before that last box | `8 - 4 = 4` |
| `with_this_box` | boxes used if the last box is `size` | `best[4] + 1 = 2` |

### Watch it run
Here's what `best` looks like after each round of the outer loop:

| After amount | `best` |
|---|---|
| start | [0, inf, inf, inf, inf, inf, inf, inf, inf] |
| 1 | [0, 1, inf, inf, inf, inf, inf, inf, inf] |
| 2 | [0, 1, 2, inf, inf, inf, inf, inf, inf] |
| 3 | [0, 1, 2, 3, inf, inf, inf, inf, inf] |
| 4 | [0, 1, 2, 3, 1, inf, inf, inf, inf] |
| 5 | [0, 1, 2, 3, 1, 2, inf, inf, inf] |
| 6 | [0, 1, 2, 3, 1, 2, 1, inf, inf] |
| 7 | [0, 1, 2, 3, 1, 2, 1, 2, inf] |
| 8 | [0, 1, 2, 3, 1, 2, 1, 2, **2**] |

Return `best[8]`, which is **2**.

### What to say in the interview
"Taking the biggest box first doesn't always work. For 8 with boxes of 1, 4 and 6, it gives 3 boxes, but 4 + 4 is 2. So I'll use dynamic programming. `best[a]` is the fewest boxes for `a` slices. For each amount from 1 upwards, I try every box as the last one: 1 plus `best[a - size]`, and I keep the smallest. Anything that can't be made stays at infinity, and I return -1 for it. It's (slices × box sizes) time."

---

## The pattern, in general
1. **Decide what one entry in the table means.** For example, "`best[a]` = the fewest boxes for `a` slices".
2. **Fill in the smallest case by hand.** For example, `best[0] = 0`.
3. **Write the rule that builds one entry from smaller ones.** For example, `best[a] = min(best[a - size] + 1)` over each size.
4. **Fill the table from small to big.**
5. **Return the entry you were asked for.**

```python
table = [starting values]
table[0] = answer for the smallest case
for i in range(1, n + 1):
    table[i] = combine(table[smaller entries])
return table[n]
```

## Common mistakes
1. **Going greedy.** "Biggest first" or "best-looking first" fails on cases like 8 with [1, 4, 6]. Test that case.
2. **Forgetting the size-0 entry.** `best[0] = 0` (and `ways[0] = 1` in problem 3) is what everything else is built on.
3. **Not handling "impossible".** Start with infinity and check for it at the end. Starting with 0 would give wrong answers.
4. **Off-by-one on the list size.** You need entries 0 to `slices`, which is `slices + 1` entries. That's why it's `[0] + [inf] * slices`.
5. **Counting the same mix twice** in "how many ways" questions. Put the box sizes in the **outer** loop (see problem 3).

## Python you'll need
| Code | What it does | Example |
|---|---|---|
| `float("inf")` | a number bigger than any other ("infinity") | `5 < float("inf")` is `True` |
| `[0] + [x] * n` | a list starting with 0, followed by `n` copies of `x` | `[0] + [9] * 3` is `[0, 9, 9, 9]` |
| `range(1, n + 1)` | 1, 2, ..., n (the end number is left out, hence `+ 1`) | `range(1, 4)` gives 1, 2, 3 |
| `max(a, b)` / `min(a, b)` | the bigger / smaller of two numbers | `max(7, 11)` is `11` |

## Now practise
`practice.py` has three problems:
1. **The fewest boxes for an order of slices**, the example above. Type it in yourself.
2. **The most tips on one street.** At each house, decide: skip it, or stop and add this tip to the best total from two houses back. Fill the table house by house.
3. **How many ways to box an order?** Count the mixes instead of finding the fewest.

Test them with:
```
python practice.py 14
```

## More practice
Once all 3 problems pass, work through `more_practice.md` in this folder: 5 to 7 free LeetCode problems that use the same pattern, easiest first.
