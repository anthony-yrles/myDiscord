#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: lib.py
@created: 08/02/2024

@project: myDiscord
@licence: GPLv3
"""

from base64 import b64encode, b64decode





def encode_file(file):
    """"
    Encode a file to base64
    :param file:
    """
    with open(file, 'rb') as f:
        payload = f.read()
        return b64encode(payload)


def decode_file(file, save):
    """
    Decode a file to base64
    :param file: file to decode
    :param save: file to decode
    :return: None
    """
    with open(save, 'wb') as f:
        f.write(b64decode(file))


if __name__ == '__main__':
    print(hash_pass("PassWord1!"))
    print(check_pass("hello", hash_pass("hello")))
    print(encode_file('recording0.wav'))
    print(decode_file(encode_file('recording0.wav'), 'hello.wav'))
