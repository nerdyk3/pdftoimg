import os
from pdf2image import convert_from_path

def usingpdf2img():
    pages = convert_from_path("../Akash Deep_CV.pdf",500) # reading pdf in 500 dpi
    for page in pages:
        page.save("image/{}.tiff".format(page),'TIFF') #saving

if __name__ == "__main__":
    usingpdf2img()