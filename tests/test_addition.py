from cal import addtion




def test_add_positive_numbers():
    assert addtion(10, 5) == 15


def test_add_negative_numbers():
    assert addtion(-10, -5) == -15


def test_add_positive_and_negative_numbers():
    assert addtion(10, -5) == 5


def test_add_zero():
    assert addtion(10, 0) == 10


def test_add_decimal_numbers():
    assert addtion(10.5, 5.5) == 16.0


def test_add_two_zero_values():
    assert addtion(0, 0) == 0