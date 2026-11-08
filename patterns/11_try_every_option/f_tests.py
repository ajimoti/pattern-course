import math


def test_read_points(m):
    assert m.read_points("0,0 1,1 2,0 2,2") == [(0, 0), (1, 1), (2, 0), (2, 2)]
    assert m.read_points("10,5 -3,4") == [(10, 5), (-3, 4)]
    assert m.read_points("7,7") == [(7, 7)]


def test_trip_length(m):
    assert round(m.trip_length([(0, 0), (1, 1), (2, 2), (2, 0), (0, 0)]), 2) == 6.83
    assert m.trip_length([(0, 0), (3, 4)]) == 5
    assert m.trip_length([(0, 0)]) == 0


def test_best_route(m):
    route, distance = m.best_route([(0, 0), (1, 1), (2, 0), (2, 2)])
    best = [(0, 0), (1, 1), (2, 2), (2, 0), (0, 0)]
    assert route in (best, best[::-1])
    assert round(distance, 2) == 6.83

    route, distance = m.best_route([(0, 0), (10, 5), (-3, 4)])
    assert round(distance, 2) == 29.22
    assert route[0] == route[-1] == (0, 0) and len(route) == 4

    assert m.best_route([(5, 5)]) == ([(5, 5), (5, 5)], 0)

    # a straight line: out to the far end and back
    route, distance = m.best_route([(0, 0), (3, 0), (1, 0), (2, 0)])
    assert distance == 6


def as_set(choices):
    return sorted(tuple(c) for c in choices)


def test_topping_choices(m):
    toppings = ["ham", "mushroom", "olive", "pepper"]
    assert as_set(m.topping_choices(toppings, 2)) == as_set([
        ("ham", "mushroom"), ("ham", "olive"), ("ham", "pepper"),
        ("mushroom", "olive"), ("mushroom", "pepper"), ("olive", "pepper"),
    ])
    assert len(m.topping_choices(toppings, 3)) == 4
    assert as_set(m.topping_choices(toppings, 4)) == [("ham", "mushroom", "olive", "pepper")]
    assert as_set(m.topping_choices(toppings, 0)) == [()]
    assert m.topping_choices(toppings, 5) == []


def check_fill(m, orders, capacity, expected_size):
    result = m.fill_the_van(orders, capacity)
    sizes = dict(orders)
    assert result is not None
    assert len(set(result)) == len(result)                 # no order used twice
    assert all(name in sizes for name in result)
    assert sum(sizes[name] for name in result) == capacity
    assert len(result) == expected_size


def test_fill_the_van(m):
    orders = [("a", 3), ("b", 5), ("c", 2), ("d", 4)]
    check_fill(m, orders, 9, 2)                            # b + d
    check_fill(m, orders, 14, 4)                           # every order
    check_fill(m, orders, 5, 1)                            # just b
    assert m.fill_the_van(orders, 1) is None
    assert m.fill_the_van(orders, 15) is None
    assert m.fill_the_van(orders, 0) == []
    assert m.fill_the_van([], 3) is None
