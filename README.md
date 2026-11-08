# Pattern course

Fourteen algorithm patterns, learned one at a time, all set in the same pizza shop.
Plain Python 3.9+, standard library only.

## How to use it

0. Watch the two practice videos at the top of `VIDEOS.md` once, before you start.
1. Open the folder for the pattern you're on, e.g. `patterns/01_dict_lookup/`.
2. Watch the pattern's short video (linked at the top of `a_lesson.md`), then read the lesson. It walks through problem 1 step by step.
3. Write your answers in `c_practice.py`: problem 1 (from the lesson), then 2 and 3.
4. Test them:
   ```bash
   python3 practice.py 1              # test pattern 1
   python3 practice.py 1 --solutions  # see the model answers pass
   python3 practice.py                # your progress across all 14
   python3 practice.py 1 --reset      # blank c_practice.py again, to rewrite from memory
   ```
5. Stuck? Have a real go for 20-30 minutes, then watch that problem's video. It's linked above each problem in `c_practice.py` and listed in `b_videos.md`. Then close the video and write your own answer.
6. Only open `d_solutions.py` once your tests pass.
7. Then do at least 3 of the extra LeetCode problems in that pattern's `e_more_practice.md` (all free, easiest first). `MORE_PRACTICE.md` lists them all.
8. Tick the steps in your tracker page as you go.

## The four steps for every pattern

| Step | What to do |
|---|---|
| 1. Read the lesson | Read `a_lesson.md` and type in the worked example. |
| 2. All tests pass | Solve problems 2 and 3 until `python3 practice.py N` shows every test passing. |
| 3. Rewrite the next day | Delete your answers and write them again from memory. |
| 4. Rewrite a week later | Same again. If you can still do it, you own the pattern. |

Don't move to the next pattern until you've done steps 1 to 3.

## The patterns, in order

| # | Pattern | Use it when |
|---|---|---|
| 01 | Dict lookup | You need to match items between two lists, or there's a loop inside a loop searching for something. |
| 02 | Counting with a dict | How many times, most common, top k, any duplicates. |
| 03 | Two pointers | A sorted list, find a pair, or compare from both ends. |
| 04 | Sliding window | The best or longest run of things next to each other. |
| 05 | Sort, then walk through once | Start and end times that overlap. |
| 06 | Stack | Brackets, undo, most recent first, the next bigger value. |
| 07 | Binary search | Sorted data and you need a position fast, or the smallest number that works. |
| 08 | Heap | The next smallest or soonest, again and again. |
| 09 | BFS | Fewest steps when every step costs the same. |
| 10 | DFS and recursion | Explore everything connected, nested data, count every path. |
| 11 | Try every option | Small input, every order or combination. |
| 12 | Fastest route (Dijkstra) | Shortest time when roads take different times. |
| 13 | Order things that depend on each other | Prerequisites and build order. |
| 14 | Dynamic programming | Fewest, most, or number of ways, built from smaller amounts. |

## Rewriting from memory (steps 3 and 4)

```bash
python3 practice.py 1 --reset
```
This makes `c_practice.py` blank again for pattern 1. Your previous answers are saved in
`c_practice_backup.py` in the same folder, so nothing is lost.
