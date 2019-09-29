import PyPDF2
import filetype
import os

pdf_object = os.listdir('d://suven/python/some sample pdfs')

#print(type(pdf_object))

pdfWriter = PyPDF2.PdfFileWriter()
sorted_pdf = pdf_object.sort()
for i in range(len(pdf_object)):
    #print(pdf[i])
    ###Checking All are pdf or not
    pdf_path = "d://suven/python/some sample pdfs/" + pdf_object[i]
    file_ext = os.path.splitext(pdf_path)
    print(file_ext[1])
    if file_ext[1] != ".pdf":
        os.remove(pdf_path)
    else:
        #print(pdf_path)
        pdfFile = open(pdf_path, 'rb')   #####Open the file
        pdfReader = PyPDF2.PdfFileReader(pdfFile)   ####Create A PDF Reader Object
        #print(pdfReader.numPages)e
        no_of_pages = pdfReader.numPages  #Calculating number of pages in Each Pdf
        print(no_of_pages)
        for i in range(1,no_of_pages):
            pdfWriterObj = pdfReader.getPage(i)
            #print(pdfWriterObj)
            pdfWriter.addPage(pdfWriterObj)
        #break
          
output_file = open("output_pdf.pdf", 'wb')
pdfWriter.write(output_file)   
    '''
    