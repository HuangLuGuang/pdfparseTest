# -*- coding: utf-8 -*-
# @createTime    : 2019/5/15 22:22
# @author  : Huanglg
# @fileName: 1.py
# @email: luguang.huang@mabotech.com
# import pyocr
from PIL import Image as PI
from wand.image import Image
import pyocr
import pyocr.builders
import io

tool = pyocr.get_available_tools()[0]
# lang = tool.get_available_languages()[1]

req_image = []
final_text = []

image_pdf = Image(filename="2.PDF", resolution=300)
image_jpeg = image_pdf.convert('jpeg')

for img in image_jpeg.sequence:
   img_page = Image(image=img)
   req_image.append(image_jpeg.make_blob('jpeg'))



for index, img in enumerate(req_image):
    with open(str(index)+".jpeg", 'wb') as f:
        print(index)
        f.write(img)


for img in req_image:
    text = tool.image_to_string(
        PI.open(io.BytesIO(img)),
        lang = 'chs',
        builder=pyocr.builders.TextBnuilder()
    )
    final_text.append(text)



for text in final_text:
    print(text)
