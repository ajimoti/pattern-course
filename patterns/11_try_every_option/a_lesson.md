# Pattern 11: Try every option

**Watch first:** [Backtracking was HARD until I learned it this way](https://www.youtube.com/watch?v=Ak-fxEwAR14) (AlgoMonster, 6 min). Every problem's video is listed in `b_videos.md`.


## What it does
Trying every option means listing every possible answer, checking each one, and keeping the best, instead of looking for a clever shortcut. It works for any question where the answer is an order or a group picked from a small set of things, like the order to visit a few places, which toppings to pick, or which orders to put together so they add up to an exact amount.

People often call this **brute force**. It's reliable because it can't miss the best answer, but the number of options grows very quickly as the list gets longer, so it's only practical when there are just a handful of items.

## A quick example
As an example, say a customer can pick any 2 toppings from ham (£1.20), mushroom (£0.80) and olive (£0.60), and you want the cheapest pair. There are only three possible pairs, so you can simply list them all and keep the cheapest:

| Pair | Total | Cheapest so far |
|---|---|---|
| ham + mushroom | £2.00 | £2.00 |
| ham + olive | £1.80 | £1.80 |
| mushroom + olive | £1.40 | **£1.40** |

## When to use it
Reach for it when the question wants the best order or the best group, and the input is small enough that checking everything is realistic. These are the signs to look for:

- **visit every place exactly once**, or **in what order**
- **every way to choose**, or **all combinations**
- **find a group that adds up to exactly** some amount
- a small input, sometimes with the question even saying brute force is fine

The catch is how fast the number of options grows, which makes it fine for a handful of items and far too slow for hundreds, so always mention this in the interview:

| Items | Orders to try (permutations) | Groups to try (any size) |
|---|---|---|
| 3 | 6 | 8 |
| 8 | 40,320 | 256 |
| 12 | 479,001,600 | 4,096 |
| 20 | 2,432,902,008,176,640,000 | 1,048,576 |

---

## Worked example: The shortest delivery route

### The problem
A driver starts at the pizza shop, delivers to three customers, then drives back to the shop. They can visit the customers in any order. Which order means the least driving?

Every place is given as a pair of numbers, like `1,1`. You don't need to picture it on a map, because Python works out the distances for you.

The input comes in as text, like this:
```
"0,0 1,1 2,0 2,2"
```
The first place is the shop. The rest are the customers. Return the shortest route (starting and ending at the shop) and its total distance.

### The data
To keep things simple, give each place a name:

| Name | Address |
|---|---|
| Shop | (0, 0) |
| A | (1, 1) |
| B | (2, 0) |
| C | (2, 2) |

### Step 1: read the input
Turn the text into a list of addresses:
```python
def read_points(text):
    points = []
    for pair in text.split(" "):          # "0,0"  "1,1"  "2,0"  "2,2"
        x, y = pair.split(",")            # "1,1" -> "1" and "1"
        points.append((int(x), int(y)))   # -> (1, 1)
    return points
```
`read_points("0,0 1,1 2,0 2,2")` gives `[(0, 0), (1, 1), (2, 0), (2, 2)]`.

### Step 2: how far is it between two places?
Python has a built-in function for this: **`math.dist(place1, place2)`**. It gives the straight-line distance between two addresses.

```python
math.dist((0, 0), (1, 1))    # 1.41
math.dist((0, 0), (2, 0))    # 2.0
math.dist((0, 0), (2, 2))    # 2.83
```

Every distance you'll need for this example:

| Between | Distance |
|---|---|
| Shop and A | 1.41 |
| Shop and B | 2 |
| Shop and C | 2.83 |
| A and B | 1.41 |
| A and C | 1.41 |
| B and C | 2 |

If you didn't know `math.dist` existed, that's fine: ask the interviewer, or write it yourself as `math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)`.

### Step 3: how long is a whole trip?
A trip is a list of places in order. Add up each drive from one place to the next:
```python
def trip_length(trip):
    total = 0
    for i in range(len(trip) - 1):
        total += math.dist(trip[i], trip[i + 1])
    return total
```

For the trip **Shop → A → C → B → Shop**:

| Drive | Distance |
|---|---|
| Shop to A | 1.41 |
| A to C | 1.41 |
| C to B | 2 |
| B to Shop | 2 |
| **Total** | **6.83** |

### Step 4: try every order
**`permutations`** gives every possible order of a list:
```python
from itertools import permutations

list(permutations(["A", "B", "C"]))
# [("A", "B", "C"), ("A", "C", "B"), ("B", "A", "C"),
#  ("B", "C", "A"), ("C", "A", "B"), ("C", "B", "A")]
```
Three customers can be visited in 6 different orders.

### How you'd do it with a pen
For each order, put the shop at the start and the end, measure it, and keep the shortest so far:

| Order | Trip | Length | Shortest so far |
|---|---|---|---|
| A B C | Shop → A → B → C → Shop | 7.66 | 7.66 |
| A C B | Shop → A → C → B → Shop | **6.83** | **6.83** (new best) |
| B A C | Shop → B → A → C → Shop | 7.66 | 6.83 |
| B C A | Shop → B → C → A → Shop | 6.83 | 6.83 (a tie, so keep the first) |
| C A B | Shop → C → A → B → Shop | 7.66 | 6.83 |
| C B A | Shop → C → B → A → Shop | 7.66 | 6.83 |

**Winner: Shop → A → C → B → Shop, 6.83.** Shop → B → C → A → Shop is the same loop driven the other way round, with the same distance, so either one is a correct answer.

### The code
```python
import math
from itertools import permutations

def read_points(text):
    points = []
    for pair in text.split(" "):
        x, y = pair.split(",")
        points.append((int(x), int(y)))
    return points


def trip_length(trip):
    total = 0
    for i in range(len(trip) - 1):
        total += math.dist(trip[i], trip[i + 1])
    return total


def best_route(points):
    shop = points[0]
    customers = points[1:]

    best = None
    shortest = float("inf")         # "infinitely far", so the first trip always wins

    for order in permutations(customers):
        trip = [shop] + list(order) + [shop]
        length = trip_length(trip)
        if length < shortest:
            shortest = length
            best = trip

    return best, shortest
```

To run it from the command line, as the original task asked:
```python
import sys

points = read_points(sys.argv[1])        # the text typed after the script name
trip, length = best_route(points)
print("Optimal route: " + " -> ".join(f"({x},{y})" for x, y in trip))
print(f"Total distance: {length:.2f}")
```
```
$ python3 delivery_route.py "0,0 1,1 2,0 2,2"
Optimal route: (0,0) -> (1,1) -> (2,2) -> (2,0) -> (0,0)
Total distance: 6.83
```

### Names used in the code
| Name | What it holds | Example |
|---|---|---|
| `points` | every address, shop first | `[(0, 0), (1, 1), (2, 0), (2, 2)]` |
| `shop` | the first address | `(0, 0)` |
| `customers` | every address except the shop | `[(1, 1), (2, 0), (2, 2)]` |
| `order` | one order of the customers | `((1, 1), (2, 2), (2, 0))` |
| `trip` | that order with the shop at both ends | `[(0, 0), (1, 1), (2, 2), (2, 0), (0, 0)]` |
| `length` | that trip's total distance | `6.83` |
| `shortest`, `best` | the shortest length found so far, and its trip | `6.83`, the trip above |

### Watch it run
The pen table above is exactly what the loop does: each row is one pass through `for order in permutations(customers)`, and the last column is `shortest` after that pass.

### What to say in the interview
"With only a few deliveries, I'll try every order of the customers with `permutations`, put the shop at the start and end, measure each trip, and keep the shortest. That's exact, but the number of orders grows very fast: 8 customers is 40,000 orders, 12 is nearly 500 million. For a lot of stops, I'd switch to always driving to the nearest customer not yet visited. That's fast, but it doesn't always find the very best route."

---

## The pattern, in general
**Every order** (when order matters):
```python
from itertools import permutations

best = None
for option in permutations(items):
    if option is better than best:
        best = option
```

**Every group of a given size** (when order doesn't matter):
```python
from itertools import combinations

for group in combinations(items, size):
    check the group
```

**Every group, written yourself with recursion** ("take it or leave it"):
For the first item, there are two choices: take it, or leave it. Either way, the rest of the list is a smaller version of the same problem.
```python
def choose(items, k):
    if k == 0:
        return [()]                       # one way to choose nothing: choose nothing
    if len(items) < k:
        return []                         # not enough items left: no ways
    first = items[0]
    rest = items[1:]
    with_first = [(first,) + group for group in choose(rest, k - 1)]
    without_first = choose(rest, k)
    return with_first + without_first
```
Interviewers sometimes ask you to do this without `itertools`, so it's worth knowing both.

## Common mistakes
1. **Forgetting the shop at both ends.** `permutations(customers)` only orders the customers. You add the shop yourself: `[shop] + list(order) + [shop]`.
2. **Starting `shortest` at 0.** Nothing is shorter than 0, so nothing ever wins. Start at `float("inf")`.
3. **Mixing up permutations and combinations.** Order matters (a route) → `permutations`. Order doesn't matter (a group of toppings) → `combinations`.
4. **Not saying how slow it gets.** Always mention the number of options grows very fast, and what you'd do for a big input.
5. **Reading the text one character at a time.** `"10,5"[0]` is `"1"`, not 10. Split on the comma first.

## Python you'll need
| Code | What it does | Example |
|---|---|---|
| `from itertools import permutations` | every order | `permutations([1, 2, 3])` gives 6 orders |
| `from itertools import combinations` | every group of a given size, order ignored | `combinations([1, 2, 3], 2)` gives (1,2), (1,3), (2,3) |
| `math.dist(a, b)` | straight-line distance between two (x, y) points | `math.dist((0, 0), (2, 0))` is `2.0` |
| `float("inf")` | a number bigger than any other | a starting value for "shortest so far" |
| `list(order)` | turn a tuple into a list, so you can join lists with `+` | `[shop] + list(order) + [shop]` |
| `f"{x:.2f}"` | show a number with 2 decimal places | `f"{6.828:.2f}"` is `"6.83"` |
| `sys.argv[1]` | the text typed after the script name | `"0,0 1,1 2,0 2,2"` |

## Now practise
Open `c_practice.py`:
- **Problem 1** is the route above. Type it in yourself without looking.
- **Problem 2** (easier): every way to choose toppings. Do it with `combinations`, then again without it.
- **Problem 3** (a little harder): find orders that exactly fill the delivery van.

Test your answers with `python practice.py 11`.

## More practice
Once all 3 problems pass, work through `e_more_practice.md` in this folder: 5 to 7 free LeetCode problems that use the same pattern, easiest first.
