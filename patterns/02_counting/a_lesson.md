# Pattern 02: Counting with a dict

**Watch first:** [Valid Anagram - Leetcode 242 - Python](https://www.youtube.com/watch?v=9UtInBqnCgA) (NeetCode, 0:00–9:10 only). Every problem's video is listed in `b_videos.md`.

**Commands for this pattern** (run them in the `pattern_course` folder):
```bash
python3 practice.py 2              # test your answers in c_practice.py
python3 practice.py 2 --solutions  # see the model answers pass
python3 practice.py 2 --reset      # blank c_practice.py, to rewrite from memory
```

## What it does
Counting with a dict answers questions about how often things appear in a list. It works on any list where things repeat, like words in a sentence, items in shopping baskets, votes in a poll, or orders in a day, because you go through the list once and keep a running tally for each thing in a dict.

Once the tally is done, you answer the question from the counts instead of going back to the list, so "which is the most common" or "which appeared only once" becomes a quick look at the dict. The same idea also lets you group things that are the same, by storing a list of matching items under each key instead of a number.

## A quick example
As an example, here's a tally of the orders in one hour as you go through them one by one:

| Order | Tally after this order |
|---|---|
| pepperoni | pepperoni 1 |
| hawaiian | pepperoni 1, hawaiian 1 |
| hawaiian | pepperoni 1, hawaiian 2 |
| margherita | pepperoni 1, hawaiian 2, margherita 1 |

From the finished tally you can see straight away that hawaiian is the most popular.

## When to use it
Use a counting dict whenever the question is about how often things appear, or about putting matching things together. Look out for:
- "how many", "most", "least", "top 3", "only once", "more than twice"
- **grouping** things that are the same (same toppings, same customer, same day)
- the urge to write "for each item, count how many others match it", which is a loop inside a loop that one counting pass replaces

---

## Worked example: What's popular right now?

### The problem
Your pizza shop's app has a "Popular right now" section that shows customers which pizzas have been ordered the most in the last hour.

As customers place orders, the system records the type of pizza and the minute each order was placed.

You want this section to reflect recent orders rather than all-time sales, so only orders placed within the last 60 minutes should count.

If two or more pizzas have the same number of orders, they should appear in alphabetical order.

**Your task is to identify the most popular pizzas from the last 60 minutes, ranked by the number of orders, with alphabetical ordering used to break ties.**

### The data
```python
events = [
    (0,  "margherita"),
    (30, "pepperoni"),
    (70, "pepperoni"),
    (80, "hawaiian"),
    (85, "hawaiian"),
    (90, "margherita"),
]
now = 90   # the current minute
k = 2      # how many pizzas to show
```
Each event is `(minute the order was placed, pizza name)`.

The answer should be `["hawaiian", "margherita"]`.

### How you'd do it with a pen
1. **Work out when an hour ago was.** It's minute 90, so an hour ago was minute 30. Only orders placed after minute 30 count.
2. **Ignore the old orders.** Minute 0 and minute 30 are not after minute 30.
3. **Count the rest:** hawaiian 2, pepperoni 1, margherita 1.
4. **Put them in order:** hawaiian has the most. Margherita and pepperoni are tied on 1, so they go alphabetically: margherita, then pepperoni.
5. **Take the top 2:** hawaiian, margherita.

### The code
```python
def trending(events, now, k):
    # Step 1: work out when "an hour ago" was
    one_hour_ago = now - 60

    # Step 2: count each pizza ordered after that
    counts = {}
    for minute, pizza in events:
        if minute > one_hour_ago:
            counts[pizza] = counts.get(pizza, 0) + 1

    # Step 3: sort by name first, then by count (biggest first)
    def how_many(p):
        return counts[p]

    alphabetical = sorted(counts)
    ranked = sorted(alphabetical, key=how_many, reverse=True)

    # Step 4: keep the top k
    return ranked[:k]
```

### Names used in the code
| Name | What it holds | Example |
|---|---|---|
| `events` | every order: (minute it was placed, pizza name) | `(70, "pepperoni")` |
| `now` | the current minute | `90` |
| `k` | how many pizzas to show | `2` |
| `one_hour_ago` | the minute it was an hour ago | `90 - 60 = 30` |
| `minute` | the minute **this** order was placed | `70` |
| `pizza` | the pizza name in **this** order | `"pepperoni"` |
| `counts` | dict: pizza name → how many times ordered | `{"pepperoni": 1, "hawaiian": 2}` |
| `how_many` | a small function: give it a pizza name, it gives back the count | `how_many("hawaiian")` gives `2` |
| `alphabetical` | the pizza names in A to Z order | `["hawaiian", "margherita", "pepperoni"]` |
| `ranked` | the pizza names, most popular first | `["hawaiian", "margherita", "pepperoni"]` |

### Watch it run
`one_hour_ago = 30`

| Order | `minute` | `pizza` | After 30? | `counts` after |
|---|---|---|---|---|
| 1st | 0 | margherita | No | `{}` |
| 2nd | 30 | pepperoni | No | `{}` |
| 3rd | 70 | pepperoni | Yes | `{pepperoni: 1}` |
| 4th | 80 | hawaiian | Yes | `{pepperoni: 1, hawaiian: 1}` |
| 5th | 85 | hawaiian | Yes | `{pepperoni: 1, hawaiian: 2}` |
| 6th | 90 | margherita | Yes | `{pepperoni: 1, hawaiian: 2, margherita: 1}` |

Then the two sorts:

| Step | Result |
|---|---|
| `sorted(counts)` (names, A to Z) | `["hawaiian", "margherita", "pepperoni"]` |
| sort that by `how_many`, biggest first | `["hawaiian", "margherita", "pepperoni"]` |
| `ranked[:2]` | `["hawaiian", "margherita"]` |

Margherita stays ahead of pepperoni because they both have a count of 1, and when two items have the same value, `sorted` keeps them in the order they were already in, which was A to Z.

### What to say in the interview
"I go through the orders once, keep only the last 60 minutes, and count each pizza in a dict. Then I sort the names alphabetically and sort again by count, biggest first. Ties stay alphabetical because sorting keeps equal items in the order they were in. Then I return the top k."

---

## The pattern, in general
```python
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1      # 0 the first time, then add 1

# then use counts to answer the question:
#   most common  -> sort by count
#   only once    -> keep items where counts[item] == 1
#   group things -> store a LIST per key instead of a number (see problem 3)
```
This takes one pass through the list plus whatever you then do with the counts, which is much faster than going back through the whole list to count each item separately.

## Common mistakes
1. **`counts[pizza] += 1` the first time you see a pizza.** It crashes with `KeyError`, because there's no count yet. Use `counts.get(pizza, 0) + 1`.
2. **Passing the whole dict into `.get()`.** `counts.get(counts, 0)` crashes with "unhashable type: 'dict'". The thing inside `.get()` is the key you're looking up, here `pizza`.
3. **Slicing a dict.** `counts[:2]` crashes. `[:2]` only works on a list. `sorted(counts)` gives you a list.
4. **Forgetting that `sorted` doesn't change anything.** `sorted(counts)` on its own line does nothing useful. Store it: `ranked = sorted(...)`.
5. **Using a list as a dict key.** Lists can't be dict keys ("unhashable type: 'list'"). Turn it into a tuple first: `tuple(my_list)`.

## Python you'll need
| Code | What it does | Example |
|---|---|---|
| `d.get(key, 0)` | the value for `key`, or 0 if it's not there yet | `counts.get("hawaiian", 0)` gives `0` the first time |
| `sorted(d)` | the dict's keys in a new list, A to Z | `["hawaiian", "margherita", "pepperoni"]` |
| `sorted(x, key=f)` | sort `x` using `f(item)` for each item instead of the item itself | `key=how_many` sorts by count |
| `reverse=True` | biggest first | |
| `my_list[:k]` | the first k items of a list | `[1, 2, 3][:2]` gives `[1, 2]` |
| `tuple(my_list)` | a tuple: like a list, but it can be a dict key | `tuple(["ham", "pineapple"])` |

## Now practise
Open `c_practice.py` in this folder:
- **Problem 1** is the example above. Type it in without looking.
- **Problem 2** (the first customer who only ordered once) and **Problem 3** (grouping orders with the same toppings) use the same counting dict.

Test your answers from the `pattern_course` folder:
```bash
python3 practice.py 2              # test your answers
python3 practice.py 2 --solutions  # see the model answers pass
```
Tomorrow, run `python3 practice.py 2 --reset` to blank your answers and write them again from memory.

## More practice
Once all 3 problems pass, work through `e_more_practice.md` in this folder: 5 to 7 free LeetCode problems that use the same pattern, easiest first. When you want even more, `e_practice_links.md` has whole LeetCode and NeetCode categories for this pattern, plus 6 to 8 more problems.
