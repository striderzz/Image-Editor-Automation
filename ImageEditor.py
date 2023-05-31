#mass edit photos in your folder.change constrast, brightness etc
from PIL import Image, ImageEnhance,ImageFilter
import os

path="./Images"
pathOut="/edited"

for filename in os.listdir(path):
    img=Image.open(f"{path}/{filename}")
    edit=img.filter(ImageFilter.SHARPEN).convert('RGB')

    # image constrast enhancer

    factor=1
    enhancer=ImageEnhance.Contrast(edit)
    edit=enhancer.enhance(factor)

    # image brightness enhancer

    factor = 2
    enhancer = ImageEnhance.Brightness(edit)
    edit = enhancer.enhance(factor)

    clean_name=os.path.splitext(filename)[0]
    edit.save(f".{pathOut}/{clean_name}_edited.jpg")