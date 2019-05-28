# coding:utf-8
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import splint


def draw_2ASK(r):
    return math.erfc(math.sqrt(r / 4)) * 0.5


def draw_2FSK(r):
    return math.erfc(math.sqrt(r / 2)) * 0.5


def draw_2PSK(r):
    return math.erfc(math.sqrt(r)) * 0.5


def r():
    r = 0
    while r < 18:
        yield r
        r = r + 1


def draw():
    # r = [x for x in range(0, 18, 0.5)]
    ask = [draw_2ASK(item) for item in r()]
    fsk = [draw_2FSK(item) for item in r()]
    psk = [draw_2PSK(item) for item in r()]

    a = pd.Series(np.array(ask))
    a.plot(logy=True, label="ASK", legend=True)
    f = pd.Series(np.array(fsk))
    f.plot(logy=True, label="FSK", legend=True)
    p = pd.Series(np.array(psk))
    p.plot(logy=True, label="PSK", legend=True)
    plt.xlim(0, 18)
    plt.show()
    # plt.plot(fsk, label="2FSK")
    # plt.plot(psk, label="2PSK")
    # plt.legend()
    # plt.xlim(0, 18)
    # # plt.ylim(0, 1)
    # plt.xlabel("r/dB")
    # plt.ylabel("P")
    # plt.show()


if __name__ == '__main__':
    draw()
