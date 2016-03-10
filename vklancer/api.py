# coding=utf-8

import requests

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode


class API(object):

    """Wrapper for vk.com API."""

    def __init__(self, token=None, version='5.49', **kwargs):
        """
        Override __init__.

        :param token (optional): `str` OAuth2 access token.
        :param version (optional): `str` API version.
        """
        self.__token = token
        self.__version = version
        self.__method = kwargs.get('method', '')

    def get_url(self, method=None, **kwargs):
        """Return url for call method.

        :param method (optional): `str` method name.
        :returns: `str` URL.
        """
        kwargs.setdefault('v', self.__version)

        if self.__token is not None:
            kwargs.setdefault('access_token', self.__token)

        return 'https://api.vk.com/method/{}?{}'.format(
            method or self.__method, urlencode(kwargs)
        )

    def request(self, method, **kwargs):
        """
        Send request to API.

        :param method: `str` method name.
        :returns: `dict` response.
        """
        kwargs.setdefault('v', self.__version)

        if self.__token is not None:
            kwargs.setdefault('access_token', self.__token)

        return requests.get(self.get_url(method, **kwargs)).json()

    def __getattr__(self, attr):
        """Override __getattr__."""
        method = ('{}.{}'.format(self.__method, attr)).lstrip('.')
        return API(self.__token, version=self.__version, method=method)

    def __call__(self, **kwargs):
        """Override __call__."""
        return self.request(self.__method, **kwargs)
