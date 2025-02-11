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
    
input_prompt1 = '''
You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
'''

input_prompt2 = '''
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and generative ai or gen ai and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
'''
