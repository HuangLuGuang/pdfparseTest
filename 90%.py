# -*- coding: utf-8 -*-
# @createTime    : 2019/6/1 16:05
# @author  : Huanglg
# @fileName: 90%.py
# @email: luguang.huang@mabotech.com
from PIL import ImageEnhance
from pdf2image import convert_from_path
import time
import pytesseract
import traceback

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

def ocr_test(image, lang = "chi_sim"):
    """

    :param image: PIL image obj
    :param lang: language
    :return:
    """
    string = pytesseract.image_to_string(image, lang=lang)
    return string
    # print(handlerString(string))


def wipLine(img):
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
    # res = str.replace("园","圆").replace("轻","轴").replace("札","系").replace(";",")").replace(",",")").replace("Zz","Z").replace("轲","轴")
    field_list = [
        ("园", "圆"),
        ("轻", "轴"),
        ("轲", "轴"),
        ("札", "系"),
        ("杀", "系"),
        ("坂", "至"),
        ("\"", ""),
        (";", ""),
        (",", ""),
        ("(", ""),
        (")", ""),
        ("Zz", "Z"),
        ("z", "Z"),

    ]
    try:
        for field in field_list:
            str = str.replace(field[0], field[1])
        if str[0] == '2':
            str = str.replace("2", "Z", 1)
    except Exception:
        # log.error(traceback.print_exc())
        print(traceback.print_exc())
    return str


def cutTestPosition(times, image, **kwargs):

    """
    :param times: loop times
    :param image: image obj
    :param kwargs: startX, startY, endX, endY -> The starting coordinates of the first cell
                space -> lattice spacing
    :return: list[image]
    """
    startX, startY, endX, endY, space = kwargs["startX"], kwargs["startY"], kwargs["endX"], kwargs["endY"], kwargs["space"]
    res = []
    for i in range(times):
        sx = startX
        sy = startY + space*i
        ex = endX
        ey = endY + space*i
        img = cutImg(img=image, coordinate=(sx,sy,ex,ey))
        res.append(img)
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
    pdfInfo = {}
    for k, v in scpoe.items():
        img = cutImg(img=image, coordinate=v)
        text = handlerstr(ocr_test(img))
        print(text)
        pdfInfo[k] = text

    testposition = cutTestPosition(image = image, times= 12, startX = 1500, startY=414, endX = 2160, endY = 493, space = 283)
    testvalue = cutTestPosition(image = image, times= 12, startX = 450, startY=596, endX = 2419, endY = 681, space = 283)

    # measuredict = {}
    #
    # for i in range(12):
    #     k = ocr_test(testposition[i])
    #     v = ocr_test(testvalue[i])
    #     measuredict[k] = v
    #
    # print(measuredict)
    # print(pdfInfo)

    testposition = map(ocr_test, testposition)
    for item in testposition:
        temp = handlerstr(item)
        print(temp)

    for index, img in enumerate(testvalue):
        value = ocr_test(img, lang="eng")
        print(value)


@print_run_time
def secondPage(image):

    testposition = cutTestPosition(image = image, times= 13, startX = 1500, startY=90, endX = 2160, endY = 169, space = 283)

    res = map(ocr_test, testposition)
    res = map(handlerstr, res)
    for text in res:
        print(text)

    testvalue = cutTestPosition(image=image, times=13, startX=450, startY=273, endX=2419, endY=359, space=283)

    for img in testvalue:
        res = ocr_test(img, lang="eng")
        print(res)



if __name__ == '__main__':

    import os
    # images = convert_from_path('pdfsample/19.03.10 20099B .PDF', dpi=400, thread_count=3, fmt="png", output_folder='images', output_file="image")
    # firstPage(images[0])
    # secondPage(images[1])
    # secondPage(images[2])

    pathList = os.listdir('pdfsample')
    for path in pathList:
        images = convert_from_path('pdfsample/' + path, dpi=400, thread_count=3, fmt="png",)
        print("file name-{}".format(path))
        firstPage(images[0])
        secondPage(images[1])
        secondPage(images[2])
        print("-" * 100)
