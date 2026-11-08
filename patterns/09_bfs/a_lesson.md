# Pattern 09: BFS (spread out one step at a time)

**Watch first:** [Learn Breadth First Search in 6 minutes](https://www.youtube.com/watch?v=7Cox-J7onXw) (Bro Code, 7 min). Every problem's video is listed in `b_videos.md`.


## What it does
BFS finds the fewest steps from a starting point to something you're looking for. It works on anything where things are connected to each other, like squares on a map, people who know each other, or stations on a train line, as long as every step counts the same.

It starts by checking everything one step away, then everything two steps away, and keeps moving outwards like that. Because it always finishes the closer ones before going further, the first time it finds what you're looking for, you know it took the fewest steps to get there.

BFS stands for **breadth-first search**, and "breadth-first" just means it covers everything at the current distance before moving any further out.

## A quick example
As an example, say you know Ben and Cara, Ben knows Dev, and Cara knows Dev and Eve. You want to know how many introductions it would take to reach Eve, so BFS checks the people one introduction away first, then the people two introductions away:

| Round | Steps from you | Who it checks | Found Eve? |
|---|---|---|---|
| 1 | 1 | Ben, Cara | no |
| 2 | 2 | Dev, Eve | **yes, in 2 steps** |

## When to use it
Reach for BFS when the question asks for the fewest steps between connected things and every step counts the same. These are the signs to look for:

- things connected to other things: squares on a map, people who referred each other, shops that call each other
- every step costs the same: one move, one introduction, one phone call
- words like **fewest steps**, **nearest**, **shortest chain**, or **how long until everyone** is reached

If the steps cost different amounts, for example one road takes 4 minutes and another takes 1, BFS gives the wrong answer and you need Dijkstra instead (Pattern 12).

---

## Where this comes from: the mango seller
This is the example from *Grokking Algorithms*. You want to find a mango seller among your friends, then your friends' friends, and so on. You want the **closest** one, so you check all your friends before any of their friends.

### The data
Who knows whom is written down in a dict. Each person points to a list of the people they know:

```python
graph = {
    "you":    ["alice", "bob", "claire"],
    "alice":  ["peggy"],
    "bob":    ["anuj", "peggy"],
    "claire": ["thom", "jonny"],
    "anuj":   [],
    "peggy":  [],
    "thom":   [],
    "jonny":  [],
}
sellers = {"thom"}      # the only mango seller
```

### The code
```python
from collections import deque

def find_seller(graph, start):
    search_queue = deque()
    search_queue += graph[start]          # start with your own friends
    searched = set()                      # people already checked

    while search_queue:
        person = search_queue.popleft()   # take the person at the front
        if person not in searched:        # only check someone once
            if person in sellers:
                return person
            else:
                search_queue += graph[person]   # add their friends to the back
                searched.add(person)
    return None
```

### Watch it run
| Step | Take from the front | Seller? | Add to the back | Queue after |
|---|---|---|---|---|
| start | | | alice, bob, claire | alice, bob, claire |
| 1 | alice | no | peggy | bob, claire, peggy |
| 2 | bob | no | anuj, peggy | claire, peggy, anuj, peggy |
| 3 | claire | no | thom, jonny | peggy, anuj, peggy, thom, jonny |
| 4 | peggy | no | (nobody) | anuj, peggy, thom, jonny |
| 5 | anuj | no | (nobody) | peggy, thom, jonny |
| 6 | peggy | already searched, skip | | thom, jonny |
| 7 | thom | **yes** | | stop, return "thom" |

Your three friends (alice, bob, claire) are all checked before any friend-of-a-friend. That's what makes BFS find the closest seller.

### Why `deque` and `popleft`
`deque` is short for **double-ended queue**, pronounced "deck". You can add and remove at either end:

| | Left end (front) | Right end (back) |
|---|---|---|
| Add | `appendleft(x)` | `append(x)` or `+=` |
| Remove | `popleft()` | `pop()` |

For BFS, always **add to the back** (`append` or `+=`) and **take from the front** (`popleft`). That makes it first in, first out: people are checked in the order they were found.

A normal list would work with `pop(0)`, but that's slow, because Python has to shift every other item along. `popleft()` on a deque is instant.

### Why `searched`
Peggy is a friend of both alice and bob, so she gets added twice. Without `searched`, you'd check her twice. On a map, where squares are each other's neighbours, you'd go back and forth forever. A set is used instead of a list because checking `in` on a set is instant.

---

## Worked example: Nearest customer on the map

### The problem
Your pizza shop has several customers waiting for their deliveries, and you want to find out which one your driver can reach the fastest.

You have a map of the surrounding streets represented as a grid. Each square is a road, a building, the shop or a customer's address. Your driver can move one square at a time, up, down, left or right, and each move takes exactly one minute. Buildings block the way, so the driver has to go around them. A customer who looks close might actually take longer to reach.

Find the minimum number of minutes needed to reach the nearest customer. If no customer can be reached, return -1.

### The data
```python
grid = ["S.#C",
        ".##.",
        "...C"]
```

| Symbol | Meaning |
|---|---|
| `S` | the shop |
| `C` | a customer |
| `#` | a building, you can't drive through it |
| `.` | road |

Every square has an address: **(row, column)**. Rows count down from 0 and columns count across from 0. `grid[row][column]` gives the symbol at that address.

| Address | Symbol |
|---|---|
| (0, 0) | S, the shop |
| (0, 1) | road |
| (0, 2) | building |
| (0, 3) | C, a customer |
| (1, 0) | road |
| (1, 1) | building |
| (1, 2) | building |
| (1, 3) | road |
| (2, 0) | road |
| (2, 1) | road |
| (2, 2) | road |
| (2, 3) | C, a customer |

The answer is **5**.

### Step 1: write the map as a graph, like the mango seller
In the mango example, each **person** had a list of **friends**. Here, each **square** has a list of **squares you can drive to in one move**.

From square (row, col), the four moves are:

| Move | Address |
|---|---|
| up | (row - 1, col) |
| down | (row + 1, col) |
| left | (row, col - 1) |
| right | (row, col + 1) |

A move only counts if the new address is on the map and isn't a building. Here's square **(1, 0)** checked by hand:

| Move | Address | On the map? | Building? | Keep? |
|---|---|---|---|---|
| up | (0, 0) | yes | no | **yes** |
| down | (2, 0) | yes | no | **yes** |
| left | (1, -1) | no, column -1 doesn't exist | | no |
| right | (1, 1) | yes | yes | no |

Doing that for every square that isn't a building gives this graph:

```python
graph = {
    (0, 0): [(1, 0), (0, 1)],
    (0, 1): [(0, 0)],
    (0, 3): [(1, 3)],
    (1, 0): [(0, 0), (2, 0)],
    (1, 3): [(0, 3), (2, 3)],
    (2, 0): [(1, 0), (2, 1)],
    (2, 1): [(2, 0), (2, 2)],
    (2, 2): [(2, 1), (2, 3)],
    (2, 3): [(1, 3), (2, 2)],
}
```
Buildings get no entry, because you can never stand on one.

### Step 2: search it like the mango seller
The search is the same as the mango code. The only addition is that we need **how many minutes**, not just "found it". So each item in the queue is a pair: `(square, minutes to get there)`. Every move adds 1.

### How you'd do it with a pen
Start at the shop with 0 minutes. Take from the front, add to the back.

| Step | Take from the front | What happens | Queue after |
|---|---|---|---|
| start | | put the shop in | (0,0) at 0 |
| 1 | (0,0) at 0 | not a customer, add its neighbours at 1 min | (1,0) at 1, (0,1) at 1 |
| 2 | (1,0) at 1 | not a customer, add (0,0) and (2,0) at 2 min | (0,1) at 1, (0,0) at 2, (2,0) at 2 |
| 3 | (0,1) at 1 | not a customer, add (0,0) at 2 min | (0,0) at 2, (2,0) at 2, (0,0) at 2 |
| 4 | (0,0) at 2 | already searched, skip | (2,0) at 2, (0,0) at 2 |
| 5 | (2,0) at 2 | not a customer, add (1,0) and (2,1) at 3 min | (0,0) at 2, (1,0) at 3, (2,1) at 3 |
| 6 | (0,0) at 2 | already searched, skip | (1,0) at 3, (2,1) at 3 |
| 7 | (1,0) at 3 | already searched, skip | (2,1) at 3 |
| 8 | (2,1) at 3 | not a customer, add (2,0) and (2,2) at 4 min | (2,0) at 4, (2,2) at 4 |
| 9 | (2,0) at 4 | already searched, skip | (2,2) at 4 |
| 10 | (2,2) at 4 | not a customer, add (2,1) and (2,3) at 5 min | (2,1) at 5, (2,3) at 5 |
| 11 | (2,1) at 5 | already searched, skip | (2,3) at 5 |
| 12 | (2,3) at 5 | **customer, return 5** | |

The customer at (0,3) is never reached: the building at (0,2) blocks the top row, so going round to it would take 7 minutes, and the search stops at 5.

### The code
```python
from collections import deque

def build_graph(grid):
    rows = len(grid)                 # 3
    cols = len(grid[0])              # 4
    graph = {}

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "#":
                continue                         # buildings get no entry

            nearby = [(row - 1, col),            # up
                      (row + 1, col),            # down
                      (row, col - 1),            # left
                      (row, col + 1)]            # right

            graph[(row, col)] = []
            for r, c in nearby:
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] != "#":
                    graph[(row, col)].append((r, c))

    return graph


def nearest_customer(grid):
    graph = build_graph(grid)

    for (row, col) in graph:                     # find the shop
        if grid[row][col] == "S":
            shop = (row, col)

    search_queue = deque()
    search_queue.append((shop, 0))               # the shop, 0 minutes
    searched = set()

    while search_queue:
        square, minutes = search_queue.popleft()
        if square not in searched:
            row, col = square
            if grid[row][col] == "C":            # like "person in sellers"
                return minutes
            else:
                for next_square in graph[square]:              # like graph[person]
                    search_queue.append((next_square, minutes + 1))
                searched.add(square)

    return -1                                    # ran out of squares, no customer reachable
```

### Names used in the code
| Name | What it holds | Example |
|---|---|---|
| `rows`, `cols` | size of the map | `3`, `4` |
| `graph` | square → squares you can drive to in one move | `graph[(1, 0)]` is `[(0, 0), (2, 0)]` |
| `nearby` | the four squares around one square, before checking them | `[(0, 0), (2, 0), (1, -1), (1, 1)]` |
| `shop` | the shop's address | `(0, 0)` |
| `search_queue` | squares waiting to be checked, with their minutes | `deque([((1, 0), 1), ((0, 1), 1)])` |
| `square`, `minutes` | the item just taken from the front | `(2, 3)`, `5` |
| `searched` | squares already checked | `{(0, 0), (1, 0)}` |

`0 <= r < rows` checks the row is real: with 3 rows, `r` must be 0, 1 or 2.

### Watch it run
The pen table above is exactly what this code does. Each "Take from the front" is one `popleft()`, each "add" is one `append()`, and each "skip" is the `if square not in searched` check.

### What to say in the interview
"I'll turn the grid into a graph where each square lists the squares you can move to. Then I'll do a BFS from the shop with a queue, carrying the minutes with each square. Because BFS checks everything 1 minute away before anything 2 minutes away, the first customer I take off the queue is the nearest. I keep a set of searched squares so I never check one twice. If the queue runs out, no customer is reachable, so I return -1. Every square is checked at most once, so the time grows in step with the size of the map."

---

## The pattern, in general
```python
from collections import deque

def bfs(graph, start):
    search_queue = deque()
    search_queue.append((start, 0))          # (place, steps to get there)
    searched = set()

    while search_queue:
        place, steps = search_queue.popleft()        # oldest first
        if place in searched:
            continue
        searched.add(place)

        if place is what you're looking for:
            return steps

        for next_place in graph.get(place, []):
            search_queue.append((next_place, steps + 1))

    return -1                                        # never found
```
Swap in your own "is this what I'm looking for?" check, and your own way of listing neighbours.

## Common mistakes
1. **Using `pop()` instead of `popleft()`.** That takes from the back, so you check the newest place first. It stops being BFS and the answer isn't the shortest any more.
2. **Forgetting `searched`.** On a map, (1,0) lists (0,0) and (0,0) lists (1,0), so without it you'd bounce between them forever.
3. **Not checking the edges of the map.** `grid[-1][0]` doesn't crash in Python, it quietly reads the **last** row. Always check `0 <= r < rows` and `0 <= c < cols` yourself.
4. **Forgetting the "never found" case.** If the queue runs out, return -1 (or whatever the question asks for) after the loop.
5. **Using BFS when steps cost different amounts.** BFS only gives the shortest answer when every step costs the same.

## Python you'll need
| Code | What it does | Example |
|---|---|---|
| `from collections import deque` | gets the double-ended queue | |
| `q.append(x)` | add to the back | `q.append(((1, 0), 1))` |
| `q += some_list` | add every item of a list to the back | `q += ["alice", "bob"]` |
| `q.popleft()` | take from the front | gives the oldest item |
| `while q:` | keep going while the queue isn't empty | an empty deque counts as False |
| `square, minutes = item` | split a pair into two names | `((2, 3), 5)` gives `(2, 3)` and `5` |
| `graph.get(place, [])` | the list for `place`, or an empty list if it isn't in the dict | |

## Now practise
Open `c_practice.py`:
- **Problem 1** is the map above. Type it in yourself without looking.
- **Problem 2** (easier): how many referral steps between two customers.
- **Problem 3** (a little harder): how many minutes until news reaches every shop.

Test your answers with `python practice.py 9`.

## More practice
Once all 3 problems pass, work through `e_more_practice.md` in this folder: 5 to 7 free LeetCode problems that use the same pattern, easiest first.
