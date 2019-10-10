### 面向正方教务使用的 rsa 加密方法的 Python 实现

## 基本使用

### 安装

```
pip install PyRsa
```

### 基本使用

使用 RsaKey 模块

由于本模块是面向正方教务的加密，因此 modulus 长度应为 172；如果单纯是加密着玩的话，那么 modulus 与 pre_psw 两个参数的长度则有所限制，大概就是
$$
modulus = int(psw / 3) + 15 + psw
$$
嘛，谁会这么无聊干这事儿呢

```
>>> from PyRsa.pyrsa import RsaKey
>>> from PyRsa.pyb64 import Base64
>>> modulus = "AJftLhHzsQPu1LwCgOR41hRKn4tbaD/ehyZKiBWDYCpaualtMyJIT0SzBl07O2NwjxI8uwr82SMvEW9iiSEoBylHOWNnEzyOYwXb29xMo+D4LTVqMX7NkAliIqH+wOSA1g0DVxmcQWCtGVI4vDUnGIN8tYPlxc9NIXN5zO0HwqKn"
>>> exponent = 'AQAB'
>>> rsakey.set_public(Base64().b64tohex(modulus), Base64().b64tohex(exponent))
>>> psw = '1234567890'
>>> en_psw = Base64().hex2b64(rsakey.encrypt(pre_psw))
```

