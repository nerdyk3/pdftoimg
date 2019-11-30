import os
from pdf2image import convert_from_path

def usingpdf2img():
    pages = convert_from_path("../Akash Deep_CV.pdf",100) # reading pdf in 100 dpi
    try: #if image folder not availble 
        os.mkdir("image")
    except:
        print("already exist")
    page_number = 0 #init page number
    for page in pages:
        page_number +=1 #increasing page number
        page.save("image/{}.tiff".format(page_number),'TIFF',quality = 10) #saving

if __name__ == "__main__":
    usingpdf2img()