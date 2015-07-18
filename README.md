VKLancer
========
[![PyPI](http://img.shields.io/pypi/v/vklancer.svg?style=flat)](https://pypi.python.org/pypi/vklancer)

*Simple usage [API vk.com](https://vk.com/dev).<br/>*

Usage
-----
```python
import vklancer

api = vklancer.API(token='token', version='5.34')
answer = api.users.get(user_ids=1)

```

Installation
------------
```pip install vklancer```

Requirements
------------
- [requests](https://github.com/kennethreitz/requests)
