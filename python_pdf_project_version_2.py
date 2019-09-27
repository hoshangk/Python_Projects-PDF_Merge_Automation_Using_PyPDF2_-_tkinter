import PyPDF2
import filetype
import os
from tkinter import *
from tkdocviewer import *

pdf_object = os.listdir('some sample pdfs')
#print(len(pdf_object))

pdfWriter = PyPDF2.PdfFileWriter()
sorted_pdf = pdf_object.sort()

for i in range(len(pdf_object)):
	pdf_path = "/some sample pdfs/" + pdf_object[i]
	print("pdf is-",pdf_path)
	file_ext = os.path.splitext(pdf_path)
	#print(file_ext[1])
	if file_ext[1] != ".pdf":
		os.remove(pdf_path)
	else:
		#get number of Pages in each pdf
		pdfFile = open(pdf_path, 'rb')
		pdfReader = PyPDF2.PdfFileReader(pdfFile)
		num_pages = pdfReader.numPages
		print("Total No of Pages in this PDF-",num_pages)
		# Create a root window
		root = Tk()
		#root = root.geometry("1200x800")
		# Create a DocViewer widget
		v = DocViewer(root.geometry("1000x500"))
		v.pack(side="right", expand=1, fill="both")
		# Display some document
		v.display_file(pdf_path)
		# Start Tk's event loop
		root.mainloop()

		no_of_pages = int(input("Enter the Number of pages you want to merge-"))
		print("no_of_pages-",no_of_pages)
		from_page = 0
		from_page = int(input("Enter From Which page no-"))
		print("From Page no-",from_page)

		for i in range(no_of_pages):
			print("from_page value-",from_page)
			pdfWriterObj = pdfReader.getPage(from_page-1)
			#print(pdfWriterObj)
			pdfWriter.addPage(pdfWriterObj)
			from_page += 1

output_file_name = input("Enter Name of the output_file-")
output_file = open(f"{output_file_name}.pdf", 'wb')
pdfWriter.write(output_file)  