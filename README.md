# Python_Projects-PDF_Merge_Automation_Using_PyPDF2_-_tkinter

This is a simple project where a daily boring job is made automated. Considering we have n number of PDFs and we want to merge them together. But a condition, we dont want to merge all pages of all the pdfs. We will select the pages runtime.

This is the best practise porject where each time, pdf will open and will ask user to choose which pages user wants to merge. 

Tkinter is the library which opens any files into GUI in python. and PyPDF2 is a library which will used to process the PDFs in python.

One supporting file gs927w32.exe will be required to view the files in tkinter and to process them.

You are expected to code a Python program to customize which pages you want in the combined PDF.
#-----------------------------------
High level Steps : 
At a high level, here’s what the program will do:
1> Find all PDF files in the current working directory.
2> Sort the filenames so the PDFs are added in order.
3> Write each page, excluding the first page, of each PDF to the output file.
#-----------------------------------
#--implementation Steps 
In terms of implementation, your code will need to do the following:

1> Call os.listdir() to find all the files in the working directory and remove any non-PDF files.
2> Call Python’s sort() list method to alphabetize the filenames.
3> Create a PdfFileWriter object for the output PDF.
4> Loop over each PDF file, creating a PdfFileReader object for it.
5> Loop over each page(except the first) in each PDF file.
6> Add the pages to the output PDF.
7> Write the output PDF to a file named final.pdf.
8> Code and save this project as combinePdfs.py
