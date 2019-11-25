# coding=utf-8

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

__author__ = 'huangliang'
__version__ = 'v1.0'


def double_star():
    img = cv.imread(r'C:\Users\huang\Pictures\806.jpg')
    star = img[305:355, 525:575]  #[y_start:y_end, x_start:x_end]
    img[0:50, 0:50] = star


    cv.imshow('double star', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def add_img():
    miao = cv.imread(r'C:\Users\huang\Pictures\miao.jpg')
    haha = cv.imread(r'C:\Users\huang\Pictures\haha.jpg')
    # dst=α⋅img1+β⋅img2+γ
    dst = cv.addWeighted(miao, 0.7, haha, 0.3,0)

    cv.imshow('sum', dst)
    cv.waitKey(0)
    cv.destroyAllWindows()

def add_logo():
    img = cv.imread(r'C:\Users\huang\Pictures\806.jpg')
    logo = cv.imread(r'C:\Users\huang\Pictures\logo.png')
    rows, cols, channels = logo.shape
    part = img[0:rows, 0:cols]

    logo_grey = cv.cvtColor(logo, cv.COLOR_BGR2GRAY)
    ret, mask = cv.threshold(logo_grey, 10, 255, cv.THRESH_BINARY)
    mask_inv = cv.bitwise_not(mask)  # 取反

    cv.imshow('1', logo)
    cv.imshow('2', logo_grey)
    cv.imshow('3', mask)
    cv.imshow('not3', mask_inv)

    img_bg = cv.bitwise_and(part, part, mask=mask_inv)
    logo_fg = cv.bitwise_and(logo, logo, mask=mask)  # 留白去黑

    dst = cv.add(img_bg, logo_fg)
    img[0:rows, 0:cols] = dst

    cv.imshow('4', img_bg)
    cv.imshow('5', logo_fg)
    cv.imshow('6', dst)

    cv.imshow('成品', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def main():
    #double_star()
    #add_img()
    add_logo()


if __name__ == '__main__':
    main()