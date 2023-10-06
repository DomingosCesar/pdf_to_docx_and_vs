from pdf2docx import Converter

class Converte_to:
    def __init__(self, file) -> None:
        self.input_file = file
        self.output_file = f"{self.input_file[:len(self.input_file) - 3]}.docx"
        self.conversor = Converter(self.input_file)
        
    def converte_pdf_to_docx(self):
        f = self.conversor.convert(self.output_file)
        self.conversor.close()
        return f