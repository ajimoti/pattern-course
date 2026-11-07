# Pattern 08: Heap (always get the smallest next)

**Watch first:** [Heaps in 3 minutes — Intro](https://www.youtube.com/watch?v=0wPlzMU-k00) (Michael Sambol). Every problem's video is listed in `videos.md`.


## In one sentence
A heap is a list that always keeps its smallest item at position `[0]`, so you can keep taking the smallest out and putting new items in, quickly.

## How to spot it
- "the **next free** driver / oven / slot"
- "the **soonest**, **closest**, **cheapest** one", asked again and again while things keep changing
- "the **k smallest** / **k closest** / **top k**"
- **Merging** several sorted lists into one

If you only need the smallest **once**, `min()` is fine. A heap is for when you need it **over and over**, with items being added and removed in between.

---

## The three things you need
```python
import heapq

heapq.heappush(h, x)    # add x
h[0]                    # look at the smallest (without removing it)
heapq.heappop(h)        # remove the smallest and give it back
```

**Watch it work:**
```python
h = []
heapq.heappush(h, 8)     # h = [8]
heapq.heappush(h, 3)     # h = [3, 8]
heapq.heappush(h, 10)    # h = [3, 8, 10]
heapq.heappush(h, 1)     # h = [1, 3, 10, 8]   <- not fully sorted!
h[0]                     # 1
heapq.heappop(h)         # gives 1,  h = [3, 8, 10]
heapq.heappop(h)         # gives 3,  h = [8, 10]
```

**Watch out:** after pushing 1, the list is `[1, 3, 10, 8]`. That isn't fully sorted, and it's meant to be that way. A heap only promises that `[0]` is the smallest. If you print one to debug and it looks out of order, nothing is wrong.

**Second watch-out:** only change a heap with `heappush` and `heappop`. If you use `.append()` or change a value directly, `[0]` stops being the smallest.

**Pairs work too.** If you push `(distance, name)`, the heap compares the distance first, and the name only if two distances are equal.

---

## Worked example: Giving orders to drivers

### The problem
Your pizza shop has two delivery drivers, and new orders are constantly coming out of the oven.

Each delivery takes exactly six minutes, including the time needed for the driver to return to the shop.

Whenever a pizza is ready, you want to assign it to whichever driver becomes available first. If a driver is already at the shop, they can leave immediately. However, if both drivers are out making deliveries, the pizza must wait until one returns.

Your task is to determine when each order actually leaves the shop, taking into account when the drivers become available.

### The data
```python
orders = [(101, 0), (102, 2), (103, 3), (104, 10)]
drivers = 2
trip = 6
```
Each order is `(order number, minute the pizza is ready)`, already in time order. Both drivers are at the shop at minute 0.

The answer is `{101: 0, 102: 2, 103: 6, 104: 10}`: each order number and the minute it leaves.

### How you'd do it with a pen
Keep a list of **the minute each driver is back at the shop**. At the start it's `[0, 0]`.

For each order:
1. **Find the driver who's back soonest**, which is the smallest number in the list.
2. **The order leaves at whichever is later:** the pizza being ready, or that driver being back.
3. **That driver is now back at** leave time + 6.

| Order | Ready | Drivers back at | Soonest | Leaves at | Drivers back at after |
|---|---|---|---|---|---|
| 101 | 0 | [0, 0] | 0 | later of 0 and 0 = **0** | [6, 0] |
| 102 | 2 | [6, 0] | 0 | later of 2 and 0 = **2** | [6, 8] |
| 103 | 3 | [6, 8] | 6 | later of 3 and 6 = **6** (waits 3 min) | [12, 8] |
| 104 | 10 | [12, 8] | 8 | later of 10 and 8 = **10** | [12, 16] |

### The code, first version: with `min()`
```python
def dispatch(orders, drivers, trip):
    back_at = [0] * drivers                 # minute each driver is back at the shop
    leaves = {}

    for order_id, ready in orders:
        soonest = min(back_at)              # the soonest any driver is back
        driver = back_at.index(soonest)     # which driver that is
        leave_time = max(ready, soonest)    # pizza ready AND driver back
        leaves[order_id] = leave_time
        back_at[driver] = leave_time + trip

    return leaves
```
This is correct. But `min()` and `.index()` both look at every driver, for every order. With 1,000 drivers, that's around 1,000 steps per order.

### The code, second version: with a heap
With a heap, you don't need to know **which** driver it is. Take out the soonest time and put back that driver's new time:
```python
import heapq

def dispatch(orders, drivers, trip):
    back_at = [0] * drivers                 # all zeros is already a valid heap
    leaves = {}

    for order_id, ready in orders:
        soonest = heapq.heappop(back_at)               # take out the soonest driver
        leave_time = max(ready, soonest)               # pizza ready AND driver back
        leaves[order_id] = leave_time
        heapq.heappush(back_at, leave_time + trip)     # put them back with their new time

    return leaves
```
`heappop` and `heappush` take about 10 steps each with 1,000 drivers, instead of about 1,000.

### Names used in the code
| Name | What it holds | Example |
|---|---|---|
| `orders` | each order as (order number, minute ready) | `(103, 3)` |
| `drivers` | how many drivers there are | `2` |
| `trip` | minutes for one delivery, there and back | `6` |
| `back_at` | the heap: the minute each driver is back at the shop | `[6, 8]` |
| `soonest` | the earliest minute any driver is back | `6` |
| `leave_time` | when this order actually leaves | `6` |
| `leaves` | dict: order number → minute it leaves | `{101: 0, 102: 2}` |

### Watch it run (heap version)
| Order | Ready | `heappop` gives | `leave_time` | Push back | `back_at` after |
|---|---|---|---|---|---|
| 101 | 0 | 0 | 0 | 6 | [0, 6] |
| 102 | 2 | 0 | 2 | 8 | [6, 8] |
| 103 | 3 | 6 | **6** | 12 | [8, 12] |
| 104 | 10 | 8 | 10 | 16 | [12, 16] |

Returns `{101: 0, 102: 2, 103: 6, 104: 10}`.

### What to say in the interview
"I keep a heap of when each driver is back at the shop. For each order, I pop the soonest driver. The order leaves at whichever is later, the pizza being ready or the driver being back. Then I push that driver back with their new return time. Each order costs O(log d), where d is the number of drivers. That means it grows very slowly even with many drivers."

---

## The pattern, in general
```python
import heapq
h = starting_items            # use heapq.heapify(h) if they aren't all equal
for item in work:
    smallest = heapq.heappop(h)          # 1. take out the soonest / smallest
    ...                                  # 2. use it
    heapq.heappush(h, new_value)         # 3. put it back with its new value
```

---

## Common mistakes
1. **Treating the heap as a sorted list.** Only `h[0]` is guaranteed to be the smallest. `h[1]` is **not** necessarily the second smallest.
2. **Using `.append()` instead of `heappush`.** The heap stops working properly.
3. **Wanting the biggest, not the smallest.** Python's heap only gives the smallest. Push negative numbers (`-x`), and turn them back when you pop.
4. **Calling `heappop` on an empty heap.** That crashes. Check `if h:` first.

---

## Python you'll need
| Code | What it does | Example |
|---|---|---|
| `heapq.heapify(lst)` | turns an existing list into a heap, in place | `h = [5, 1, 3]; heapq.heapify(h)` makes `h[0]` equal 1 |
| `heapq.nsmallest(k, lst)` | the k smallest items, smallest first | `nsmallest(2, [5, 1, 3])` gives `[1, 3]` |
| `[0] * 3` | a list of 3 zeros | `[0, 0, 0]` |

---

## Now practise
Open `practice.py` in this folder:
1. **Problem 1** is the worked example above. Write the heap version.
2. **Problem 2** (the closest customers) and **Problem 3** (merging sorted order lists) are new.

Test your answers:
```bash
python3 practice.py 8
```
