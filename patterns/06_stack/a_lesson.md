# Pattern 06: Stack

**Watch first:** [Python Stacks - Python Tutorial for Absolute Beginners](https://www.youtube.com/watch?v=NKmasqr_Xkw) (Programming with Mosh, 5 min). Every problem's video is listed in `b_videos.md`.

**Commands for this pattern** (run them in the `pattern_course` folder):
```bash
python3 practice.py 6              # test your answers in c_practice.py
python3 practice.py 6 --solutions  # see the model answers pass
python3 practice.py 6 --reset      # blank c_practice.py, to rewrite from memory
```

## What it does
A stack is a list where you only ever add to the end and take from the end, so the last thing you put in is always the first thing you get back. That makes it useful whenever the most recent item is the one you need to deal with next, like undoing your last action, matching a closing bracket with the opening one before it, or going back through the pages you've visited in a browser.

You don't need anything special in Python, because a normal list already works as a stack:

| Code | What it does |
|---|---|
| `stack.append(x)` | add `x` to the end |
| `stack.pop()` | remove the last item and give it back |
| `stack[-1]` | look at the last item without removing it |
| `if stack:` | True if the stack has anything in it |

## A quick example
For example, a text editor keeps every letter you type on a stack, so that pressing undo removes whatever you typed most recently.

| Action | Stack after |
|---|---|
| type `a` | `a` |
| type `b` | `a b` |
| type `c` | `a b c` |
| undo | `a b` (`c` went in last, so it comes out first) |
| type `d` | `a b d` |

## When to use it
Use a stack when the thing you need to deal with next is always the most recent one you haven't finished with yet, which shows up in questions like:
- **undo**: "go back to how it was before the last action"
- **matching pairs**: brackets, opening and closing tags, start and end markers
- "the **most recent** one that hasn't been dealt with yet"
- "for each item, find the **next one that is bigger**"

---

## Worked example: Are the brackets in an order note balanced?

### The problem
Customers can add a note to their order, and the kitchen's printer uses brackets to format it: `( )`, `[ ]` and `{ }`. If a note has a bracket that's never closed, or closed with the wrong type, the printer jams and the ticket comes out as nonsense.

Before a note is sent to the kitchen, you want to check that every bracket is closed, by the right type, in the right order. Any other characters in the note don't matter.

Your task is to say whether the brackets in a note are balanced.

### The data
```python
note = "(extra cheese [no onions]) {ring bell}"
```
The answer is `True`.

Some notes that should give `False`:

| Note | Why it's wrong |
|---|---|
| `"(extra cheese"` | the `(` is never closed |
| `"no onions)"` | the `)` has nothing to close |
| `"[well done)"` | `[` is closed with `)`, the wrong type |
| `"([)]"` | `[` was opened last, so it must be closed first |

### How you'd do it with a pen
Read the note from left to right, writing each **opening** bracket at the end of a list as you meet it. When you reach a **closing** bracket, it has to match the **last** opening bracket you wrote down, so if it does you cross that one off, and if it doesn't (or there's nothing left to match) the note is broken.

By the end the list should be empty, because anything left over is a bracket that was never closed.

For `"(extra cheese [no onions]) {ring bell}"`, ignoring the letters and spaces:

| Character | Opening or closing? | List before | What you do | List after |
|---|---|---|---|---|
| `(` | opening | `[]` | write it down | `["("]` |
| `[` | opening | `["("]` | write it down | `["(", "["]` |
| `]` | closing | `["(", "["]` | last is `[`, matches, cross off | `["("]` |
| `)` | closing | `["("]` | last is `(`, matches, cross off | `[]` |
| `{` | opening | `[]` | write it down | `["{"]` |
| `}` | closing | `["{"]` | last is `{`, matches, cross off | `[]` |
| end | | `[]` | list is empty | **True** |

### The code
```python
def is_balanced(note):
    pairs = {")": "(", "]": "[", "}": "{"}    # closing bracket -> its opening bracket
    stack = []

    for char in note:
        if char in "([{":                       # opening bracket
            stack.append(char)
        elif char in ")]}":                     # closing bracket
            if not stack:                       # nothing to close
                return False
            if stack[-1] != pairs[char]:        # wrong type
                return False
            stack.pop()                         # matched, cross it off
        # any other character is ignored

    return len(stack) == 0                      # anything left was never closed
```

### Names used in the code
| Name | What it holds | Example |
|---|---|---|
| `note` | the customer's note | `"(extra cheese [no onions])"` |
| `pairs` | dict: each closing bracket → the opening bracket it needs | `pairs["]"]` gives `"["` |
| `stack` | opening brackets not yet closed, most recent last | `["(", "["]` |
| `char` | the character being looked at | `"["` |

### Watch it run on a broken note: `"([)]"`
| `char` | `stack` before | Check | Result |
|---|---|---|---|
| `(` | `[]` | opening | `stack = ["("]` |
| `[` | `["("]` | opening | `stack = ["(", "["]` |
| `)` | `["(", "["]` | needs `(`, but `stack[-1]` is `[` | **return False** |

### What to say in the interview
"I go through the note once and keep a stack of opening brackets that haven't been closed. A closing bracket has to match the one on top of the stack, the most recent one. If it doesn't match, or the stack is empty, it's unbalanced. At the end the stack must be empty. That's O(n): the work grows in step with the length of the note."

---

## The pattern, in general
```python
stack = []
for item in items:
    if item starts something:
        stack.append(item)
    elif item ends something:
        if not stack:              # nothing to end
            ...
        top = stack.pop()          # the most recent thing still open
        ...
return ...                         # often: is the stack empty?
```

---

## Common mistakes
1. **Calling `stack.pop()` or `stack[-1]` on an empty list.** That crashes with an `IndexError`. Check `if not stack` first.
2. **Forgetting the final check.** `"(("` never fails during the loop, but the stack isn't empty at the end.
3. **Using `stack.pop(0)`.** That takes from the front, which makes it a queue, not a stack.

---

## Now practise
Open `c_practice.py` in this folder:
1. **Problem 1** is the worked example above. Type it in without looking.
2. **Problem 2** (undo in the order editor) and **Problem 3** (days until a busier day) are new.

Test your answers:
```bash
python3 practice.py 6              # test your answers
python3 practice.py 6 --solutions  # see the model answers pass
```
Tomorrow, run `python3 practice.py 6 --reset` to blank your answers and write them again from memory.

## More practice
Once all 3 problems pass, work through `e_more_practice.md` in this folder: 5 to 7 free LeetCode problems that use the same pattern, easiest first.
