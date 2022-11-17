import pymysql

conn=pymysql.connect(host="localhost",user="root",passwd="123456",db="dbconnection",charset="utf8")
cur=conn.cursor()#生成游標對象
#查詢
sql="SELECT num,start,end,name,phone FROM dbconnection.order;"
cur.execute(sql)#放入sql語法
data=cur.fetchall()#撈資料


#for i in data[:1]:
#    print(i[0])

for i in data:#迴圈讀取
    print(i)


#新增
sql="insert into dbconnection.order(num,start,end,name,phone)value('P1201','台北','台南','王大槌','02-1234-5678');"
cur.execute(sql)#放入sql語法
conn.commit()#儲存(想像成MySQL的閃電按鈕)
cur.close()
conn.close()