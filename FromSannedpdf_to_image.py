#insatll poppler and write the path in poppler_path
#link:https://blog.alivate.com.au/poppler-windows/
from pdf2image import convert_from_path  
pdfs = r"path_scanned_pdf.pdf"
pages = convert_from_path(pdfs, 350 , poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
print(pages)
i = 1
for page in pages:
    image_name = "Page_" + str(i) + ".jpg"  
    page.save(image_name, "JPEG")
    i = i+1   