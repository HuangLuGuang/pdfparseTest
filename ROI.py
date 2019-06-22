from PIL import Image
from pytesseract import *

img = Image.open("3.png")
text = image_to_string(img)
print(text)

