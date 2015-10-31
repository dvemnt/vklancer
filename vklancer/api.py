# coding=utf-8

__author__ = 'Vitalii Maslov'
__version__ = '1.2.2'
__email__ = 'me@pyvim.com'
__license__ = 'MIT'

import requests


class API(object):

    """Wrapper for vk.com API."""

    def __init__(self, token, version='5.37', **kwargs):
        """
        Initialize class.

        :param token: OAuth2 access token.
        :param version: API version.
        :param method: method name.
        """
        self._token = token
        self._version = version
        self._method = kwargs.get('method', '')

    def _request(self, **kwargs):
        """
        Send request to API.

        :param method: name of API method.
        :param params: method parameters.
        :returns: answer in dictionary.
        """
        url = 'https://api.vk.com/method/%s' % self._method
        data = {
            'access_token': self._token,
            'v': self._version
        }
        data.update(kwargs)
        return requests.post(url, data=data).json()

    def __getattr__(self, attr):
        try:
            return self.__dict__[attr]
        except KeyError:
            method = ('{}.{}'.format(self._method, attr)).lstrip('.')
            return API(self._token, version=self._version, method=method)

    def __call__(self, **kwargs):
        return self._request(**kwargs)
