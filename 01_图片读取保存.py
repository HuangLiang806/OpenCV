# coding=utf-8

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def test01():
    # 以正常模式读取图片信息
    img = cv.imread(r'hl_painting.jpg', 1)

    # 显示照片
    cv.imshow('hl_painting', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # 保存照片
    # cv.imwrite('my_image.jpg', img)


def test02():
    # 以灰度模式读取图片信息
    img = cv.imread(r'C:\Users\huang\Pictures\806.jpg', 0)

    # 显示照片
    cv.imshow('my test image', img)
    key = cv.waitKey(0)
    print("key=", key)
    if key == 27:  # 等待esc键退出
       cv.destroyAllWindows()
    elif key == ord('s'):
        cv.imwrite('my_gray_image.jpg', img)
        cv.destroyAllWindows()
        print('---save done---')


def test_plt():
    img = cv.imread(r'C:\Users\huang\Pictures\806.jpg', 0)
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([])
    plt.yticks([])
    plt.show()

def main():
    test01()


if __name__ == '__main__':
    main()