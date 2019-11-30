import os
from pdf2image import convert_from_path

def usingpdf2img():
    pages = convert_from_path("../Akash Deep_CV.pdf",100) # reading pdf in 100 dpi
    try: #if image folder not availble 
        os.mkdir("image")
    except:
        print("already exist")
    for page in pages:
        page.save("image/{}.tiff".format(page),'TIFF',quality = 10) #saving

if __name__ == "__main__":
    usingpdf2img()