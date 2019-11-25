# coding=utf-8

# import numpy as np
import cv2 as cv
import time
# from matplotlib import pyplot as plt

__author__ = 'huangliang'
__version__ = 'v1.0'

def measure_time():
    img = cv.imread('hl_painting.jpg',)

    tt1 = time.time()
    t1 = cv.getTickCount()
    for i in range(5, 49, 2):
        img = cv.medianBlur(img, i)

    tt2 = time.time()
    t2 = cv.getTickCount()

    t = (t2 - t1) / cv.getTickFrequency()
    tt = (tt2 -tt1)

    print(t)
    print(tt)



def main():
    measure_time()


if __name__ == '__main__':
    main()