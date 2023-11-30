#pip install pdfminer.six
import io
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
def extract_text_from_pdf(pdf_path):
 text = ""
 resource_manager = PDFResourceManager()
 fake_file_handle = io.StringIO()
 converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
 page_interpreter = PDFPageInterpreter(resource_manager, converter)
 with open(r"C:\Users\acer\Desktop\Srinivas-09\my_pdf_file.pdf", 'rb') as pdf_file:
     for page in PDFPage.get_pages(pdf_file, check_extractable=True):
         page_interpreter.process_page(page)
         text = fake_file_handle.getvalue()
         # Cleanup
 converter.close()
 fake_file_handle.close()
 return text
# Replace 'your_pdf_file.pdf' with the path to your PDF file
pdf_path = 'your_pdf_file.pdf'
extracted_text = extract_text_from_pdf(pdf_path)
# Print the extracted text
print(extracted_text) 
