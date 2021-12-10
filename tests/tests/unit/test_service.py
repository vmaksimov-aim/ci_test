import pytest

from project.integration import service


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'a, b, c',
    [(1, 1, 2), (2, 2, 4)],
)
def test_get_estimated_driving_range(a, b, c):
    assert c == service.a(a, b)
