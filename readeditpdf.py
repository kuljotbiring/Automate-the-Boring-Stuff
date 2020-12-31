import PyPDF2, os

os.chdir('/Users/kj/Desktop/Certificates/Automate the Boring Stuff')

# open the file in read binary mode
pdfFile = open('meetingminutes1.pdf', 'rb')

# pass this object to PyPDF2 will make a pdf reader object
reader = PyPDF2.PdfFileReader(pdfFile)

# get the number of pages in the document
print(reader.numPages)

# return a page object py specifiying page
page = reader.getPage(0)

# now you can extract the page
print(page.extractText())

# we can get the entire text of the pdf by looping
for pageNum in range(reader.numPages):
    # extract the text in each page and print it out
    print(reader.getPage(pageNum).extractText())


"""Add, remove, re-order pages in a PDF at the page level"""

# combine 2 PDF files
pdf1File = open('meetingminutes1.pdf', 'rbf')
pdf2File = open('meetingminutes2.pdf', 'rbf')

reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)


writer = PyPDF2.PdfFileWriter()

# add the pages by looping through all the pages
for pageNum in range(reader1.numPages):
    # getting each page object passing it the page number
    page = reader1.getPage(pageNum)
    # call the add page function and passing it the page
    writer.addPage(page)

# add the pages by looping through all the pages
for pageNum in range(reader2.numPages):
    # getting each page object passing it the page number
    page = reader2.getPage(pageNum)
    # call the add page function and passing it the page
    writer.addPage(page)

# now to save the output to a file
outputFile = open('combinedminutes.pdf', 'wb')

writer.write(outputFile)

# close the files
pdf1File.close()
pdf2File.close()