import requests
import json

res=requests.get("https://api.covid19api.com/world") #取得頁面資料存入res

content = res.content.decode() #decode()解碼

getJson=json.loads(content)

i=0
for item in getJson: #迴圈逐筆跑
    if(getJson[i]['TotalConfirmed']==222258826): #若TotalConfirmed為222258826
        print(getJson[i]['Date']) #則印出該筆Date
    i=i+1
    
