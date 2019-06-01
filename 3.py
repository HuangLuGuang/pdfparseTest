# -*- coding: utf-8 -*-
# @createTime    : 2019/5/16 14:04
# @author  : Huanglg
# @fileName: 3.py
# @email: luguang.huang@mabotech.com
from PIL import ImageEnhance
from pdf2image import convert_from_path
import re

import time
import pytesseract

#计算时间函数
def print_run_time(func):
    def wrapper(*args, **kw):
        local_time = time.time()
        func(*args, **kw)
        print('current Function [%s] run time is %.2f' % (func.__name__ ,time.time() - local_time))
    return wrapper


def ocr_test(image):
    """
    :param image: Image Obj
    :return:
    """
    string = pytesseract.image_to_string(image, lang="chi_sim+eng")
    return string
    # print(handlerString(string))

def cutImg(img, coordinate):
     """
      根据坐标位置剪切图片
     :param img Obj
     :param coordinate: 原始图片上的坐标(tuple) egg:(x, y, w, h) ---> x,y为矩形左上角坐标, w,h为右下角坐标
     :return:
     """
     # image = Image.open(imgsrc)
     region = img.crop(coordinate)
     region = ImageEnhance.Contrast(region).enhance(1.5)
     return region

def wipLine(img):
    # 处理图片
    width = img.size[0]
    height = img.size[1]
    for i in range(0, width):
        for j in range(0, height):
            data = img.getpixel((i, j))
            R = data[0]
            G = data[1]
            B = data[2]
            if (R < 10 and G <10 and B < 10) or (R > 150 and G < 90):
                img.putpixel((i, j), (0, 0, 0))
            else:
                img.putpixel((i, j), (255, 255, 255))
    return img

@print_run_time
def firstPage(image):
    y,h = 607, 753
    space = 282
    fcf1 = cutImg(image, (215,607,2480,753))
    fcf2 = cutImg(image, (215, y+space, 2480,h + space))
    fcf3 = cutImg(image, (215, y+space*2, 2480,h + space * 2))
    fcf4 = cutImg(image, (215, y+space*3, 2480,h + space * 3))
    fcf5 = cutImg(image, (215, y+space*4, 2480,h + space * 4))
    fcf6 = cutImg(image, (215, y+space*5, 2480,h + space * 5))
    position = cutImg(image, (215, 2391, 2480, 2645))
    positionTitle = cutImg(image, (1690, 2211, 2005, 2273))
    position1 = cutImg(image, (215, 2859, 2480, 3103))
    position1Title = cutImg(image, (1690, 2675, 2005, 2743))
    position2 = cutImg(image, (215, 3325, 2480, 3578))
    position2Title = cutImg(image, (1690, 3143, 2005, 3207))
    position, position1, position2 = map(wipLine, (position, position1, position2))
    position.save('position.jpg')
    position2.save('position2.jpg')
    res = map(ocr_test, (fcf1, fcf2, fcf3, fcf4, fcf5, fcf6,positionTitle, position, position1Title, position1, position2Title, position2))
    for text in res:
        print(text)


def cutRowImage(img):
    # 处理图片
    width = img.size[0]
    height = img.size[1]
    h = 0
    while h + 85 < height:
        print(h)
        h = h + 85
        res = cutImg(img, (0, h, 3300, h + 85))
        res.save(str(h) + '.jpg')

def handlerImage(img):
    # img = cutImg(img, (190,500,2380, 3547))
    width = img.size[0]
    height = img.size[1]
    for i in range(width):
        for j in range(height):
            data = img.getpixel((i, j))
            R = data[0]
            G = data[1]
            B = data[2]
            if (R==G==B and R < 200) or (R - G > 20 and R - B > 35):
                img.putpixel((i, j), (0, 0, 0))
            else:
                img.putpixel((i, j), (255, 255, 255))

    img.save('handler.png')
    return img


if __name__ == '__main__':
    images = convert_from_path('1.PDF', dpi=400, thread_count=3, fmt="png", output_folder='images', output_file="image")
    firstPage(images[0])
    # img = handlerImage(images[0])
    # str = ocr_test(img)
    # print(str)
