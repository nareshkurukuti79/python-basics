###################### Working with PDF files ########################

import PyPDF2

# Reading and Writing PDF Files

with open("flexbox.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)

    print(reader.numPages)

    page = reader.getPage(10)

    writer = PyPDF2.PdfFileWriter()

    writer.addPage(page)

    with open("flixboxv2.pdf", "wb") as result:
        writer.write(result)

# Merging PDF Files

merger = PyPDF2.PdfFileMerger()
pdf_files = ["flexbox.pdf", "grid.pdf"]

for pdf_file in pdf_files:
    merger.append(pdf_file)

merger.writer("Flix-Grid-Guide.pdf")
