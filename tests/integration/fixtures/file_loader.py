import pytest


@pytest.fixture
def basic_input():
    with open('tests/integration/fixtures/basic.json') as file:
        yield file.read()
