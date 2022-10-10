import pytest


async def af(a, b):
    return a + b


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'a, b, c',
    [(1, 1, 2), (2, 2, 4)],
)
async def test_get_estimated_driving_range(a, b, c):
    assert c == await af(a, b)
