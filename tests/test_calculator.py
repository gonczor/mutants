from pytest import raises, mark

from calculator import calculate


def test_tier_1_discount():
    assert calculate(1, 100) == 100.0


def test_tier_2_discount():
    assert calculate(2, 100) == 90.0


@mark.parametrize("tier", [0, 3])
def test_non_existing_tier(tier: int):
    with raises(ValueError):
        calculate(tier, 100)
