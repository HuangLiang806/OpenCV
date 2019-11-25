# coding=utf-8

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

__author__ = 'huangliang'
__version__ = 'v1.0'


def double_click_to_draw_circle():
    def draw_circle(event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDBLCLK:
            cv.circle(img, (x, y), 50, (0, 0, 226), -1)

    img = np.zeros((600,800,3), np.uint8)
    cv.namedWindow('image')
    cv.setMouseCallback('image', draw_circle)

    while True:
        cv.imshow('image', img)
        if cv.waitKey(20) == 27:
            break
    cv.destroyAllWindows()



def main():
    double_click_to_draw_circle()


if __name__ == '__main__':
    main()