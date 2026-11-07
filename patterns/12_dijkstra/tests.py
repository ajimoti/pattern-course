ROADS = [("Shop", "A", 4), ("Shop", "B", 1), ("B", "A", 2), ("A", "C", 5), ("B", "C", 8)]


def test_fastest_route(m):
    assert m.fastest_route(ROADS, "Shop", "C") == (8, ["Shop", "B", "A", "C"])
    assert m.fastest_route(ROADS, "Shop", "A") == (3, ["Shop", "B", "A"])
    assert m.fastest_route(ROADS, "Shop", "Shop") == (0, ["Shop"])
    assert m.fastest_route(ROADS + [("X", "Y", 1)], "Shop", "X") == (-1, [])
    assert m.fastest_route([("Shop", "D", 3), ("Shop", "E", 1), ("E", "D", 5)], "Shop", "D") == (3, ["Shop", "D"])


def test_fastest_times(m):
    assert m.fastest_times(ROADS, "Shop") == {"Shop": 0, "B": 1, "A": 3, "C": 8}
    assert m.fastest_times(ROADS + [("X", "Y", 1)], "Shop") == {"Shop": 0, "B": 1, "A": 3, "C": 8}
    assert m.fastest_times([], "Shop") == {"Shop": 0}
    assert m.fastest_times([("Shop", "A", 2)], "A") == {"A": 0, "Shop": 2}


LINKS = [("HQ", "Leeds", 2), ("HQ", "York", 5), ("Leeds", "York", 1), ("York", "Hull", 3)]
SHOPS = ["HQ", "Leeds", "York", "Hull"]


def test_everyone_has_message(m):
    assert m.everyone_has_message(LINKS, SHOPS, "HQ") == 6
    assert m.everyone_has_message(LINKS, SHOPS + ["Bath"], "HQ") == -1
    assert m.everyone_has_message(LINKS, SHOPS, "Leeds") == -1        # links only go one way
    assert m.everyone_has_message([], ["HQ"], "HQ") == 0
    assert m.everyone_has_message(LINKS + [("HQ", "Hull", 4)], SHOPS, "HQ") == 4
