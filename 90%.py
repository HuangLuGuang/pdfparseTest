# -*- coding: utf-8 -*-
# @createTime    : 2019/6/1 16:05
# @author  : Huanglg
# @fileName: 90%.py
# @email: luguang.huang@mabotech.com
from PIL import ImageEnhance
from pdf2image import convert_from_path
import time
import pytesseract

#计算时间函数


def print_run_time(func):
    def wrapper(*args, **kw):
        local_time = time.time()
        func(*args, **kw)
        print('current Function [%s] run time is %.2f' % (func.__name__ ,time.time() - local_time))
    return wrapper


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

def ocr_test(image, lang = "chi_sim+eng"):
    """

    :param image: PIL image obj
    :param lang: language
    :return:
    """
    string = pytesseract.image_to_string(image, lang=lang)
    return string
    # print(handlerString(string))


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

def handlerstr(str):
    res = str.replace("园","圆").replace("#", "至").replace("[§)","圆").replace("轻","轴").replace("札","系")
    return res


@print_run_time
def firstPage(image):

    # 识别区域
    scpoe = {
        "title": (833,91, 2457,227),        # 标题
        "testtime": (2707,109, 2977,225),     # 检测时间
        "serialnum": (1901,283, 2209,369),  # 序列号
        "operator": (2707,259, 2977,377),  # 操作人
    }
    pdfInfo = []
    for k, v in scpoe.items():
        img = cutImg(img=image, coordinate=v)
        # img = {k:img}
        pdfInfo.append(img)

    testposition = []
    startX, startY, space = 1500, 414, 283
    endX, endY = 2160, 493
    for i in range(12):
        sx = startX
        sy = startY + space*i
        ex = endX
        ey = endY + space*i
        img = cutImg(img=image, coordinate=(sx,sy,ex,ey))
        testposition.append(img)

    startX, startY, space = 450, 596, 283
    endX, endY = 2419, 681
    testvalue = []
    for i in range(12):
        sx = startX
        sy = startY + space * i
        ex = endX
        ey = endY + space * i
        img = cutImg(img=image, coordinate=(sx, sy, ex, ey))
        testvalue.append(img)

    # res = map(ocr_test, pdfInfo + testposition)
    # res = map(handlerstr, res)
    # for text in res:
    #     print(text)
    for img in pdfInfo+testposition:
        res = ocr_test(img)
        print(handlerstr(res))
    for img in testvalue:
        res = ocr_test(img, lang="eng")
        print(res)


if __name__ == '__main__':
    images = convert_from_path('pdfsample/19.03.10 20099B .PDF', dpi=400, thread_count=3, fmt="png", output_folder='images', output_file="image")
    firstPage(images[0])
