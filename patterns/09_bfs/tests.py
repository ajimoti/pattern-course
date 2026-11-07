GRID = ["S.#C",
        ".##.",
        "...C"]


def test_build_graph(m):
    graph = m.build_graph(GRID)
    assert graph[(1, 0)] == [(0, 0), (2, 0)]
    assert graph[(0, 0)] == [(1, 0), (0, 1)]
    assert graph[(0, 1)] == [(0, 0)]
    assert (1, 1) not in graph                       # buildings get no entry
    assert len(graph) == 9
    assert m.build_graph(["S"]) == {(0, 0): []}


def test_nearest_customer(m):
    assert m.nearest_customer(GRID) == 5
    assert m.nearest_customer(["S#C"]) == -1         # blocked
    assert m.nearest_customer(["SC"]) == 1           # next door
    assert m.nearest_customer(["S..", "...", "..."]) == -1   # no customers at all
    assert m.nearest_customer(["C..", "...", "..S"]) == 4


LINKS = {
    "Ada": ["Ben", "Cara"],
    "Ben": ["Ada", "Dev"],
    "Cara": ["Ada"],
    "Dev": ["Ben", "Esi"],
    "Esi": ["Dev"],
    "Femi": [],
}


def test_referral_steps(m):
    assert m.referral_steps(LINKS, "Ada", "Esi") == 3
    assert m.referral_steps(LINKS, "Ada", "Cara") == 1
    assert m.referral_steps(LINKS, "Ada", "Ada") == 0
    assert m.referral_steps(LINKS, "Ada", "Femi") == -1
    assert m.referral_steps(LINKS, "Cara", "Esi") == 4


CALLS = {
    "Central": ["North", "East"],
    "North": ["Central", "West"],
    "East": ["Central"],
    "West": ["North"],
}


def test_minutes_until_everyone_knows(m):
    assert m.minutes_until_everyone_knows(CALLS, "Central") == 2
    assert m.minutes_until_everyone_knows(CALLS, "West") == 3
    assert m.minutes_until_everyone_knows({"Central": []}, "Central") == 0
    with_south = dict(CALLS, South=[])
    assert m.minutes_until_everyone_knows(with_south, "Central") == -1
    one_way = {"A": ["B"], "B": ["C"], "C": []}
    assert m.minutes_until_everyone_knows(one_way, "A") == 2
    assert m.minutes_until_everyone_knows(one_way, "B") == -1   # nobody calls A
