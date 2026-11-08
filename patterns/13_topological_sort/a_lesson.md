# Pattern 13: Order things that depend on each other

**Watch first:** [Topological Sort | Kahn's Algorithm | Graph Theory](https://www.youtube.com/watch?v=cIBFEhD77b4) (WilliamFiset). Every problem's video is listed in `b_videos.md`.


## What it does
A topological sort puts things in an order where everything comes after the things it depends on. It works on any set of jobs with "this must happen before that" rules, like the build steps in a project, courses with prerequisites, the steps of a recipe, or software that has to be installed in a certain order. **Topological sort** is the name interviewers will know it by.

It counts how many jobs each one is still waiting for, does every job that's waiting for nothing, and then lowers the count of the jobs that were waiting on it. Repeating that until nothing is left gives you a valid order, and if you get stuck with jobs still waiting, you know some of them depend on each other in a loop, so no order is possible.

## A quick example
For example, getting dressed: you put on socks before shoes, and trousers before shoes.

| Job | Waiting for |
|---|---|
| socks | nothing |
| trousers | nothing |
| shoes | socks, trousers |

Socks and trousers are waiting for nothing, so they go first, and once both are done, shoes is waiting for nothing too. One valid order is socks, trousers, shoes.

## When to use it
Use it when a question gives you rules about what must happen before what, and asks for an order or whether everything can be done.
- Words like "depends on", "requires", "prerequisite", "before", "after".
- It asks for **an order** to do everything in.
- It asks **whether it's possible** to finish everything. A loop in the rules makes it impossible.

---

## Worked example: What order should we build the app in?

### The problem
The pizza app is split into a few parts, and some of them can't be built until others are done. The menu needs the database, for example, so the database has to be built first.

Work out an order to build everything in. When more than one part is ready at the same time, build them in alphabetical order, so the answer is always the same. If two parts each need the other, there's no way to build them, so raise an error.

### The data
```python
deps = {"app":      ["menu", "payments"],
        "payments": ["db"],
        "menu":     ["db"],
        "db":       []}
```
Each key is a part. Its list is **the parts it needs built first**. So `"app": ["menu", "payments"]` means the app can't be built until the menu and payments are both built.

The answer should be `["db", "menu", "payments", "app"]`.

### How you'd do it with a pen
**First, count how many parts each one is waiting for:**

| Part | Needs first | Waiting for |
|---|---|---|
| app | menu, payments | 2 |
| payments | db | 1 |
| menu | db | 1 |
| db | nothing | 0 |

**Next, flip it round. For each part, list which parts are waiting for it:**

| Part | Parts waiting for it |
|---|---|
| db | payments, menu |
| menu | app |
| payments | app |
| app | nobody |

**Now build.** Anything waiting for 0 is ready, so build it, then take 1 off the count of every part that was waiting for it.

| Step | Ready to build | Build (first alphabetically) | Counts that go down | New counts |
|---|---|---|---|---|
| 1 | db | **db** | payments 1 → 0, menu 1 → 0 | app 2, payments 0, menu 0 |
| 2 | menu, payments | **menu** | app 2 → 1 | app 1, payments 0 |
| 3 | payments | **payments** | app 1 → 0 | app 0 |
| 4 | app | **app** | nothing waits for app | |

**Order: db, menu, payments, app.**

**How you spot an impossible case.** Take `{"a": ["b"], "b": ["a"]}`, where a waits for b and b waits for a. Both start out waiting for 1, so **nothing is ever ready** and you build 0 of the 2 parts. Whenever you finish with fewer parts built than there are parts, there's a loop, so raise an error.

### The code
```python
import heapq

def build_order(deps):
    waiting_on = {}      # part -> how many parts it is still waiting for
    needed_by = {}       # part -> list of parts that need it

    # 1. count what each part is waiting for, and who needs what
    for part, needs in deps.items():
        waiting_on.setdefault(part, 0)
        for need in needs:
            waiting_on.setdefault(need, 0)        # a part might only appear in a list
            waiting_on[part] += 1
            needed_by.setdefault(need, []).append(part)

    # 2. everything waiting for 0 is ready
    ready = [part for part, count in waiting_on.items() if count == 0]
    heapq.heapify(ready)                          # alphabetically first comes out first

    # 3. build, then unlock what was waiting
    order = []
    while ready:
        part = heapq.heappop(ready)
        order.append(part)
        for waiting_part in needed_by.get(part, []):
            waiting_on[waiting_part] -= 1
            if waiting_on[waiting_part] == 0:
                heapq.heappush(ready, waiting_part)

    # 4. if anything was never built, there's a loop
    if len(order) != len(waiting_on):
        raise ValueError("some parts depend on each other in a loop")
    return order
```

### Names used in the code
| Name | What it holds | Example (at the start) |
|---|---|---|
| `deps` | the input: part → parts it needs first | `{"menu": ["db"], ...}` |
| `waiting_on` | part → how many parts it is still waiting for | `{"app": 2, "payments": 1, "menu": 1, "db": 0}` |
| `needed_by` | part → parts that are waiting for it | `{"db": ["payments", "menu"], "menu": ["app"], "payments": ["app"]}` |
| `ready` | heap of parts waiting for nothing | `["db"]` |
| `part` | the part being built right now | `"db"` |
| `waiting_part` | one part that was waiting for `part` | `"payments"` |
| `order` | the build order so far | `["db"]` |

### Watch it run
| Loop | `heappop` gives | `order` after | Counts changed | `ready` after |
|---|---|---|---|---|
| 1 | db | [db] | payments → 0, menu → 0 | [menu, payments] |
| 2 | menu | [db, menu] | app → 1 | [payments] |
| 3 | payments | [db, menu, payments] | app → 0 | [app] |
| 4 | app | [db, menu, payments, app] | none | [] |

`ready` is empty, so the loop ends. `order` has 4 parts and `waiting_on` has 4 parts, so there's no loop. Return the order.

### What to say in the interview
"This is a topological sort. I count how many dependencies each part has and keep a list of what each part unlocks. I start with everything that has zero dependencies, and each time I build one, I lower the count of the parts waiting on it and add any that hit zero. To keep ties alphabetical, I use a heap. If I finish with fewer parts than I started with, there's a cycle, so I raise an error. It runs in about (parts + dependencies) time."

---

## The pattern, in general
```python
waiting_on = {thing: 0 for thing in all_things}
unlocks = {thing: [] for thing in all_things}
for first, then in rules:                 # "first" must happen before "then"
    waiting_on[then] += 1
    unlocks[first].append(then)

ready = [t for t in all_things if waiting_on[t] == 0]
order = []
while ready:
    thing = ready.pop()                   # or heapq.heappop(ready) for alphabetical ties
    order.append(thing)
    for nxt in unlocks[thing]:
        waiting_on[nxt] -= 1
        if waiting_on[nxt] == 0:
            ready.append(nxt)             # or heapq.heappush(ready, nxt)

possible = len(order) == len(all_things)
```

## Common mistakes
1. **Getting the direction backwards.** In `deps`, `"menu": ["db"]` means menu waits for db, so **menu's** count goes up and db **unlocks** menu. Write one example out by hand before coding.
2. **Forgetting parts that only appear inside a list.** In `{"a": ["b"]}`, b is never a key, but it still has to be built. That's why the code uses `setdefault(need, 0)`.
3. **Not checking for a loop at the end.** Without the `len(order)` check, a loop gives you a short list instead of an error.
4. **Sorting the whole result alphabetically at the end.** That breaks the dependency order. Only choose alphabetically between parts that are ready at the same time.

## Python you'll need
| Code | What it does | Example |
|---|---|---|
| `d.setdefault(k, 0)` | if `k` isn't in `d` yet, set it to 0. Otherwise leave it alone. | `{}.setdefault("db", 0)` makes `{"db": 0}` |
| `d.setdefault(k, []).append(x)` | make an empty list for `k` if needed, then add `x` | |
| `heapq.heapify(lst)` | turn an existing list into a heap | `["menu", "db"]` → `"db"` comes out first |
| `heapq.heappop(h)` with strings | takes out the alphabetically first string | `"db"` before `"menu"` |
| `{t: 0 for t in things}` | build a dict with every item set to 0 | `{"a": 0, "b": 0}` |

## Now practise
`c_practice.py` has three problems:
1. **What order should we build the app in?**, the example above. Type it in yourself.
2. **The order to do the kitchen prep.** Same method, but the rules are given as (first, then) pairs.
3. **Can a new driver finish all the training?** Return True or False instead of the order.

Test them with:
```
python practice.py 13
```

## More practice
Once all 3 problems pass, work through `e_more_practice.md` in this folder: 5 to 7 free LeetCode problems that use the same pattern, easiest first.
