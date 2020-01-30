# -*- coding:utf-8 -*-

import imageio as img

"""
create gif picture

usage:
def main():
    gifname = 'zyx.gif'
    gifpath = ['001.jpg', '002.jpg','003.jpg']
    dur = 1
    create_gif(gifname, gifpath, duration=dur)

"""


def create_gif(gif_name, gif_path, duration):
    frame = []
    for i in gif_path:
        frame.append(img.imread(i))
    img.mimsave(gif_name, frame, duration=duration)
