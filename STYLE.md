# How every pattern folder is written (spec for authors)

Folder: `patterns/NN_short_name/` with exactly four files:

| File | What goes in it |
|---|---|
| `lesson.md` | The explanation. First line is `# Pattern NN: Name` (the runner reads it). |
| `practice.py` | Three problems. Each is a commented problem statement + a function whose body is `pass`. |
| `solutions.py` | The same three functions, solved, with short comments and the speed in plain words. |
| `tests.py` | `test_<function_name>(m)` functions. `m` is the module under test. Use plain `assert`. |

Rules for tests.py
- Every test calls `m.<function>(...)`. 3-5 asserts per problem, including edge cases (empty input, one item, ties, nothing found).
- Must ALL pass against solutions.py, and must fail (not crash the runner) against the `pass` stubs.
- Standard library only. Python 3.9+.

## The reader
A backend engineer who is new to algorithms. He finds abstract wording, metaphors and vague
references confusing. He wants everything in one place, in plain English, in a logical order.

## Writing rules (these come from his feedback, follow them strictly)
1. **Problem statements read like a person wrote them.** Short natural paragraphs, a pizza-shop
   situation, then the task. No bullet-point problem statements, no "You have two lists:" style.
   Model to copy:
   > Your pizza shop promises to deliver every order within 30 minutes. At the end of each night,
   > you need to find out which orders failed to meet that promise.
2. **No metaphors or comparisons** (no "index cards", "phone book", etc). Say what the code does.
3. **No vague references.** Never "the square right of 1" or "the 2nd one". Use exact values,
   names or addresses every time, e.g. "(row 1, column 0)", "order 103".
4. **No diagrams that need interpreting.** Use tables instead.
5. **Everything in one place.** Show the full data, the full code, and a table explaining every
   variable name. The reader should never need to scroll back up.
6. **Order of explanation:** the problem → the data → how you'd do it with a pen (table) →
   the code (complete, commented) → watch it run (table, row per step, exact values) →
   what to say in the interview.
7. Explain any Python feature that isn't basic (`heapq`, `deque`, `key=`, `lambda`, `yield`,
   slicing, `float("inf")`, `bisect`...) in a small "Python you'll need" table with an example.
8. Avoid jargon. If a term is unavoidable (BFS, O(n)), explain it in one plain sentence the first
   time, e.g. "O(n) means the time grows in step with the number of items".
9. British spelling.

## How the prose must read (approved by Ajimoti — follow exactly)
- **General first, then the example.** Say what the pattern does in general terms. Never state a
  pizza example as if it were the definition ("BFS finds the closest customer..." is WRONG).
  Then say what kinds of things it applies to, then give the example.
- **Flowing, natural sentences**, the way a person explains something out loud. Connect ideas with
  "so", "then", "because", "instead of", "until". Not choppy: no strings of tiny sentences
  ("It does X. Then Y. It never Z."). Not overloaded either: no sentence that tries to do two
  jobs where the second half doesn't follow from the first.
- Short paragraphs (2-3 sentences). No jargon without a plain explanation.

Approved models (copy this voice):

> BFS finds the fewest steps from a starting point to something you're looking for. It works on
> anything where things are connected to each other, like squares on a map, people who know each
> other, or stations on a train line, as long as every step counts the same.
>
> It starts by checking everything one step away, then everything two steps away, and keeps moving
> outwards like that. Because it always finishes the closer ones before going further, the first
> time it finds what you're looking for, you know it took the fewest steps to get there.

> A sliding window answers questions about groups of items that sit next to each other in a list,
> like the best three days in a row. Instead of adding up every group from scratch, it works out
> the first group once and then slides along, adding the new item that comes in and taking away
> the one that drops out.

> Dynamic programming answers a big question by building up to it from smaller versions of the
> same question. You start with the smallest size, write down its answer, and use the answers
> you've already written to work out the next size, until you reach the one you were asked about.

## lesson.md layout
```
# Pattern NN: Name

## In one sentence
## How to spot it            (what words/shapes in a question point to this pattern)
## Worked example: <Problem 1 title>
### The problem
### The data
### How you'd do it with a pen
### The code
### Names used in the code   (table)
### Watch it run             (table)
### What to say in the interview
## The pattern, in general   (a short generic template in code, with comments)
## Common mistakes           (3-5, concrete)
## Python you'll need        (table, only if needed)
## Now practise              (point to practice.py problems 2 and 3, and the test command)
```

## practice.py layout (per problem)
```
# =============================================================================
# 1. TITLE IN CAPITALS
# =============================================================================
# THE PROBLEM
#   human prose paragraphs
#
# THE DATA
#   exact Python values
#
# YOUR TASK
#   function name, what it returns, edge cases (e.g. "return -1 if ...")
#
# EXAMPLE
#   worked step by step with the exact values
#
# HINT
#   one or two lines (optional, never the whole answer)
def function_name(...):
    pass
```
Problem 1 is the lesson's worked example (so he can type it in after reading).
Problems 2 and 3 are new: problem 2 easy, problem 3 a little harder. Same pattern each time.
