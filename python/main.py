import os
from pdf2image import convert_from_path


def usingpdf2img():
    '''funtion used for convert a pdf into tiff'''
    file_path = input("enter your file path:")
    pages = convert_from_path(file_path, 100)  # reading pdf in 100 dpi
    try:
        os.mkdir("image")
    except:
        pass
    page_number = 0
    for page in pages:
        page_number += 1
        page.save("image/{}.tiff".format(page_number),
                  'TIFF', quality=10)  # saving


if __name__ == "__main__":
    usingpdf2img()
