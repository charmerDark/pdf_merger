import PIL.Image as Image
import PyPDF2
import os
from pikepdf import _cpphelpers

def merger(file_list):

    num_docs=len(file_list)
    merger=PyPDF2.PdfFileMerger()
    for i in range(num_docs):
        ext=file_list[i][-3:]
        if ext=="pdf":
            merger.append(PyPDF2.PdfFileReader(file_list[i],"rb"))
        elif ext=="png" or ext=="PNG":
            im = Image.open(file_list[i])
            rgb = Image.new('RGB', im.size, (255, 255, 255)) 
            rgb.paste(im, mask=im.split()[3])
            rgb.save('temp.pdf', 'PDF', resoultion=100.0)

            merger.append(PyPDF2.PdfFileReader('temp.pdf',"rb"))
            os.remove('temp.pdf')
        elif ext=="jpg" or ext=="jpeg":
            im = Image.open(file_list[i])
            im.save('temp.pdf', 'PDF', resoultion=100.0)

            merger.append(PyPDF2.PdfFileReader('temp.pdf',"rb"))
            os.remove('temp.pdf')

    merger.write("product file.pdf")

