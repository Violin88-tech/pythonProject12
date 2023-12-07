
import os
import requests

def download_pdf():
    content = requests.get(
        url="https://buildmedia.readthedocs.org/media/pdf/howtothink/latest/howtothink.pdf"
    ).content
    with open(os.path.join('tmp', "file_pdf.pdf"), 'wb') as file:
        file.write(content)







