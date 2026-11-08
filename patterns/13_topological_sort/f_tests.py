def raises(fn, exc):
    try:
        fn()
    except exc:
        return True
    return False


def test_build_order(m):
    deps = {"app": ["menu", "payments"], "payments": ["db"], "menu": ["db"], "db": []}
    assert m.build_order(deps) == ["db", "menu", "payments", "app"]
    assert m.build_order({"a": ["b"]}) == ["b", "a"]          # b is only mentioned as a need
    assert m.build_order({"z": [], "y": [], "x": []}) == ["x", "y", "z"]
    assert m.build_order({}) == []
    assert raises(lambda: m.build_order({"a": ["b"], "b": ["a"]}), ValueError)
    assert raises(lambda: m.build_order({"a": ["a"]}), ValueError)


STEPS = ["add toppings", "make dough", "make sauce", "proof dough", "stretch dough"]
RULES = [("make dough", "proof dough"),
         ("proof dough", "stretch dough"),
         ("stretch dough", "add toppings"),
         ("make sauce", "add toppings")]


def test_prep_order(m):
    assert m.prep_order(STEPS, RULES) == \
        ["make dough", "make sauce", "proof dough", "stretch dough", "add toppings"]
    assert m.prep_order(["b", "a", "c"], []) == ["a", "b", "c"]
    assert m.prep_order([], []) == []
    assert raises(lambda: m.prep_order(["x", "y"], [("x", "y"), ("y", "x")]), ValueError)


def test_can_finish(m):
    modules = ["safety", "app", "driving", "customer service"]
    assert m.can_finish(modules, [("safety", "driving"), ("app", "driving")]) is True
    assert m.can_finish(modules, []) is True
    assert m.can_finish([], []) is True
    assert m.can_finish(["a", "b"], [("a", "b"), ("b", "a")]) is False
    assert m.can_finish(["a", "b", "c"], [("a", "b"), ("b", "c"), ("c", "a")]) is False
    assert m.can_finish(["a", "b", "c", "d"], [("a", "b"), ("c", "d"), ("d", "c")]) is False
