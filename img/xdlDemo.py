import cv2
import imutils
import numpy as np
import os


def cv_show(name):
    cv2.imshow('name', name)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 统一的：mouse callback function
def draw_roi(img):
    # img = imutils.resize(img, width=500) 704 576
    # pts = [(249, 99), (475, 406), (497, 406), (497, 105), (249, 99)]  # 用于存放点

    pts = [(356, 130), (669, 576), (704, 576), (704, 130), (356, 130)]  # 用于存放点
    mask = np.zeros(img.shape, np.uint8)
    points = np.array(pts, np.int32)
    points = points.reshape((-1, 1, 2))
    # 画多边形
    mask = cv2.polylines(mask, [points], True, (255, 255, 255), 2)
    mask2 = cv2.fillPoly(mask.copy(), [points], (255, 255, 255))  # 用于求 ROI
    mask3 = cv2.fillPoly(mask.copy(), [points], (0, 255, 0))  # 用于 显示在桌面的图像

    show_image = cv2.addWeighted(src1=img, alpha=0.8, src2=mask3, beta=0.2, gamma=0)
    cv_show(show_image)

    ROI = cv2.bitwise_and(mask2, img)
    # res = np.hstack(show_image,ROI)
    cv_show(ROI)
    # cv2.imshow("res", res)
    cv2.waitKey(0)


# 创建图像与窗口并将窗口与回调函数绑定

img = cv2.imread("ori/1618310760.0999048.jpg")
draw_roi(img)
