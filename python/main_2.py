import fitz
import os
from PIL import Image


def pdf2img():
    '''funtion used for convert a pdf into tiff'''
    file_path = input("enter your file path:")
    open_doc = fitz.open(file_path)
    try:
        os.mkdir("image_2")
    except:
        pass
    for page in range(0, open_doc.pageCount):
        pages = open_doc[page]
        pix = pages.getPixmap()
        pix.writeImage("image_2/{}.png".format(page))
        image = Image.open("image_2/%s.png" % (page))
        image.save("image_2/%s.tiff" %
                   (page), "TIFF", quality=10)
        os.remove("image_2/%s.png" % (page))


if __name__ == "__main__":
    pdf2img()
