## VKLancer ##
*Simple usage [API vk.com](https://vk.com/dev).*

[![Build Status](https://travis-ci.org/pyvim/vklancer.svg)](https://travis-ci.org/pyvim/vklancer)
[![Coverage Status](https://coveralls.io/repos/pyvim/vklancer/badge.svg?branch=master&service=github)](https://coveralls.io/github/pyvim/vklancer?branch=master)
[![PyPI](http://img.shields.io/pypi/v/vklancer.svg?style=flat)](https://pypi.python.org/pypi/vklancer)

## Installation ##
```pip install vklancer```

## Usage ##
List of methods: [https://vk.com/dev/methods](https://vk.com/dev/methods)

### Simple usage ###
```python
from vklancer import api

vk = api.API()
response = vk.users.get(user_ids=1)

print(response)

>>> {'response': [{'last_name': 'Дуров', 'id': 1, 'first_name': 'Павел'}]}
```

### With request method ###
```python
from vklancer import api

vk = api.API()
response = vk.request('users.get', user_ids=1)

print(response)

>>> {'response': [{'last_name': 'Дуров', 'id': 1, 'first_name': 'Павел'}]}
```

### Get method call URL ###
```python
from vklancer import api

vk = api.API()
url = vk.get_url('users.get', user_ids=1)

print(url)

>>> https://api.vk.com/method/users.get?user_ids=1&v=5.49
```

### With special version API ###
```python
from vklancer import api

vk = api.API(token='your access token', version='4.0')
response = vk.users.get(user_ids=1)

print(response)

>>> {'response': [{'last_name': 'Дуров', 'id': 1, 'first_name': 'Павел'}]}
```

### Obtain access token ###
```python
from vklancer import api
from vklancer import utils

access_token = utils.oauth('your login', 'your password')

vk = api.API(token=access_token, version='5.37')
response = vk.users.get(user_ids=1)

print(response)

>>> {'response': [{'last_name': 'Дуров', 'id': 1, 'first_name': 'Павел'}]}
```

## Documentation ##
In development. See docstrings.

## Tests ##
```bash
nosetests
```
or
```bash
python tests.py
```

## Changelog ##
See [CHANGELOG.md](https://github.com/pyvim/vklancer/blob/master/CHANGELOG.md)

## License ##
See [LICENSE](https://github.com/pyvim/vklancer/blob/master/LICENSE)
