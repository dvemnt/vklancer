## VKLancer ##
*Simple usage [API vk.com](https://vk.com/dev).*  
[![PyPI](http://img.shields.io/pypi/v/vklancer.svg?style=flat)](https://pypi.python.org/pypi/vklancer)

## Installation ##
```pip install vklancer```

## Usage ##
### Simple usage ###
```python
from vklancer import api

vk = api.API('your access token')
response = vk.users.get(user_ids=1)

print(response)

{'response': [{'last_name': 'Дуров', 'id': 1, 'first_name': 'Павел'}]}
```

### With special version API ###
```python
from vklancer import api

vk = api.API('your access token', version='4.0')
response = vk.users.get(user_ids=1)

print(response)

{'response': [{'last_name': 'Дуров', 'id': 1, 'first_name': 'Павел'}]}
```

### Obtain access token ###
```python
from vklancer import api
from vklancer import utils

access_token = utils.oauth('your login', 'your password')

vk = api.API(access_token, version='5.37')
response = vk.users.get(user_ids=1)

print(response)

{'response': [{'last_name': 'Дуров', 'id': 1, 'first_name': 'Павел'}]}
```
