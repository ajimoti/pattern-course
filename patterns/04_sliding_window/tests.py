"""Tests for pattern 04. Run from the pattern_course folder: python3 practice.py 4"""


def test_best_run(m):
    revenue = [120, 80, 200, 150, 90, 300]
    assert m.best_run(revenue, 3) == (3, 540)
    assert m.best_run(revenue, 1) == (5, 300)
    assert m.best_run(revenue, 6) == (0, 940)
    assert m.best_run(revenue, 7) is None
    assert m.best_run(revenue, 0) is None
    assert m.best_run([], 2) is None
    assert m.best_run([50, 50, 50, 50], 2) == (0, 100)        # tie: keep the earliest
    big = list(range(200000))
    assert m.best_run(big, 1000) == (199000, sum(range(199000, 200000)))


def test_count_good_stretches(m):
    revenue = [120, 80, 200, 150, 90, 300]
    assert m.count_good_stretches(revenue, 3, 435) == 2
    assert m.count_good_stretches(revenue, 3, 400) == 4     # first stretch counts too
    assert m.count_good_stretches(revenue, 3, 1000) == 0
    assert m.count_good_stretches(revenue, 7, 10) == 0
    assert m.count_good_stretches([], 1, 0) == 0
    assert m.count_good_stretches([5, 5], 1, 5) == 2


def test_longest_stretch(m):
    d = ["O", "L", "O", "O", "L", "L", "O"]
    assert m.longest_stretch(d, 1) == 4
    assert m.longest_stretch(d, 2) == 5
    assert m.longest_stretch(d, 0) == 2
    assert m.longest_stretch(d, 10) == 7
    assert m.longest_stretch([], 1) == 0
    assert m.longest_stretch(["L", "L"], 0) == 0
    assert m.longest_stretch(["O", "O", "O"], 0) == 3
