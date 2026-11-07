"""Tests for pattern 03. Run from the pattern_course folder: python3 practice.py 3"""


def test_two_prices(m):
    assert m.two_prices([4, 6, 9, 11, 15], 20) == (9, 11)
    assert m.two_prices([5, 5], 10) == (5, 5)            # two pizzas, same price
    assert m.two_prices([10], 20) is None                # can't buy one pizza twice
    assert m.two_prices([], 20) is None
    assert m.two_prices([1, 2, 3], 100) is None
    assert m.two_prices([2, 7, 11, 15], 9) == (2, 7)


def test_is_mirror_code(m):
    assert m.is_mirror_code("Xy1yX") is True
    assert m.is_mirror_code("AB12BA") is False
    assert m.is_mirror_code("") is True
    assert m.is_mirror_code("Q") is True
    assert m.is_mirror_code("abBA") is True              # case doesn't matter
    assert m.is_mirror_code("ab") is False


def test_merge_orders(m):
    assert m.merge_orders([5, 12, 30], [8, 12, 40, 41]) == [5, 8, 12, 12, 30, 40, 41]
    assert m.merge_orders([], [1, 2]) == [1, 2]
    assert m.merge_orders([3, 4], []) == [3, 4]
    assert m.merge_orders([], []) == []
    assert m.merge_orders([1, 2, 3], [10, 20]) == [1, 2, 3, 10, 20]
    a = [5, 6]
    m.merge_orders(a, [1])
    assert a == [5, 6]                                   # don't change the input lists
