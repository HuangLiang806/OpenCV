# coding=utf-8
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def draw():
    # 生成一张黑底照片
    img = np.zeros((512, 512, 3), np.uint8)

    # 画线
    cv.line(img, (0,0), (511,511), (0,0,255), 5)

    # 画正方形
    cv.rectangle(img, (0,0), (50,50), (73,156,84), -1)

    # 画圆
    cv.circle(img, (255,255), 50, (88,88,88), -1)

    # 显示文字
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, "HL.'s painting", (10,500), font, 2, (255,255,255), 2, cv.LINE_AA)

    # 将图像矩阵显示出来
    cv.imshow("hl's painting", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def draw_bing_tang_hu_lu():
    img = np.zeros((600, 300, 3), np.uint8)

    # 画线
    cv.line(img, (150, 0), (150, 600), (88, 88, 88), 5)

    # 画⚪
    for i in range(50, 550, 100):
        cv.circle(img, (150, i), 50, (0, 0, 226), -1)

    # 将图像矩阵显示出来
    cv.imshow("hl's painting", img)
    # cv.imwrite('bing_tang_hu_lu.jpg', img)
    cv.waitKey(0)
    cv.destroyAllWindows()




def main():
    draw_bing_tang_hu_lu()


if __name__ == '__main__':
    main()