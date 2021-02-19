
import pytest
import requests

# Create your tests here.

IP = '1270.0.1:8000'
URL = 'http:{}/'.format(IP)

TOKEN_DICT = {}


def register_payload(username, password):
    data = {
        'username': username,
        'password': password
    }
    return data


def test_TC1():
    """
    Olga, Nick and Mary register in the application and are ready to access the API
    """
    url = "authentication/register/"

    data = register_payload('olga', 'olga1234')

    res = requests.post(URL + url, data=data)
    TOKEN_DICT['olga'] = res.json()
    print(TOKEN_DICT['olga'])
    assert res.status_code == 200


def test_TC2():
    """
    Olga, Nick and Mary will use the oAuth v2 authorisation service to get their tokens
    """

    pass


def test_TC3():
    """
    Olga makes a call to the API (any endpoint) without using a token.
    This call should be unsuccessful as the user is unauthorised
    """

    pass


def test_TC4():
    """
    Olga adds an item for auction with an expiration time using her token
    """

    pass


def test_TC5():
    """

    """

    pass


def test_TC6():
    """

    """

    pass


def test_TC7():
    """

    """

    pass


def test_TC8():
    """

    """

    pass


def test_TC9():
    """

    """

    pass


def test_TC10():
    """

    """

    pass


def test_TC11():
    """

    """

    pass


def test_TC12():
    """

    """

    pass