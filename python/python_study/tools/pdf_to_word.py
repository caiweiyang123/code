from pdf2docx import Converter

pdf_path = "./理想汽车服务手册-员工适用版.pdf"
word_path = "./理想汽车服务手册-员工适用版.docx"

cv = Converter(pdf_path)
cv.convert(word_path,start=0,end=None)
cv.close()