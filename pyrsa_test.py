# -*- coding: utf-8 -*-
"""
Created on: 2019/10/10 22:31
Author    : zxt
File      : pyrsa_test.py
Software  : PyCharm
"""

from PyRsa.pyrsa import RsaKey
from PyRsa.pyb64 import Base64


if __name__ == '__main__':
    """
    测试使用文件
    """
    rsakey = RsaKey()
    modulus = "AOQfMKCLOREHpMnwSqWq2yuEO/m9KlUfHpqHoqkU+zpTXW59LdkE35N5pVpaggxZZxX+VtLiZTa+" \
              "pae4iWP8hWQm68aeVNus1WBlVexsZllVlhGWmKTqPZHpU//d/XwXrm81IR5drosuPaJf1WgEQV6T3tuYxcoj81jfg8qm4HIL"
    exponent = 'AQAB'
    rsakey.set_public(Base64().b64tohex(modulus), Base64().b64tohex(exponent))
    rr = rsakey.rsa_encrypt('1234567890')
    enpsw = Base64().hex2b64(rr)
    print(enpsw)
