import fitz
import os
from PIL import Image

def pdf2img():
    file_path = input("enter your file path:")
    open_doc = fitz.open(file_path) #reading pdf
    try: #if image folder not availble 
        os.mkdir("image_2")
    except:
        pass
    for page in range(0,open_doc.pageCount): #runing on per page
        pages = open_doc[page] #opening of doc
        pix = pages.getPixmap() #making frame
        pix.writeImage("image_2/{}.png".format(page)) #saving asimage
        image = Image.open("image_2/%s.png"%(page)) #open image
        image.save("image_2/%s.tiff"%(page),"TIFF",quality=10) #saving in tiff
        os.remove("image_2/%s.png"%(page)) #deleting png
        
if __name__ == "__main__":
    pdf2img()