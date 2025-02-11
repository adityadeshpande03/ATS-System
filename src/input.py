import pdf2image
import os
from PIL import Image
import io
import base64

def input_pdf_content(uploaded_file):
    images=pdf2image.convert_from_bytes(uploaded_file.read())

    first_page=images[0]

    #Convert to bytes
    if uploaded_file is not None:

        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    
    else:
        raise FileNotFoundError("No file uploaded")
    
