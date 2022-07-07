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
    #readapi.app.test_request_context

    yield client

@mock.patch('readapi.dummyFuncForMock')
def mockDummyFunction():
    return "2"


def test_landing_aliases(client):
    #print(client.get("/read").data)
    with mock.patch('app.app.readapi.dummyFuncForMock') as mock_method:
            mock_method.return_value = "2"
            assert client.get("/read").data.decode('UTF-8') == "hello read api 2"
            mock_method.assert_called_once()

    
    
    
    
