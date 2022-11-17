#Rank100名

import time as t
import requests
from lxml import etree
from openpyxl import load_workbook

#表示請求方使用瀏覽器
#https://shopping.yahoo.co.jp/ranking/


    

def menu():
    print("-----------Yahoo Rank取用-----------")
    print("*請確保getYahooRank.xlsx關閉")
    print("*請輸擷取並輸入該rank資料夾位置，例如網址為:")
    print("     https://shopping.yahoo.co.jp/category/2503/3930/ranking/cr_80/(略)")
    print("\n"+"*請擷取jp/與/ranking之間的字元，上方案例即輸入category/2503/3930")
    print("\n"+"*若jp/與/ranking之間無字元，如jp/ranking/，請直接鍵入Enter")
    urlinsert=input("請輸入(輸入0結束程式):")
    if urlinsert!="":
        urlinsert=urlinsert+"/"
    
        
    return urlinsert

#獲取並處理資料成陣列
def getPage(url):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
    res=requests.get(url, headers=headers)#放入url取得頁面
    content=res.content.decode() #解碼
    html=etree.HTML(content) #使用etree.HTML()載入html
    #Item_name商品名
    Item_name=html.xpath('/html/body/div[1]/div[2]/div/div[1]/div/div[3]/ol/li/div[2]/h4[1]/a/text()')
    #Item_price商品金額
    Item_price=html.xpath('/html/body/div[1]/div[2]/div/div[1]/div/div[3]/ol/li/div[2]/h4[2]/span[1]/text()')
    
    #Item_shipping送料(送料有空欄位 所以要一筆一筆讀)
    Item_shipping=[]
    insert=1
    for i in range(20):
        shipping=html.xpath('/html/body/div[1]/div[2]/div/div[1]/div/div[3]/ol/li['+str(insert)+']/div[2]/p[2]/span/text()')
        a=[]
        if shipping==a:
            shipping=["null"]
        for j in shipping:
            Item_shipping.append(j)
        insert+=1

   #商店名
    Item_shopname=html.xpath('/html/body/div[1]/div[2]/div/div[1]/div/div[3]/ol/li/div[2]/h4[3]/a/text()')
    #print(Item_shopname)
    return Item_name,Item_price,Item_shipping,Item_shopname

def deata_select(order):
    #rank100位一共5頁要合併成一個陣列
    url="https://shopping.yahoo.co.jp/"+order+"ranking/#list"
    getData=getPage(url)
    url=url.replace("/#list", "/cr_20/#list")
    getData1=getPage(url)
    url=url.replace("/cr_20/#list", "/cr_40/#list")
    getData2=getPage(url)
    url=url.replace("/cr_40/#list", "/cr_60/#list")
    getData3=getPage(url)
    url=url.replace("/cr_60/#list", "/cr_80/#list")
    getData4=getPage(url)

    #print(len(getData1[2]))  #22位沒有送料資料
    #print(len(getData3[2])) #71位沒有送料資料
    #print(getData4[0])
    #合併1~5頁
    a=0
    for i in getData:    
        getData[a].extend(getData1[a])
        getData[a].extend(getData2[a])
        getData[a].extend(getData3[a])
        getData[a].extend(getData4[a])
        a=a+1


    #資料中不要的東西去掉
    Item_name=[]
    Item_price=[]
    Item_shipping=[]
    Item_shopname=[]

    for de in getData[0]:
        de=de.replace("\n                                ","")
        de=de.replace("                            ","")
        Item_name.append(de)
    
    for setin in getData[1]:
        Item_price.append(setin)
    
    for setin in getData[2]:
        Item_shipping.append(setin)
    
    for de in getData[3]:
        de=de.replace("\n                            ","")
        Item_shopname.append(de)
    """ 
    print(len(Item_name))
    print(len(Item_price))
    print(len(Item_shipping))
    print(len(Item_shopname))
    print(Item_shipping)
    """ 
    return Item_name,Item_price,Item_shipping,Item_shopname

def open_excel(getData):
    #放進EXCEL
    wb=load_workbook("getYahooRank.xlsx")
    setXlsx(wb,'B',getData[0])
    setXlsx(wb,'C',getData[1])
    setXlsx(wb,'D',getData[2])
    setXlsx(wb,'E',getData[3])

def setXlsx(wb,Row,getData):
    rows=2
    setSheet=wb.get_sheet_by_name('rank_sheet')
    for x in getData:
        ichi=Row+str(rows)
        setSheet[ichi]=x
        rows=rows+1
    wb.save("getYahooRank.xlsx")

while 1:
    order=menu()
    if order=="0/":
        break
    getData=deata_select(order)
    open_excel(getData)
    print("--------------------------------------")
    print("資料獲取完成，請開啟getYahooRank.xlsx複製資料。若再次執行資料會被覆愾。")
    t.sleep(3)
#https://shopping.yahoo.co.jp/ranking/#list
#https://shopping.yahoo.co.jp/ranking/cr_20/#list
#https://shopping.yahoo.co.jp/ranking/cr_60/#list
#https://shopping.yahoo.co.jp/ranking/cr_80/#list