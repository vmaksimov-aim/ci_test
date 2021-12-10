import pytest


@pytest.mark.parametrize(
    'a, b',
    [(1, 1), (2, 2)],
)
def test_get_estimated_driving_range(a, b):
    assert a == b
