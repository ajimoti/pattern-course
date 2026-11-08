def test_min_ovens(m):
    assert m.min_ovens([(0, 10), (5, 15), (10, 20), (12, 14)]) == 3
    assert m.min_ovens([(0, 5), (5, 10), (10, 15)]) == 1        # back to back
    assert m.min_ovens([(0, 10), (0, 10), (0, 10)]) == 3        # all at once
    assert m.min_ovens([(3, 4)]) == 1
    assert m.min_ovens([]) == 0


def test_merge_shifts(m):
    assert m.merge_shifts([(16, 18), (9, 12), (18, 20), (11, 14)]) == [(9, 14), (16, 20)]
    assert m.merge_shifts([(9, 17), (10, 12)]) == [(9, 17)]       # one inside another
    assert m.merge_shifts([(1, 2), (3, 4)]) == [(1, 2), (3, 4)]   # no overlap
    assert m.merge_shifts([(5, 6)]) == [(5, 6)]
    assert m.merge_shifts([]) == []


def test_can_one_driver(m):
    assert m.can_one_driver([(25, 30), (0, 10), (10, 20)]) is True
    assert m.can_one_driver([(0, 10), (5, 15)]) is False
    assert m.can_one_driver([(20, 30), (0, 25)]) is False         # clash only visible after sorting
    assert m.can_one_driver([(4, 9)]) is True
    assert m.can_one_driver([]) is True
