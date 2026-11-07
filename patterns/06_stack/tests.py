def test_is_balanced(m):
    assert m.is_balanced("(extra cheese [no onions]) {ring bell}") is True
    assert m.is_balanced("(extra cheese") is False
    assert m.is_balanced("no onions)") is False
    assert m.is_balanced("[well done)") is False
    assert m.is_balanced("([)]") is False
    assert m.is_balanced("no brackets at all") is True
    assert m.is_balanced("") is True


def test_final_order(m):
    actions = ["add margherita", "add pepperoni", "add hawaiian",
               "undo", "add veggie", "undo", "undo"]
    assert m.final_order(actions) == ["margherita"]
    assert m.final_order(["undo", "add margherita"]) == ["margherita"]     # undo on empty
    assert m.final_order(["add bbq chicken", "add four cheese"]) == ["bbq chicken", "four cheese"]
    assert m.final_order(["add margherita", "undo", "undo"]) == []
    assert m.final_order([]) == []


def test_days_until_busier(m):
    assert m.days_until_busier([30, 25, 40, 35, 50]) == [2, 1, 2, 1, 0]
    assert m.days_until_busier([50, 40, 30]) == [0, 0, 0]                  # only gets quieter
    assert m.days_until_busier([10, 10, 20]) == [2, 1, 0]                  # equal is not busier
    assert m.days_until_busier([5]) == [0]
    assert m.days_until_busier([]) == []
    big = list(range(5000, 0, -1)) + [99999]
    assert m.days_until_busier(big)[0] == 5000                             # a longer list
