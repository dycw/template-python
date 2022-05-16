from dycw_template import negate


def test_negate() -> None:
    assert negate(True) is False
