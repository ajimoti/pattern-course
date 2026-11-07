"""
PATTERN 13: ORDER THINGS THAT DEPEND ON EACH OTHER - SOLUTIONS
"""
import heapq


# =============================================================================
# 1. WHAT ORDER SHOULD WE BUILD THE APP IN?
# =============================================================================
# Idea: count how many parts each part is still waiting for. Anything waiting
# for 0 is ready. Build the ready part that comes first alphabetically, then
# lower the count of every part that was waiting for it. If you run out of
# ready parts before building everything, some parts wait on each other in a
# loop, so it's impossible.
# Speed: about (parts + dependencies), plus a little for the heap.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Course Schedule I and II | Pre-requisite Tasks | Topological Sort (C++/Java) (take U forward)
#   https://www.youtube.com/watch?v=WAOfKpxYHR8
#   Same idea as LeetCode 210 Course Schedule II. The video uses a different story and
#   different names, so watch for the method, not the details.
def build_order(deps):
    waiting_on = {}      # part -> how many parts it is still waiting for
    needed_by = {}       # part -> parts that need it

    for part, needs in deps.items():
        waiting_on.setdefault(part, 0)
        for need in needs:
            waiting_on.setdefault(need, 0)        # a part might only appear as a need
            waiting_on[part] += 1
            needed_by.setdefault(need, []).append(part)

    ready = [part for part, count in waiting_on.items() if count == 0]
    heapq.heapify(ready)                          # smallest name comes out first

    order = []
    while ready:
        part = heapq.heappop(ready)
        order.append(part)
        for waiting_part in needed_by.get(part, []):
            waiting_on[waiting_part] -= 1
            if waiting_on[waiting_part] == 0:
                heapq.heappush(ready, waiting_part)

    if len(order) != len(waiting_on):
        raise ValueError("some parts depend on each other in a loop")
    return order


# =============================================================================
# 2. THE ORDER TO DO THE KITCHEN PREP
# =============================================================================
# Idea: the same as problem 1. The only difference is how the rules are given:
# here each rule is (do this first, then this).
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Kahn's Algorithm | Topological Sort Algorithm | BFS (take U forward)
#   https://www.youtube.com/watch?v=73sneFXuTEg
#   Same idea as LeetCode Topological sort walkthrough. The video uses a different story and
#   different names, so watch for the method, not the details.
def prep_order(steps, rules):
    waiting_on = {step: 0 for step in steps}
    unlocks = {step: [] for step in steps}        # step -> steps waiting for it

    for first, then in rules:
        waiting_on[then] += 1
        unlocks[first].append(then)

    ready = [step for step in steps if waiting_on[step] == 0]
    heapq.heapify(ready)

    order = []
    while ready:
        step = heapq.heappop(ready)
        order.append(step)
        for next_step in unlocks[step]:
            waiting_on[next_step] -= 1
            if waiting_on[next_step] == 0:
                heapq.heappush(ready, next_step)

    if len(order) != len(steps):
        raise ValueError("the rules go round in a loop")
    return order


# =============================================================================
# 3. CAN A NEW DRIVER FINISH ALL THE TRAINING?
# =============================================================================
# Idea: try to put the modules in order, exactly like problem 2. If every
# module gets a place in the order, the training can be finished. If some are
# stuck waiting on each other, it can't. No alphabetical rule is needed here,
# so a plain list works as well as a heap.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Course Schedule I and II | Pre-requisite Tasks | Topological Sort (C++/Java) (take U forward)
#   https://www.youtube.com/watch?v=WAOfKpxYHR8
#   Same idea as LeetCode 207 Course Schedule. The video uses a different story and
#   different names, so watch for the method, not the details.
def can_finish(modules, prerequisites):
    waiting_on = {module: 0 for module in modules}
    unlocks = {module: [] for module in modules}

    for first, then in prerequisites:
        waiting_on[then] += 1
        unlocks[first].append(then)

    ready = [module for module in modules if waiting_on[module] == 0]
    finished = 0

    while ready:
        module = ready.pop()
        finished += 1
        for next_module in unlocks[module]:
            waiting_on[next_module] -= 1
            if waiting_on[next_module] == 0:
                ready.append(next_module)

    return finished == len(modules)
