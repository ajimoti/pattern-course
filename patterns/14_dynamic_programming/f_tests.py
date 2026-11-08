def test_fewest_boxes(m):
    assert m.fewest_boxes(8, [1, 4, 6]) == 2          # 4 + 4, not 6 + 1 + 1
    assert m.fewest_boxes(12, [4, 6]) == 2
    assert m.fewest_boxes(10, [4, 6]) == 2
    assert m.fewest_boxes(7, [4, 6]) == -1
    assert m.fewest_boxes(0, [4, 6]) == 0
    assert m.fewest_boxes(11, [2, 5]) == 4            # 5 + 2 + 2 + 2


def test_most_tips(m):
    assert m.most_tips([2, 7, 9, 3, 1]) == 12         # houses 0, 2 and 4
    assert m.most_tips([1, 2, 3, 1]) == 4
    assert m.most_tips([2, 1, 1, 2]) == 4
    assert m.most_tips([5]) == 5
    assert m.most_tips([5, 1]) == 5
    assert m.most_tips([]) == 0


def test_ways_to_pack(m):
    assert m.ways_to_pack(5, [1, 2, 5]) == 4
    assert m.ways_to_pack(4, [1, 2]) == 3
    assert m.ways_to_pack(3, [2]) == 0
    assert m.ways_to_pack(10, [10]) == 1
    assert m.ways_to_pack(0, [1, 2]) == 1
