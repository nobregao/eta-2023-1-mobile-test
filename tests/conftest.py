import pytest

from page.HomePage import HomePage


@pytest.fixture
def home_page():
    home_page = HomePage()
    home_page.set_up()

    yield home_page

    home_page.teardown()
