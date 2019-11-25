# coding=utf-8

import numpy as np
import cv2 as cv
import random
from matplotlib import pyplot as plt

__author__ = 'huangliang'
__version__ = 'v1.0'


def _nothing(x):
    pass

def color_palette():
    # 创建空的画布和一个窗口
    img = np.zeros((300,512,3), np.uint8)
    cv.namedWindow('palette')
    # 创建滑动条
    cv.createTrackbar('R', 'palette', 0, 255, _nothing)
    cv.createTrackbar('G', 'palette', 0, 255, _nothing)
    cv.createTrackbar('B', 'palette', 0, 255, _nothing)
    # 创建开关
    switch = '0: OFF \n1: ON'
    cv.createTrackbar(switch, 'palette', 0, 1, _nothing)

    while True:
        cv.imshow('palette', img)
        k = cv.waitKey(1) & 0xff
        if k == 27: break

        r = cv.getTrackbarPos('R', 'palette')
        g = cv.getTrackbarPos('G', 'palette')
        b = cv.getTrackbarPos('B', 'palette')
        s = cv.getTrackbarPos(switch, 'palette')

        img[:] = 0 if s == 0 else [b, g, r]


def click_to_draw_circle():
    def nothing(x):
        get_color_palette(palette)


    def create_color_palette():
        # 创建空的画布和一个窗口
        cv.namedWindow('palette')
        # 创建滑动条
        cv.createTrackbar('R', 'palette', 18, 255, nothing)
        cv.createTrackbar('G', 'palette', 211, 255, nothing)
        cv.createTrackbar('B', 'palette', 146, 255, nothing)
        # 创建开关
        cv.createTrackbar('switch', 'palette', 0, 1, _nothing)
        return None

    def get_color_palette(img):
        r = cv.getTrackbarPos('R', 'palette')
        g = cv.getTrackbarPos('G', 'palette')
        b = cv.getTrackbarPos('B', 'palette')
        s = cv.getTrackbarPos('switch', 'palette')

        img[:] = 0 if s == 0 else [b, g, r]
        cv.imshow('palette', img)
        ret = (0, 0, 0) if s == 0 else (b, g, r)
        return ret

    def draw_circle(event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            color = get_color_palette(palette)
            radius = random.randint(10, 60)
            cv.circle(img, (x, y), radius, color, -1)


    img = np.zeros((600,800,3), np.uint8)
    palette = np.zeros((200, 360, 3), np.uint8)
    create_color_palette()
    cv.namedWindow('image')
    cv.setMouseCallback('image', draw_circle)

    while True:
        cv.imshow('image', img)

        key = cv.waitKey(20)
        if key == 27:
            break
        elif key == ord('s'):
            cv.imwrite('hl_painting.jpg', img)
            cv.destroyAllWindows()
            print('---save done---')
    cv.destroyAllWindows()


def main():
    click_to_draw_circle()


if __name__ == '__main__':
    main()