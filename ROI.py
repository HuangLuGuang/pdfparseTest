# -*- coding: utf-8 -*-
# @createTime    : 2019/5/17 9:17
# @author  : Huanglg
# @fileName: ROI.py
# @email: luguang.huang@mabotech.com
# coding: utf-8
import cv2
import pytesseract

# 设置tesseract可执行程序及中文字库的路径
# pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR'
# tessdata_dir_config = r'--tessdata-dir D:\Program Files\Tesseract-OCR\tessdata'

img = cv2.imread("1.jpg")

print(img.shape)
height, width, _ = img.shape

# 设定图片区域，例如取图片顶部以下60行、从右往左数第5-125列的区域
img_roi = img[0:60, width-125:width-5]

text = pytesseract.image_to_string(img_roi, lang='chi_sim')
print(text)

# 由于图片上字符间距的原因，识别出的文本中可能会包含空格，使用下列语句去除空格
for r in text.splitlines():
    print(r.replace(" ", ""))

cv2.namedWindow("roi")
cv2.imshow("roi", img_roi)
cv2.waitKey(0)
cv2.destroyAllWindow()
