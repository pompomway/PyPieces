import requests
import pandas
a=1
req=requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")

dfs=pandas.read_html("https://rate.bot.com.tw/xrt?Lang=zh-TW")
#print(req.text)
#print(type(dfs[0]))
