import pymysql

#MySQL有可能防誤刪誤改機制，需要用下方語法關閉該機制
#set SQL_SAFE_UPDATES=0;

conn=pymysql.connect(host="localhost",user="root",passwd="123456",db="dbconnection",charset="utf8")
cur=conn.cursor()

#######################################################修改
def upData():
    print("------------請輸入要修改的單號-----------")
    num=input("單號:")
    sql="SELECT num,start,end,name,phone FROM dbconnection.order where num='"+num+"';"
    cur.execute(sql)
    data=cur.fetchall()
    print("目前資料:")
    for i in data:
        print(i)
    print("-----------請輸入-----------")
    start=input("起點:")
    end=input("迄點:")
    name=input("名字:")
    phone=input("電話:")
    sql="update dbconnection.order set start='"+start+"',end='"+end+"',name='"+name+"',phone='"+phone+"' where num='"+num+"';"
    cur.execute(sql)
    conn.commit()
    print("修改完成")
    cur.close()
    conn.close()
#######################################################刪除
def deData():
    print("------------請輸入要刪除的單號-----------")
    num=input("單號:")
    print("確定要刪除嗎?"+"\n"+"1.確認刪除 2.取消刪除")
    cho=input()
    if cho=="":
        print("輸入錯誤")
    elif cho=="2":
        print("取消刪除")
    elif cho=="1":
        sql="delete from dbconnection.order where num='"+num+"';"
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        print(num+"已刪除")
    else:
        print("輸入錯誤")
    

###################################################新增
def saveData():
    print("-----------請輸入-----------")
    num=input("單號:")
    start=input("起點:")
    end=input("迄點:")
    name=input("名字:")
    phone=input("電話:")
    sql="insert into dbconnection.order(num,start,end,name,phone)value('"+num+"','"+start+"','"+end+"','"+name+"','"+phone+"')"
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
###################################################查詢&修改
def getData():
    print("-----------請選擇-----------")
    print("以1.單號 2.名字 3.電話 查詢")
    cho=input()
    if cho=="1":
        wh=input("輸入單號:")
        cond="num="+"'"+wh+"'"
    elif cho=="2":
        wh=input("輸入名字:")
        cond="name="+"'"+wh+"'"
    elif cho=="3":
        wh=input("輸入電話(需加入-):")
        cond="phone="+"'"+wh+"'"
    elif cho=="":
        print("輸入錯誤")
    else:print("輸入錯誤")
    #print(cond)
    sql="SELECT num,start,end,name,phone FROM dbconnection.order where "+cond+";"
    cur.execute(sql)
    data=cur.fetchall()
    for i in data:
        print(i)

    print("是否要更改資訊?"+"\n"+"1.是 2.否")
    upcho=input()
    if upcho=="" :
        print("輸入錯誤")
    elif upcho=="1":
        print("進入修改")
        upData()
    elif upcho!="2" or upcho!="1" :
        print("輸入錯誤")
        
    cur.close()

###################################################主菜單
def menu():
    print("下單系統")
    print("-----------請選擇-----------")
    print("1.查詢"+"\n"+"2.新增"+"\n"+"3.修改"+"\n"+"4.刪除")
    cho=input()
    if cho=="1":
        print("進入查詢"+"\n")
        getData()
    elif cho=="2":
        print("進入新增"+"\n")
        saveData()
    elif cho=="3":
        print("進入修改"+"\n")
        upData()
    elif cho=="4":
        print("進入刪除"+"\n")
        deData()
    elif cho=="":
        print("未輸入")   
    else:
        print("輸入錯誤")

while 1:
    menu()
    a=input("輸入任意見繼續，輸入0結束")
    if a=="0":
        break
    elif a=="":
        continue
    else:
        continue
