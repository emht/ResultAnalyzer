from pyPdf import PdfFileReader

f = open('data.pdf', 'rb')
reader = PdfFileReader(f)
contents = reader.getPage(0).extract.Text().split('\n')
f.close()
