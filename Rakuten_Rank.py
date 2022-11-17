import time as t
import requests
from lxml import etree
from openpyxl import load_workbook

def getPage(url):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
    res=requests.get(url, headers=headers)#放入url取得頁面
    content=res.content.decode() #解碼
    html=etree.HTML(content) #使用etree.HTML()載入html
    #Item_name商品名
    Item_name=html.xpath("/html/body/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[7]/div/div[3]/div[1]/div/div/div/div[1]/a/text()")
    #Item_price商品金額
    Item_price=html.xpath("/html/body/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[7]/div/div[3]/div[2]/div[1]/div[1]/text()")

    #商店名
    Item_shopname=html.xpath("/html/body/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[7]/div/div[3]/div[1]/div/div/div/div[3]/a/text()")

    return Item_name,Item_price,Item_shopname
    
    
a=getPage("https://ranking.rakuten.co.jp/daily/111469/")
print(a)