# Pattern 12: Fastest route (Dijkstra)

**Watch first:** [How Dijkstra's Algorithm Works](https://www.youtube.com/watch?v=EFg3u_E6eHU) (Spanning Tree, 9 min), then [Dijkstras Shortest Path Algorithm Explained – With Example](https://www.youtube.com/watch?v=bZkzH5x0SKU) (FelixTechTips, 8 min). Every problem's video is listed in `b_videos.md`.

**Commands for this pattern** (run them in the `pattern_course` folder):
```bash
python3 practice.py 12              # test your answers in c_practice.py
python3 practice.py 12 --solutions  # see the model answers pass
python3 practice.py 12 --reset      # blank c_practice.py, to rewrite from memory
```

## What it does
Dijkstra's algorithm finds the quickest or cheapest way from a starting point to somewhere else, when each connection costs a different amount. It works on anything made of connected places where moving between them has its own cost, like roads that take different numbers of minutes, flights with different prices, or network links with different delays.

It keeps a note of the best cost it has found so far to each place, and always carries on from the place it can reach most cheaply. Because it always deals with the cheapest place first, no cheaper way to a place can turn up after it has finished with it. So as soon as it finishes with the place you're after, you have your answer.

## Before you start
This pattern joins two things you've already done:

| You learned | In pattern | What it did |
|---|---|---|
| BFS | 09 | Spread out from the start one step at a time, using a queue. Every move cost 1 minute. |
| Heap | 08 | Always hand you the smallest number in a list. |

**Dijkstra is BFS for connections that cost different amounts.** When one road takes 1 minute and another takes 8, going "one step at a time" no longer finds the fastest route, so instead you always carry on from **the place you can reach soonest**. The heap hands you that place, which is why the queue from BFS becomes a heap here.

The name is pronounced "DIKE-stra". It's named after the person who came up with it.

If you'd like to see it drawn out before reading on, these two videos show it on a small map:
- How Dijkstra's Algorithm Works (Spanning Tree, 9 min): https://www.youtube.com/watch?v=EFg3u_E6eHU
- Dijkstra's Shortest Path Algorithm Explained (FelixTechTips, 8 min, worked as a table): https://www.youtube.com/watch?v=bZkzH5x0SKU

## A quick example
For example, say you're booking flights from London to Rome, and these are the prices:

| Flight | Price |
|---|---|
| London → Rome | £200 |
| London → Paris | £50 |
| Paris → Rome | £60 |

Flying straight there costs £200, but going through Paris costs £50 + £60 = **£110**. Dijkstra finds the £110 route without listing every possible route, which matters once there are thousands of them.

## When to use it
Use it when you need the quickest, cheapest or shortest way between places and each connection has its own cost.
- The question asks for the **fastest**, **cheapest**, **shortest time** or **lowest cost** between places.
- Each road, flight or link has its **own number** (minutes, miles, pounds).
- No connection has a cost below zero. Dijkstra doesn't work if one does.
- If every connection costs the same, BFS (pattern 09) is simpler and does the same job.

---

## Worked example: The fastest way to a customer

### The problem
A customer has just placed an order, and your driver needs to get their pizza there as quickly as possible.

There are several ways from the shop to the customer, and some roads take longer to drive than others. The route with the fewest roads isn't always the fastest one.

You know how the roads connect and how many minutes each one takes. Find the fastest route from the shop to the customer, and how long it takes.

### The data
```python
roads = [("Shop", "A", 4),
         ("Shop", "B", 1),
         ("B",    "A", 2),
         ("A",    "C", 5),
         ("B",    "C", 8)]
```
Each road is `(place, other place, minutes)`, and roads go both ways. The customer is at **C**.

The answer should be `(8, ["Shop", "B", "A", "C"])`. If C can't be reached, return `(-1, [])`.

### How you'd do it with a pen
With a small map, you can list every route:

| Route | Minutes |
|---|---|
| Shop → A → C | 4 + 5 = 9 |
| Shop → B → C | 1 + 8 = 9 |
| Shop → B → A → C | 1 + 2 + 5 = **8**, the fastest |

The fastest route uses the **most** roads. On a real map there are far too many routes to list, so we need a method that finds the fastest one without checking them all.

We'll do it in two parts:
- **Part 1:** find the fastest **time** (8).
- **Part 2:** add the **route** (Shop, B, A, C).

---

## Part 1: find the fastest time

### The method
Keep a note of **the quickest time you've found so far to each place**. Then repeat these three steps:

1. **Pick the place you can reach soonest** that you haven't finished with yet.
2. **Look at every road out of it.** If going through this place gets you somewhere quicker than you knew before, update that place's time.
3. **Mark it as finished.**

Stop when the place you pick is C.

**Why you can stop there:** because you always pick the soonest place next, by the time you pick C every place still waiting is at least as far away as C, so no quicker way to C can turn up later.

### First, list the roads out of each place
The `roads` list is hard to search, so first turn it into a dict: place → the roads leaving it. Each road is added twice, once in each direction, because roads go both ways.

```python
roads_from = {
    "Shop": [("A", 4), ("B", 1)],
    "A":    [("Shop", 4), ("B", 2), ("C", 5)],
    "B":    [("Shop", 1), ("A", 2), ("C", 8)],
    "C":    [("A", 5), ("B", 8)],
}
```

### Watch it run (Part 1)
You keep three things:

| Name | What it holds |
|---|---|
| best | the quickest time found so far to each place |
| to visit | the heap, holding (time, place) pairs |
| done | the places you've finished with |

**Start.** best: Shop = 0. To visit: (0, Shop). Done: nothing.

---

**Take (0, Shop),** the smallest time in the heap. Shop isn't done, so mark it done. Roads out of Shop:

| Road to | Time going this way | Best before | Update? |
|---|---|---|---|
| A | 0 + 4 = 4 | none yet | **Yes, A = 4** |
| B | 0 + 1 = 1 | none yet | **Yes, B = 1** |

To visit: (1, B), (4, A)

---

**Take (1, B),** the smallest time in the heap. Mark B done. Roads out of B:

| Road to | Time going this way | Best before | Update? |
|---|---|---|---|
| Shop | 1 + 1 = 2 | 0 | No, 2 is slower |
| A | 1 + 2 = 3 | 4 | **Yes, A = 3** (quicker through B) |
| C | 1 + 8 = 9 | none yet | **Yes, C = 9** |

To visit: (3, A), (4, A), (9, C)

---

**Take (3, A),** the smallest time in the heap. Mark A done. Roads out of A:

| Road to | Time going this way | Best before | Update? |
|---|---|---|---|
| Shop | 3 + 4 = 7 | 0 | No |
| B | 3 + 2 = 5 | 1 | No |
| C | 3 + 5 = 8 | 9 | **Yes, C = 8** (quicker through A) |

To visit: (4, A), (8, C), (9, C)

---

**Take (4, A).** A is already done, because we found the quicker time of 3 earlier. **Skip it.**

To visit: (8, C), (9, C)

---

**Take (8, C).** C is the customer. **Stop. The fastest time is 8.**

---

**Why there were two A's and two C's in the heap:** when you find a quicker way to a place, you push the new time, but the old time stays in the heap. The `done` set lets you skip the old one when it comes out.

### The code (Part 1)
```python
import heapq

def fastest_time(roads, start, end):
    # list the roads leaving each place
    roads_from = {}
    for a, b, minutes in roads:
        if a not in roads_from:
            roads_from[a] = []
        if b not in roads_from:
            roads_from[b] = []
        roads_from[a].append((b, minutes))
        roads_from[b].append((a, minutes))      # roads go both ways

    best = {start: 0}
    done = set()
    to_visit = [(0, start)]

    while to_visit:
        time, place = heapq.heappop(to_visit)   # the place we can reach soonest
        if place in done:
            continue                            # old entry, skip it
        done.add(place)

        if place == end:
            return time

        for next_place, minutes in roads_from.get(place, []):
            new_time = time + minutes
            if next_place not in best or new_time < best[next_place]:
                best[next_place] = new_time
                heapq.heappush(to_visit, (new_time, next_place))

    return -1                                   # never reached the end
```

---

## Part 2: remember the route

### The method
To know the **route**, add one more dict: **`came_from`**. Whenever you update a place's best time, write down **which place you came from**.

### Watch it run (Part 2)
These are the same updates as in Part 1, now with `came_from` filled in:

| Taking | Updates made | `came_from` after |
|---|---|---|
| Shop | A = 4, B = 1 | A: Shop, B: Shop |
| B | A = 3, C = 9 | A: **B**, B: Shop, C: B |
| A | C = 8 | A: B, B: Shop, C: **A** |

At the end, `came_from = {"A": "B", "B": "Shop", "C": "A"}`.

**Walk backwards from C:**

| Step | Place | `came_from[place]` | Route so far |
|---|---|---|---|
| 1 | C | A | [C, A] |
| 2 | A | B | [C, A, B] |
| 3 | B | Shop | [C, A, B, Shop] |
| 4 | Shop | this is the start, stop | [C, A, B, Shop] |

Reverse it to get `["Shop", "B", "A", "C"]`.

### The code (Parts 1 and 2 together)
```python
import heapq

def fastest_route(roads, start, end):
    # Step 1: for each place, list the roads leaving it
    roads_from = {}
    for a, b, minutes in roads:
        if a not in roads_from:
            roads_from[a] = []
        if b not in roads_from:
            roads_from[b] = []
        roads_from[a].append((b, minutes))
        roads_from[b].append((a, minutes))      # roads go both ways

    best = {start: 0}          # quickest time found so far to each place
    came_from = {}             # the place before it on that quickest route
    done = set()               # places we've finished with
    to_visit = [(0, start)]    # heap of (time to get there, place)

    while to_visit:
        # Pick the place we can reach soonest
        time, place = heapq.heappop(to_visit)
        if place in done:
            continue                            # old entry, skip it
        done.add(place)

        # Reached the customer: walk back to build the route
        if place == end:
            route = [end]
            while route[-1] != start:
                route.append(came_from[route[-1]])
            route.reverse()
            return time, route

        # Check every road out of this place
        for next_place, minutes in roads_from.get(place, []):
            new_time = time + minutes
            if next_place not in best or new_time < best[next_place]:
                best[next_place] = new_time
                came_from[next_place] = place
                heapq.heappush(to_visit, (new_time, next_place))

    # Ran out of places without reaching the customer
    return -1, []
```

### Names used in the code
| Name | What it holds | Example |
|---|---|---|
| `roads` | every road: (place, other place, minutes) | `("B", "A", 2)` |
| `roads_from` | dict: place → list of (next place, minutes) | `roads_from["B"]` is `[("Shop", 1), ("A", 2), ("C", 8)]` |
| `best` | dict: place → quickest time found so far | `{"Shop": 0, "B": 1, "A": 3}` |
| `came_from` | dict: place → the place before it on the quickest route | `{"A": "B"}` |
| `done` | set of places we've finished with | `{"Shop", "B"}` |
| `to_visit` | heap of (time, place), smallest time first | `[(3, "A"), (4, "A"), (9, "C")]` |
| `time`, `place` | the pair just taken out of the heap | `3`, `"A"` |
| `next_place`, `minutes` | one road out of `place` | `"C"`, `5` |
| `new_time` | time to `next_place` if you go through `place` | `3 + 5 = 8` |
| `route` | the places in order, built backwards then reversed | `["Shop", "B", "A", "C"]` |

### What to say in the interview
"Every road takes a different time, so I'll use Dijkstra. I keep a heap of (time, place) and always carry on from the place I can reach soonest. For each road out of it, I update the next place if this way is quicker, and I record where I came from. When I take the customer out of the heap, that's the fastest time, and I walk back through `came_from` to build the route. It runs in about (roads × log roads) time."

---

## The pattern, in general
```python
import heapq

best = {start: 0}
done = set()
to_visit = [(0, start)]                  # heap of (cost so far, place)

while to_visit:
    cost, place = heapq.heappop(to_visit)
    if place in done:
        continue                         # an old, slower entry
    done.add(place)
    # (stop here if place is the target)
    for next_place, step_cost in connections[place]:
        new_cost = cost + step_cost
        if next_place not in best or new_cost < best[next_place]:
            best[next_place] = new_cost
            heapq.heappush(to_visit, (new_cost, next_place))
```

## Common mistakes
1. **Putting `(place, time)` in the heap instead of `(time, place)`.** The heap sorts by the first item, so the time must come first.
2. **Forgetting the `done` check.** Without it, old slower entries get handled again. The answer usually still comes out right, but it does extra work and can confuse the route.
3. **Only adding each road one way** when the roads go both ways. Add `(a → b)` and `(b → a)`.
4. **Stopping when you first *see* the customer instead of when you *take it out* of the heap.** In the example, C is first seen at 9 minutes, but the fastest is 8. Only the time you take it out with is final.
5. **Using Dijkstra when every road costs the same.** BFS (pattern 09) is simpler and does the same job then.

## Python you'll need
| Code | What it does | Example |
|---|---|---|
| `heapq.heappush(h, (3, "A"))` | add to the heap | |
| `heapq.heappop(h)` | take out the pair with the smallest first number | `[(3, "A"), (9, "C")]` gives `(3, "A")` |
| `continue` | skip the rest of this loop round and go to the next | |
| `roads_from.get(place, [])` | the list for `place`, or an empty list if it has none | |
| `route[-1]` | the last item in a list | `["C", "A"][-1]` is `"A"` |
| `route.reverse()` | flip the list in place | `["C", "A", "B"]` becomes `["B", "A", "C"]` |
| `d.setdefault(k, []).append(x)` | shortcut: create an empty list for `k` if needed, then add `x` | used in the solutions |

## Now practise
`c_practice.py` has three problems:
1. **The fastest way to a customer**, the example above. Type it in yourself: do Part 1 first, then add Part 2.
2. **Fastest time from the shop to every place.** Easy once 1 works.
3. **When has every shop got the promo message?** The links only go one way.

Test your answers from the `pattern_course` folder:
```bash
python3 practice.py 12              # test your answers
python3 practice.py 12 --solutions  # see the model answers pass
```
Tomorrow, run `python3 practice.py 12 --reset` to blank your answers and write them again from memory.

## More practice
Once all 3 problems pass, work through `e_more_practice.md` in this folder: 5 to 7 free LeetCode problems that use the same pattern, easiest first. When you want even more, `e_practice_links.md` has whole LeetCode and NeetCode categories for this pattern, plus 6 to 8 more problems.
