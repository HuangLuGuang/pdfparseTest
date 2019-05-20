# -*- coding: utf-8 -*-
# @createTime    : 2019/5/16 23:09
# @author  : Huanglg
# @fileName: 4.py
# @email: luguang.huang@mabotech.com
#直线检测
#使用霍夫直线变换做直线检测，前提条件：边缘检测已经完成
import cv2 as cv
import numpy as np

#标准霍夫线变换
from pytesseract import pytesseract


def line_detection(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)  #apertureSize参数默认其实就是3
    cv.imshow("edges", edges)
    cv.imwrite('11.jpg', edges)
    lines = cv.HoughLines(edges, 1, np.pi/180, 80)
    # for line in lines:
    #     rho, theta = line[0]  #line[0]存储的是点到直线的极径和极角，其中极角是弧度表示的。
    #     a = np.cos(theta)   #theta是弧度
    #     b = np.sin(theta)
    #     x0 = a * rho    #代表x = r * cos（theta）
    #     y0 = b * rho    #代表y = r * sin（theta）
    #     x1 = int(x0 + 1000 * (-b)) #计算直线起点横坐标
    #     y1 = int(y0 + 1000 * a)    #计算起始起点纵坐标
    #     x2 = int(x0 - 1000 * (-b)) #计算直线终点横坐标
    #     y2 = int(y0 - 1000 * a)    #计算直线终点纵坐标    注：这里的数值1000给出了画出的线段长度范围大小，数值越小，画出的线段越短，数值越大，画出的线段越长
    #     cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)    #点的坐标必须是元组，不能是列表。
    # cv.imshow("image-lines", image)



src = cv.imread('1.jpg')
print(src.shape)
# cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
# cv.imshow('input_image', src)
line_detection(src)
cv.waitKey(0)
cv.destroyAllWindows()
