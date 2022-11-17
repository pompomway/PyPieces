from openpyxl import load_workbook
from openpyxl import workbook
import datetime
import pandas as pd


"""
today=datetime.date.today()#取今天日期
tM=today.month #取月份
tD=today.day   #取日
FormatDay=(str(tM)+"月"+str(tD)+"日")
"""
#def csv_to_xlsx():
csv = pd.read_csv('202143.csv', encoding='Shift-JIS')
csv.to_excel('目標.xlsx', sheet_name='data')



wb=load_workbook(r"目標.xlsx")  
getSheet=wb.get_sheet_by_name('data')
"""
col=47
ichi="F"+str(col)
val=getSheet[ichi]
print(val.value==None)

"""
getOrderNum=[]#取得注文數
getCode=[]#取得商品code
col=3 #資料從第三行開始
"""
ichi=str(col)
val=getSheet["F"+ichi].value
print(val)
getSheet["F"+ichi].value=100
"""

while 1:
    ichi=str(col)
    Orderval=getSheet["F"+ichi].value #注文數
    Codeval=getSheet["C"+ichi].value #商品code
    """
    i=Codeval.count("-") #有幾個-
    for y in range(i-1): #跑-數量-1次,跑完只剩最後一個-
        i=Codeval.find("-") #找到第一個-
        Codeval=Codeval.replace("-", "",1) #把-去掉
    i=Codeval.find("-") #看-第幾位
    Codeval=Codeval[i+1:i+5]  #取出-後的字串
    print(Codeval)
    
    if Codeval.isdigit()==True: 
    """ 
    if Orderval==None:
        break
    else:
        i=Codeval.count("-") #有幾個-
        for y in range(i-1): #跑-數量-1次,跑完只剩最後一個-
            i=Codeval.find("-") #找到第一個-
            Codeval=Codeval.replace("-", "",1) #把-去掉
        i=Codeval.find("-") #看-第幾位
        Codeval=Codeval[i+1:i+50]  #取出-後的字串
        if Codeval.isdigit()==True:
            getSheet["F"+ichi].value=int(getSheet["F"+ichi].value)*int(Codeval)
        #getOrderNum.append(Orderval)
    #getCode.append(Codeval)
    col=col+1


wb.save("目標.xlsx")


wb.close()

