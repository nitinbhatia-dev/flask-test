from unittest import mock
from urllib import request
from app.app import readapi
import pytest

@pytest.fixture
def client():
    """Configures the app for testing
    Sets app config variable ``TESTING`` to ``True``
    :return: App for testing
    """

    #app.config['TESTING'] = True
    client = readapi.app.test_client()

    yield client


def test_landing_aliases(client):
    print(client.get("/").data)
    assert client.get("/").data.decode('UTF-8') == "hello flask"
    
