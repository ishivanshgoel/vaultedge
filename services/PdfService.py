from PyPDF2 import PdfReader, PdfWriter

class PdfService:
    @staticmethod
    def rotate_page_in_pdf(file_path, page_number, angle_of_rotation):
        reader = PdfReader(file_path)
        writer = PdfWriter()
        total_pages = len(reader.pages)
        if(page_number >= total_pages):
            raise Exception("page_number out of bound")
        
        if(angle_of_rotation == 0 or angle_of_rotation % 90 != 0 or angle_of_rotation > 270):
            raise Exception("invalid angle_of_rotation")

        current_page_number = 1
        for page in reader.pages:
            if current_page_number == page_number:
                page.rotate_clockwise(angle_of_rotation)
            writer.add_page(page)
            current_page_number += 1
            
        with open(file_path, "wb") as pdf_out:
            writer.write(pdf_out)