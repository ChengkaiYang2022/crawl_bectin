import urllib
import requests as re

def getFile(url):
    file_name = "text.pdf"
    chunk_size = 2000
    r = re.get(url, stream=True)
    with open("text2.pdf","wb") as f:
        for chunk in r.iter_content(chunk_size):
            f.write(chunk)
    print("Sucessful to download" + " " + file_name)
getFile("http://file.bcactc.com/FileInterface/FileRead.ashx?filename=3e50e262-72cc-4654-b451-0e15a6446646.pdf")