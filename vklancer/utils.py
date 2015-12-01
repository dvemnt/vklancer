# coding=utf-8

import re

import requests


def authentication(login, password):
    """
    Authentication on vk.com.

    :param login: login on vk.com.
    :param password: password on vk.com.
    :returns: `requests.Session` session with cookies.
    """
    session = requests.Session()
    response = session.get('https://m.vk.com')
    url = re.search(r'action="([^\"]+)"', response.text).group(1)
    data = {'email': login, 'pass': password}
    response = session.post(url, data=data)
    return session


def oauth(login, password, app_id=4729418, scope=2097151):
    """
    OAuth on vk.com.

    :param login: login on vk.com.
    :param password: password on vk.com.
    :param app_id: vk.com application id (default: 4729418).
    :param scope: allowed actions (default: 2097151 (all)).
    :returns: OAuth2 access token or None.
    """
    session = authentication(login, password)
    data = {
        'response_type': 'token',
        'client_id': app_id,
        'scope': scope,
        'display': 'mobile',
    }
    response = session.post('https://oauth.vk.com/authorize', data=data)

    if 'access_token' not in response.url:
        url = re.search(r'action="([^\"]+)"', response.text).group(1)
        response = session.get(url)

    try:
        return re.search(r'access_token=([^\&]+)', response.url).group(1)
    except:
        return None
