# coding=utf-8

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def capture_camera():
    cap = cv.VideoCapture(1)  # 参数为选择对应摄像头输入
    if cap.isOpened() is False:
        print("摄像头打开失败")
        exit()

    while True:
        # 获取视频帧
        ret, frame = cap.read()
        if ret is False:
            print("无法获取视频帧。。。")
            break

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # 显示接收到的视频数据
        cv.imshow('my_video', gray)
        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


def capture_save_video():
    cap = cv.VideoCapture(1)

    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret is False:
            print("无法获取视频帧。。。")
            break
        frame = cv.flip(frame, 1)

        out.write(frame)
        cv.imshow('my_video', frame)

        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    out.release()
    cv.destroyAllWindows()





def main():
    capture_camera()


if __name__ == '__main__':
    main()
