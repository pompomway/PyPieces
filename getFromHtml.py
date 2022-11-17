import requests
from lxml import etree

#取得博客來首頁存入res
res=requests.get("http://www.books.com.tw") 
#res2=requests.get("https://shopping.yahoo.co.jp/") #yahoo

#回覆Response [200] 代表請求得到許可
print(res) 
#取得回應內容，中文字都是unicode呈現
print(res.content) 

#decode()解碼，不傳入參數則以預設UTF-8解碼
content = res.content.decode() 
print(content)
