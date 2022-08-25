import PyPDF2
import sys

#adding watermark to all pages
with open('super.pdf', 'rb') as original_pdf, open('wtr.pdf', 'rb') as watermark_pdf:
    original = PyPDF2.PdfFileReader(original_pdf)
    watermark = PyPDF2.PdfFileReader(watermark_pdf)
    watermark_page = watermark.getPage(0)

    updated = PyPDF2.PdfFileWriter()

    for i in range(original.getNumPages()):
        original_page = original.getPage(i)
        original_page.mergePage(watermark_page)
        updated.addPage(original_page)
    
    with open('super_watermark.pdf', 'wb') as merged_file:
        updated.write(merged_file)



#combining PDFs
inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')



# Rotating One PDF
# #file name and 'rb' which means read binary. this creates a filestream object
# with open('dummy.pdf', 'rb') as file:
#     #reading binary object
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)