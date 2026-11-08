"""Tests for pattern 01. Run from the pattern_course folder: python3 practice.py 1"""


def test_late_orders_fast(m):
    orders = [{"id": i, "promised": 30} for i in range(1, 6)]
    deliveries = [{"order_id": 1, "minutes": 25}, {"order_id": 2, "minutes": 40},
                  {"order_id": 4, "minutes": 31}, {"order_id": 5, "minutes": 30}]
    assert m.late_orders_fast(orders, deliveries) == [2, 4]
    # different promises: must use each order's own promise, not 30
    assert m.late_orders_fast([{"id": 7, "promised": 45}, {"id": 8, "promised": 20}],
                              [{"order_id": 7, "minutes": 40}, {"order_id": 8, "minutes": 25}]) == [8]
    assert m.late_orders_fast([], []) == []
    assert m.late_orders_fast(orders, []) == []
    # 20,000 orders: the slow version would take far too long
    big_o = [{"id": i, "promised": 30} for i in range(20000)]
    big_d = [{"order_id": i, "minutes": 31 if i % 2 else 10} for i in range(20000)]
    assert len(m.late_orders_fast(big_o, big_d)) == 10000


def test_unpaid_orders(m):
    orders = [{"id": 101, "total": 18.50}, {"id": 102, "total": 12.00},
              {"id": 103, "total": 25.00}, {"id": 104, "total": 9.50}]
    payments = [{"order_id": 103, "amount": 25.00}, {"order_id": 101, "amount": 18.50}]
    assert m.unpaid_orders(orders, payments) == [102, 104]
    assert m.unpaid_orders(orders, []) == [101, 102, 103, 104]
    all_paid = [{"order_id": o["id"], "amount": o["total"]} for o in orders]
    assert m.unpaid_orders(orders, all_paid) == []
    assert m.unpaid_orders([], payments) == []
    big_o = [{"id": i, "total": 10} for i in range(20000)]
    big_p = [{"order_id": i, "amount": 10} for i in range(0, 20000, 2)]
    assert len(m.unpaid_orders(big_o, big_p)) == 10000


def test_voucher_pair(m):
    assert m.voucher_pair([12, 7, 15, 3, 13], 20) == (1, 4)
    assert m.voucher_pair([10, 10], 20) == (0, 1)
    assert m.voucher_pair([10], 20) is None           # can't pair an order with itself
    assert m.voucher_pair([], 20) is None
    assert m.voucher_pair([5, 6, 7], 20) is None
    assert m.voucher_pair([2, 18, 8, 12], 20) == (0, 1)   # earliest completed pair
    big = list(range(1, 30001))
    assert m.voucher_pair(big, 59999) == (29998, 29999)
