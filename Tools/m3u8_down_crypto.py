# coding:utf-8

import requests
import os
import re
from Crypto.Cipher import AES
# pip install Crypto,PyCryptodome


def crypto(filepath, data, key: str):
    """
    ts字节流进行AES解密
    """
    cp = AES.new(key.encode("utf-8"), AES.MODE_CBC)
    with open(filepath, "ab") as f:
        # decrypt 中必须传入字节流
        f.write(cp.decrypt(data))


def decrypt_m3u8(file):
    with open(file, "r") as f:
        s = f.readlines()
    for item in s:
        if item[0] != '#':
            yield item


def stream(url):
    head = {
        "Referer": "https://www.kk00qq.com:2083/public/player/ckm3u8.html?v=/2019/e01c1541/m3u8.m3u8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    sess = requests.Session()

    response = sess.get(url)
    return response.content


# crypto(R"E:\Users\Downloads\new.ts", R"E:\Users\Downloads\0000.ts", "g14yv7rlzdup8m3c")
