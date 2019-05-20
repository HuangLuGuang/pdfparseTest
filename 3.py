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

# 处理识别后的字符
def handlerString(str):
    str = re.sub(u"\\[.*?]", "", str)
    result = str.replace("lll", '').replace("兰", '').replace("|", '').replace("_", '').replace("[",'').replace("}", '').replace("‖", '')\
        .replace("OUtTToL", 'OUTTOL').replace("Pe", '').replace("R 轴 庞 弓", "同轴度4").replace("木", "米")
    return result

@print_run_time
def ocr_test(image):
    """
    :param image: Image Obj
    :return:
    """
    string = pytesseract.image_to_string(image, lang="chi_sim+eng")
    # print(string)
    print(handlerString(string))

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

if __name__ == '__main__':
    images = convert_from_path('1.PDF', dpi=400, thread_count=3, fmt="jpg", output_folder='images', output_file="image")

    # for img in images:
    #     ocr_test(cutImg(img, (0,0,600,600)))

    res = cutImg(images[0], (0,0,600,600))
    ocr_test(res)
    print(res)




