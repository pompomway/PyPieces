#搜尋結果

import requests
from lxml import etree

#表示請求方使用瀏覽器
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}

def getPage(url):
    res=requests.get(url, headers=headers)#放入url取得葉面
    content=res.content.decode() #解碼
    html=etree.HTML(content) #使用etree.HTML()載入html