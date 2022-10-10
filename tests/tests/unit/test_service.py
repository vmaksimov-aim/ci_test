import pytest


async def af(aaa, bbbb):
    return aaa + bbbb


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'aaa, bbbb, ccc',
    [(1, 1, 2), (2, 2, 4)],
)
async def test_get_estimated_driving_range(aaa, bbbb, ccc):
    assert ccc == await af(aaa, bbbb)
