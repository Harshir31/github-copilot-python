import pytest

from app import CURRENT, app


@pytest.fixture
def client():
    app.config.update(TESTING=True)
    CURRENT.update(puzzle=None, solution=None)
    with app.test_client() as test_client:
        yield test_client
    CURRENT.update(puzzle=None, solution=None)
