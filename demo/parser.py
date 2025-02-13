def parse(s):
    n = 0
    fraction = 1.0
    decimal = False
    for c in s:
        if c == ".":
            decimal = True
            continue
        if decimal:
            fraction /= 10.0  # fraction = fraction / 10.0
            n = n + (ord(c) - ord("0")) * fraction
        else:
            n = n * 10 + ord(c) - ord("0")
    return n


def test_parse_single_digits():
    assert parse("2") == 2
    assert parse("3") == 3
    assert parse("5") == 5
    assert parse("9") == 9


def test_parse_multiple_digits():
    assert parse("22") == 22
    assert parse("345") == 345


def test_parse_decimal_numbers():
    assert parse("22.234") == 22.234
    assert parse("345.6") == 345.6
    try:
        assert parse("345......6") == 345.6
        raise Exception("Should have seen a decimal error")
    except:
        pass
