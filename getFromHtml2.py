#爬博客來排行榜
import requests
from lxml import etree
import openpyxl

#User-Agent使用者代理，向對方表示自己透過瀏覽器發出請求
#google chromet查詢代理:瀏覽器輸入about:version
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
res=requests.get("http://www.books.com.tw/web/sys_hourstop/home?loc=P_003_001",headers=headers)
content=res.content.decode()
#print(content) 可讀取出該網頁html的src
#至此資料取得結束，以下開始處裡

#使用etree.HTML()載入html，etree的選擇器可獲取想要的內容
html=etree.HTML(content)
#XPATH F12先找到想獲取的目標>右鍵>copy>copy full xpath
#取下來後要顯示字串所以最後面加上text()
name=html.xpath('/html/body/div[4]/div/div[2]/div[1]/div/div[1]/ul/li/div[2]/h4/a/text()')
#print(name) #印出所有書名

#以下兩個範例為單書名和所有書名的差別，所有書名存在li下面，所以不指定元素即可取得所有書名。
#//body/div[4]/div/div[2]/div[1]/div/div[1]/ul/li[1]/div[2]/h4/a
#//body/div[4]/div/div[2]/div[1]/div/div[1]/ul/li/div[2]/h4/a

#該網站在價格前會標折數，並且標籤為strong，其中最後一個strong才是真正的價格，所以把strong[2]改成strong[last()]
sell=html.xpath('/html/body/div[4]/div/div[2]/div[1]/div/div[1]/ul/li/div[2]/ul/li[2]/strong[last()]/b/text()')
print(sell)
