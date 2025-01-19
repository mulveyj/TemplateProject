from src.app import healthcheck, dogs
import pytest


@pytest.mark.describe("Healthcheck tests")
@pytest.mark.it("The healthcheck gives a healthcheck message")
def test_healthcheck():
    assert healthcheck() == {"message": "Application is healthy"}


@pytest.mark.describe("Dogs endpoint")
@pytest.mark.it("Returns some dogs")
def test_dogs():
    result = dogs()
    expected = {
        "dogs": [
            {"name": "fido", "good_doggo": True},
            {"name": "gnasher", "good_doggo": False},
        ]
    }
    assert result == expected
