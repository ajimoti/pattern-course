MINI = {"name": "Mini pack", "pizzas": 3, "contains": []}
KIDS = {"name": "Kids box", "pizzas": 1, "contains": []}
PARTY = {"name": "Party add-on", "pizzas": 1, "contains": [MINI]}
FAMILY = {"name": "Family deal", "pizzas": 2, "contains": [KIDS, PARTY]}


def test_total_pizzas(m):
    assert m.total_pizzas(FAMILY) == 7
    assert m.total_pizzas(PARTY) == 4
    assert m.total_pizzas(KIDS) == 1
    empty = {"name": "Sides only", "pizzas": 0, "contains": []}
    assert m.total_pizzas(empty) == 0
    deep = {"name": "L1", "pizzas": 1, "contains": [
        {"name": "L2", "pizzas": 1, "contains": [
            {"name": "L3", "pizzas": 1, "contains": [
                {"name": "L4", "pizzas": 5, "contains": []}]}]}]}
    assert m.total_pizzas(deep) == 8


ROADS = {
    "Shop": ["A", "B"],
    "A": ["C"],
    "B": ["A", "C"],
    "C": [],
}


def test_count_routes(m):
    assert m.count_routes(ROADS, "Shop", "C") == 3
    assert m.count_routes(ROADS, "A", "C") == 1
    assert m.count_routes(ROADS, "C", "Shop") == 0
    assert m.count_routes(ROADS, "Shop", "Shop") == 1
    no_end_key = {"Shop": ["A", "B"], "A": ["D"], "B": ["D"]}   # "D" isn't a key
    assert m.count_routes(no_end_key, "Shop", "D") == 2


def test_count_neighbourhoods(m):
    assert m.count_neighbourhoods(["..#.", ".##.", "#..#"]) == 3
    assert m.count_neighbourhoods(["...", "...", "..."]) == 1
    assert m.count_neighbourhoods(["###", "###"]) == 0
    assert m.count_neighbourhoods([]) == 0
    assert m.count_neighbourhoods([".#.#."]) == 3
    assert m.count_neighbourhoods([".#", "#."]) == 2     # diagonals don't connect
