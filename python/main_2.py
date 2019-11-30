import fitz
import os
from PIL import Image

def pdf2img():
    open_doc = fitz.open("../Akash Deep_CV.pdf")
    for page in range(0,open_doc.pageCount):
        pages = open_doc[page]
        pix = pages.getPixmap()
        pix.writeImage("{}.png".format(page))
        image = Image.open("%s.png"%(page))
        image.save("%s.tiff"%(page),"TIFF",quality=10)
        os.remove("%s.png"%(page))
        
if __name__ == "__main__":
    pdf2img()