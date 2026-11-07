def test_find_order(m):
    ids = [101, 104, 108, 115, 120, 133, 140]
    assert m.find_order(ids, 120) == 4
    assert m.find_order(ids, 101) == 0           # first
    assert m.find_order(ids, 140) == 6           # last
    assert m.find_order(ids, 110) == -1          # missing
    assert m.find_order([], 5) == -1
    big = list(range(0, 2_000_000, 2))
    assert m.find_order(big, 1_234_566) == 617_283


def test_first_departure(m):
    times = [5, 12, 12, 20, 31]
    assert m.first_departure(times, 13) == 20
    assert m.first_departure(times, 12) == 12
    assert m.first_departure(times, 0) == 5
    assert m.first_departure(times, 31) == 31
    assert m.first_departure(times, 40) == -1
    assert m.first_departure([], 3) == -1


def test_slowest_speed(m):
    assert m.slowest_speed([3, 6, 7, 11], 8) == 4
    assert m.slowest_speed([30, 11, 23, 4, 20], 5) == 30
    assert m.slowest_speed([30, 11, 23, 4, 20], 6) == 23
    assert m.slowest_speed([1], 1) == 1
    assert m.slowest_speed([10], 10) == 1
