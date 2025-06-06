from pypdf import PdfWriter

merger = PdfWriter()

pdfs=[]
n=int(input("How many pdf you want to Merge?\n->"))
for i in range (0,n):
    name=input("Enter the name of PDF you want to merge.\n-> ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()