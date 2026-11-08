# Pattern 10: DFS and recursion (go deep first)

**Watch first:** [Learn RECURSION in 5 minutes!](https://www.youtube.com/watch?v=ivl5-snqul8) (Bro Code, 6 min), then [Learn Depth First Search in 7 minutes](https://www.youtube.com/watch?v=by93qH4ACxo) (Bro Code, 8 min). Every problem's video is listed in `b_videos.md`.


## What it does
Recursion is when a function solves a problem by calling itself on a smaller piece of the same problem, then uses the answers that come back to build its own. It suits anything that contains smaller copies of itself, like folders inside folders, comments with replies to replies, or a combo deal that includes other deals.

DFS, short for **depth-first search**, uses the same idea to explore things that are connected, like squares on a map or roads between places. It follows one path as far as it can go, then backs up and tries the next one, so it ends up visiting everything that can be reached from where it started. It's usually written with recursion, because "explore from here" is the same job at every step.

## A quick example
As an example, say a folder holds 2 files plus a subfolder, and the subfolder holds 3 files. To count every file, the function counts the folder's own files and then calls itself on the subfolder, so the top folder's call has to wait for the subfolder's answer before it can finish:

| Call | Its own files | Files from folders inside it | Total it hands back |
|---|---|---|---|
| `count(subfolder)` | 3 | none | 3 |
| `count(top folder)` | 2 | 3, handed back by the subfolder | 5 |

## When to use it
Reach for recursion and DFS when something contains smaller versions of itself, or when you need to explore everything that's connected rather than find the nearest thing. These are the signs to look for:

- things inside things, to any depth: deals inside deals, folders inside folders
- **how many different routes** or **how many ways** to get somewhere
- **how many separate groups**, or whether everything is connected
- you need to visit everything, and the order you visit in doesn't matter

If you're not sure whether a question wants BFS or DFS, this is the difference:
| | BFS (Pattern 09) | DFS (this pattern) |
|---|---|---|
| Order | everything 1 step away, then 2 steps, ... | one path all the way down, then the next |
| Tool | a queue (`deque`) | the function calling itself |
| Best for | **fewest** steps, **nearest** thing | **counting** routes or groups, things inside things |

---

## First: recursion on its own
Before the worked example, here is recursion at its very smallest: a function that counts down by calling itself with a smaller number each time, until it reaches zero.

```python
def count_down(n):
    if n == 0:              # the stopping point
        print("Go!")
        return
    print(n)
    count_down(n - 1)       # call itself with a smaller number

count_down(3)
```
Output:
```
3
2
1
Go!
```

| Call | `n` | `n == 0`? | What it does |
|---|---|---|---|
| `count_down(3)` | 3 | no | prints 3, then calls `count_down(2)` |
| `count_down(2)` | 2 | no | prints 2, then calls `count_down(1)` |
| `count_down(1)` | 1 | no | prints 1, then calls `count_down(0)` |
| `count_down(0)` | 0 | **yes** | prints "Go!" and stops |

Every recursive function has two parts:
1. **The stopping point** (often called the "base case"): when the problem is so small you know the answer straight away. Here: `n == 0`.
2. **The call to itself** on a smaller problem. Here: `count_down(n - 1)`.

Without the stopping point, the function calls itself forever and Python stops it with a `RecursionError`.

**One more thing to know:** when a function calls itself, the first call **waits** until the inner call finishes and hands back its answer, then carries on. The worked example shows this in a table.

---

## Worked example: How many pizzas are in this deal?

### The problem
Your shop sells combo deals, and some deals include other deals. The Family deal comes with two pizzas of its own, plus a Kids box and a Party add-on. The Party add-on has a pizza of its own, plus a Mini pack.

The kitchen needs to know how many pizzas to make when someone orders a deal. Work out the total number of pizzas in a deal, including everything inside it, however many levels deep it goes.

### The data
Each deal is a dict with its own name, how many pizzas it has itself, and a list of the deals inside it:

```python
mini_pack  = {"name": "Mini pack",     "pizzas": 3, "contains": []}
kids_box   = {"name": "Kids box",      "pizzas": 1, "contains": []}
party_addon = {"name": "Party add-on", "pizzas": 1, "contains": [mini_pack]}
family_deal = {"name": "Family deal",  "pizzas": 2, "contains": [kids_box, party_addon]}
```

| Deal | Its own pizzas | Contains |
|---|---|---|
| Family deal | 2 | Kids box, Party add-on |
| Kids box | 1 | nothing |
| Party add-on | 1 | Mini pack |
| Mini pack | 3 | nothing |

The answer for the Family deal is **7**.

### How you'd do it with a pen
To count a deal: take its own pizzas, then count each deal inside it **the same way**, and add them up.

- Family deal: its own **2**, plus the Kids box, plus the Party add-on.
  - Kids box: its own **1**, contains nothing. Kids box total = **1**.
  - Party add-on: its own **1**, plus the Mini pack.
    - Mini pack: its own **3**, contains nothing. Mini pack total = **3**.
  - Party add-on total = 1 + 3 = **4**.
- Family deal total = 2 + 1 + 4 = **7**.

"Count each deal inside it the same way" is the recursion: the function calls itself for each inner deal.

### The code
```python
def total_pizzas(deal):
    total = deal["pizzas"]                    # start with this deal's own pizzas
    for inner_deal in deal["contains"]:
        total += total_pizzas(inner_deal)     # count the inner deal the same way
    return total
```

**Where's the stopping point?** When a deal contains nothing, the `for` loop runs zero times, so the function just returns its own pizzas. That's the stopping point: the Kids box and the Mini pack.

### Names used in the code
| Name | What it holds | Example |
|---|---|---|
| `deal` | the deal this call is counting | the Party add-on dict |
| `deal["pizzas"]` | that deal's own pizzas | `1` |
| `deal["contains"]` | the list of deals inside it | `[mini_pack]` |
| `inner_deal` | one deal from that list | the Mini pack dict |
| `total` | pizzas counted so far in **this** call | starts at `1`, ends at `4` |

Each call has its **own** `total`. The Party add-on's `total` and the Family deal's `total` are separate.

### Watch it run
| Step | Call | What happens | `total` in this call |
|---|---|---|---|
| 1 | `total_pizzas(Family deal)` | starts with its own 2 | 2 |
| 2 | ↳ `total_pizzas(Kids box)` | starts with its own 1, contains nothing, **returns 1** | 1 |
| 3 | `total_pizzas(Family deal)` | adds the 1 it got back | 3 |
| 4 | ↳ `total_pizzas(Party add-on)` | starts with its own 1 | 1 |
| 5 | ↳↳ `total_pizzas(Mini pack)` | starts with its own 3, contains nothing, **returns 3** | 3 |
| 6 | ↳ `total_pizzas(Party add-on)` | adds the 3 it got back, **returns 4** | 4 |
| 7 | `total_pizzas(Family deal)` | adds the 4 it got back, **returns 7** | 7 |

The arrows show how deep the call is. At step 2, the Family deal call is paused, waiting for the Kids box call to hand back its answer. At step 5, both the Family deal and the Party add-on calls are waiting.

### What to say in the interview
"Deals can contain deals to any depth, so I'll use recursion. A deal's total is its own pizzas plus the total of each deal inside it, worked out the same way. The stopping point is a deal that contains nothing: its total is just its own pizzas. Each deal is visited once, so the time grows in step with the number of deals."

---

## The pattern, in general
For **things inside things**:
```python
def solve(item):
    answer = the part that belongs to this item
    for inner in the items inside it:
        answer += solve(inner)          # same question, smaller piece
    return answer
```

For **exploring a graph or a map** (DFS), add a `seen` set so you never visit the same place twice:
```python
def explore(place):
    if place is off the map, blocked, or already in seen:
        return                          # stopping point
    seen.add(place)
    for next_place in the places next to it:
        explore(next_place)             # go deeper
```

## Common mistakes
1. **No stopping point.** The function calls itself forever and you get `RecursionError: maximum recursion depth exceeded`. Ask yourself: "when is the problem so small that I know the answer without calling myself?"
2. **Calling itself on the same thing, not a smaller one.** `total_pizzas(deal)` inside `total_pizzas(deal)` never gets smaller. It must be `total_pizzas(inner_deal)`.
3. **Forgetting to use what comes back.** Writing `total_pizzas(inner_deal)` on its own line throws the answer away. You need `total += total_pizzas(inner_deal)`.
4. **Forgetting `seen` on a map.** Square (0,0) explores (0,1), which explores (0,0) again, forever.
5. **Very deep recursion.** Python stops at about 1,000 calls deep. That's fine for interview-sized inputs. For huge maps you'd switch to a loop with a list used as a stack.

## Python you'll need
| Code | What it does | Example |
|---|---|---|
| `return` on its own | stop this call and hand back nothing | used in `explore` when a square is blocked |
| `dict.get(key, [])` | the value, or an empty list if the key is missing | `roads.get("C", [])` gives `[]` |
| a function inside a function | the inner one can use the outer one's names | `explore` uses `grid` and `seen` from `count_neighbourhoods` |

## Now practise
Open `c_practice.py`:
- **Problem 1** is the deal above. Type it in yourself without looking.
- **Problem 2** (easier): count every route from the shop to a customer on one-way roads.
- **Problem 3** (a little harder): count the separate neighbourhoods on a map.

Test your answers with `python practice.py 10`.

## More practice
Once all 3 problems pass, work through `e_more_practice.md` in this folder: 5 to 7 free LeetCode problems that use the same pattern, easiest first.
