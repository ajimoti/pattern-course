"""Tests for pattern 02. Run from the pattern_course folder: python3 practice.py 2"""


def test_trending(m):
    ev = [(0, "margherita"), (30, "pepperoni"), (70, "pepperoni"),
          (80, "hawaiian"), (85, "hawaiian"), (90, "margherita")]
    assert m.trending(ev, 90, 2) == ["hawaiian", "margherita"]
    assert m.trending(ev, 90, 10) == ["hawaiian", "margherita", "pepperoni"]
    assert m.trending(ev, 500, 3) == []                       # everything too old
    assert m.trending([], 90, 3) == []
    assert m.trending([(10, "veggie"), (20, "bbq"), (30, "veggie")], 40, 1) == ["veggie"]


def test_first_one_time_customer(m):
    assert m.first_one_time_customer(["ada", "ben", "ada", "cy", "ben", "dee"]) == "cy"
    assert m.first_one_time_customer(["ada", "ada"]) is None
    assert m.first_one_time_customer([]) is None
    assert m.first_one_time_customer(["zoe"]) == "zoe"
    assert m.first_one_time_customer(["ben", "ada", "ben"]) == "ada"


def test_group_same_toppings(m):
    orders = [(1, ["ham", "pineapple"]), (2, ["pepperoni"]), (3, ["pineapple", "ham"]),
              (4, ["pepperoni"]), (5, ["mushroom", "olive"])]
    assert m.group_same_toppings(orders) == [[1, 3], [2, 4], [5]]
    assert m.group_same_toppings([]) == []
    assert m.group_same_toppings([(9, ["cheese"])]) == [[9]]
    # plain cheese (no toppings) is its own group
    assert m.group_same_toppings([(1, []), (2, ["olive"]), (3, [])]) == [[1, 3], [2]]
