# -*- coding: utf-8 -*-

import urllib
import requests as re

def getFile(pdf_real_link, project_id, title, date):
    file_name = "{}_{}_{}.pdf".format(str(project_id), str(title), str(date))
    chunk_size = 2000
    r = re.get(pdf_real_link, stream=True)
    if r.status_code == 200:
        with open(("pdf_result/"+file_name).decode('utf-8'), "wb") as f:
            for chunk in r.iter_content(chunk_size):
                f.write(chunk)
        print("Sucessful to download" + " " + file_name)
    else:
        print("!!!ERROR!!!")
def test():
    getFile("http://file.bcactc.com/FileInterface/FileRead.ashx?filename=3e50e262-72cc-4654-b451-0e15a6446646.pdf")