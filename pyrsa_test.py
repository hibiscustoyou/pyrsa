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
    modulus = '"AIGSfrdb8K42HCxY9UAsfOPn4sh7A7VVeiUOS+IaAt6tTcf99mtiN1Q7jIcCr3Hk9Vz4tkiOwxub4zNrUU8PY6H6Oj6/TYVFWYy6NBJeREe6RDMNBMorn+sABZ/2JLLi+mTSKe5d6HvPsROtMLvD+TBUnJr9mDcOvPrLZwY1YXkd"'
    exponent = 'AQAB'
    rsakey.set_public(Base64().b64tohex(modulus), Base64().b64tohex(exponent))
    rr = rsakey.rsa_encrypt('1234567890')
    enpsw = Base64().hex2b64(rr)
    print(enpsw)
