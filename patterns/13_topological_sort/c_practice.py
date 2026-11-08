"""
PATTERN 13: ORDER THINGS THAT DEPEND ON EACH OTHER - PRACTICE
Read a_lesson.md first. Then write your code where it says `pass`.
Test your answers:   python practice.py 13
"""
import heapq


# =============================================================================
# 1. WHAT ORDER SHOULD WE BUILD THE APP IN?   (the lesson's worked example)
# =============================================================================
# THE PROBLEM
#   The pizza app is split into a few parts, and some of them can't be built
#   until others are done. The menu needs the database, for example, so the
#   database has to be built first.
#
#   Work out an order to build everything in. When more than one part is
#   ready at the same time, build them in alphabetical order, so the answer
#   is always the same. If two parts each need the other, there's no way to
#   build them, so raise an error.
#
# THE DATA
#   deps = {"app":      ["menu", "payments"],
#           "payments": ["db"],
#           "menu":     ["db"],
#           "db":       []}
#   Each key is a part. Its list is the parts it needs built first.
#
# YOUR TASK
#   build_order(deps) returns a list of parts in build order.
#   A part might only appear inside a list (not as a key). It still needs building.
#   Raise ValueError if the parts depend on each other in a loop.
#
# EXAMPLE
#   db needs nothing                         -> build db
#   menu and payments were only waiting for db, so both are ready.
#   Alphabetical: menu first                 -> build menu
#                                            -> build payments
#   app was waiting for menu and payments    -> build app
#
#   build_order(deps)                        ->  ["db", "menu", "payments", "app"]
#   build_order({"a": ["b"], "b": ["a"]})    ->  raises ValueError
#
# HINT
#   For each part, count how many parts it is still waiting for.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Course Schedule I and II | Pre-requisite Tasks | Topological Sort (C++/Java) (take U forward)
#   https://www.youtube.com/watch?v=WAOfKpxYHR8
#   Same idea as LeetCode 210 Course Schedule II. The video uses a different story and
#   different names, so watch for the method, not the details.
def build_order(deps):
    pass


# =============================================================================
# 2. THE ORDER TO DO THE KITCHEN PREP
# =============================================================================
# THE PROBLEM
#   Every morning the kitchen has a list of prep jobs to get through before
#   opening. Some jobs have to wait for others. You can't stretch the dough
#   until it has proofed, and you can't add the toppings until the dough is
#   stretched and the sauce is made.
#
#   Write out the order the jobs should be done in. If more than one job could
#   be done next, pick them in alphabetical order. If the rules can't all be
#   followed, raise an error.
#
# THE DATA
#   steps = ["add toppings", "make dough", "make sauce", "proof dough", "stretch dough"]
#   rules = [("make dough",    "proof dough"),
#            ("proof dough",   "stretch dough"),
#            ("stretch dough", "add toppings"),
#            ("make sauce",    "add toppings")]
#   Each rule is (do this first, then this).
#
# YOUR TASK
#   prep_order(steps, rules) returns the list of steps in order.
#   Raise ValueError if the rules go round in a loop.
#
# EXAMPLE
#   Ready at the start: "make dough", "make sauce".   Alphabetical: make dough.
#   That makes "proof dough" ready.  Ready: "make sauce", "proof dough".
#   Alphabetical: make sauce, then proof dough.
#   That makes "stretch dough" ready, then "add toppings".
#
#   prep_order(steps, rules)  ->
#       ["make dough", "make sauce", "proof dough", "stretch dough", "add toppings"]
#
# HINT
#   Same method as problem 1. Only the shape of the input is different.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Kahn's Algorithm | Topological Sort Algorithm | BFS (take U forward)
#   https://www.youtube.com/watch?v=73sneFXuTEg
#   Same idea as LeetCode Topological sort walkthrough. The video uses a different story and
#   different names, so watch for the method, not the details.
def prep_order(steps, rules):
    pass


# =============================================================================
# 3. CAN A NEW DRIVER FINISH ALL THE TRAINING?
# =============================================================================
# THE PROBLEM
#   New drivers go through a set of training modules before their first shift.
#   Some modules can only be started once another one is finished. Someone in
#   head office has been editing the rules, and you're worried they've made a
#   loop, where two modules each need the other to be done first. If that has
#   happened, no new driver could ever finish their training.
#
#   Check the rules and say whether it's possible to finish every module.
#
# THE DATA
#   modules = ["safety", "app", "driving", "customer service"]
#   prerequisites = [("safety", "driving"), ("app", "driving")]
#   Each pair is (finish this first, before starting this).
#
# YOUR TASK
#   can_finish(modules, prerequisites) returns True if every module can be
#   finished, and False if some are stuck waiting on each other.
#
# EXAMPLE
#   safety, app and customer service need nothing, so do them.
#   driving was waiting for safety and app, both done, so do driving.
#   All 4 done  ->  True
#
#   can_finish(["a", "b"], [("a", "b"), ("b", "a")])  ->  False
#       (a needs b first, b needs a first, so neither can start)
#
# HINT
#   Try to put them in order like problem 2, and count how many you manage.
#
# VIDEO (watch after you've had a real go, about 20-30 minutes)
#   Course Schedule I and II | Pre-requisite Tasks | Topological Sort (C++/Java) (take U forward)
#   https://www.youtube.com/watch?v=WAOfKpxYHR8
#   Same idea as LeetCode 207 Course Schedule. The video uses a different story and
#   different names, so watch for the method, not the details.
def can_finish(modules, prerequisites):
    pass
