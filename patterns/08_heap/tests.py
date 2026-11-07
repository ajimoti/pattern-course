def test_dispatch(m):
    assert m.dispatch([(101, 0), (102, 2), (103, 3), (104, 10)], 2, 6) == \
        {101: 0, 102: 2, 103: 6, 104: 10}
    assert m.dispatch([(1, 0), (2, 0), (3, 0)], 1, 5) == {1: 0, 2: 5, 3: 10}
    assert m.dispatch([(1, 0), (2, 0), (3, 0)], 3, 5) == {1: 0, 2: 0, 3: 0}
    assert m.dispatch([], 3, 5) == {}


def test_closest_customers(m):
    customers = [("Amara", 4.5), ("Ben", 1.2), ("Chloe", 3.0), ("Dev", 1.2), ("Esi", 7.1)]
    assert m.closest_customers(customers, 3) == ["Ben", "Dev", "Chloe"]
    assert m.closest_customers(customers, 1) == ["Ben"]
    assert m.closest_customers(customers, 10) == ["Ben", "Dev", "Chloe", "Amara", "Esi"]
    assert m.closest_customers(customers, 0) == []
    assert m.closest_customers([], 2) == []


def test_merge_order_lists(m):
    assert m.merge_order_lists([[1, 5, 9], [2, 3, 10], [4]]) == [1, 2, 3, 4, 5, 9, 10]
    assert m.merge_order_lists([[], [1, 2], []]) == [1, 2]
    assert m.merge_order_lists([[1, 1], [1]]) == [1, 1, 1]
    assert m.merge_order_lists([]) == []
    assert m.merge_order_lists([[3, 4]]) == [3, 4]
