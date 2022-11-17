

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


def yRankIn():
    while 1:
        order=menu()
        
        if order=="0/":
            break
        #getData=deata_select(order)
        #open_excel(getData)
        print("--------------------------------------")
        print("資料獲取完成，請開啟getYahooRank.xlsx複製資料。若再次執行資料會被覆愾。")
        t.sleep(3)