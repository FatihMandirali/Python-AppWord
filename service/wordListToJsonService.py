import model_list.word as modelword
import json
import requests #web sayfasından verileri requests ile çekiyoruz
from bs4 import BeautifulSoup  #Web sayfası içindeki bilgileri alma

def createJsonFile():
    url = "https://blog.konusarakogren.com/en-cok-kullanilan-ingilizce-kelimeler-ve-anlamlari/"

    response = requests.get(url)

    html_content = response.content

    soup = BeautifulSoup(html_content,"html.parser")

    wordList = list();
    for i in soup.find_all("li"):
        if(i.text.find("–")>0):
            wordList.append(modelword.Word(i.text.split("–")[1].replace(" ",""),i.text.split("–")[0].replace(" ","")))

    wordList.pop(0)
    wordList.pop()

    file = open('wordList.json', 'w', encoding='utf8')
    file.write(json.dumps([ob.__dict__ for ob in wordList]))
    file.close()
    return json.dumps([ob.__dict__ for ob in wordList])

