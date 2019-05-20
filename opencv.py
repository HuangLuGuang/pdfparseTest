# -*- coding: utf-8 -*-
# @createTime    : 2019/5/16 17:57
# @author  : Huanglg
# @fileName: opencv2.py
# @email: luguang.huang@mabotech.com
import cv2
import numpy as np

img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 120)
minLineLength = 100
maxLineGap = 5
lines = cv2.HoughLinesP(edges, 1.0, np.pi / 180, 500, minLineLength=minLineLength, maxLineGap=maxLineGap)
for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 0), 1)

cv2.imshow("lines", img)
cv2.waitKey()
cv2.destroyAllWindows()
