import pymysql

conn=pymysql.connect(host="localhost",user="Pom",passwd="123456",db="pom",charset="utf8")
cur=conn.cursor()

def login_menu1_out():
    print("***************************")
    print("歡迎使用會員系統，請選擇:")
    print("-------------------------")
    print("1.登入")
    print("2.新增會員")
    print("3.結束")
    

def login_menu2_out():
    print("請選擇執行項目:")
    print("-------------------------")
    print("1.查詢會員資料")
    print("2.修改會員資料")
    print("3.刪除會員資料")
    print("4.登出")
    

def menu1_cho():  
    while 1:
        login_menu1_out()
        cho=eval(input())
        if cho==1: 
            print("進入登入畫面") #OK
            login()
        elif cho==2:
            print("新增會員畫面") #OK
            save()
        elif cho==3:
            print("結束程式") #OK
            break
        else:
            print("輸入錯誤，請重新輸入")
            


        
        
    


def menu2_cho():
    while 1:
        login_menu2_out()
        cho=eval(input())
        if cho==1:
            print("查詢會員資料") #OK
            getData()
        elif cho==2:
            print("修改會員資料")
            update()
        elif cho==3:
            print("刪除會員資料") #OK
            delete()
        elif cho==4:
            print("登出，回前頁") #OK
            break
        else:
            print("輸入錯誤，請重新輸入")
            
 ############################################################ 
            
def update():
    while 1:
        print("請輸入欲修改帳號，或輸入0退出")
        idd=input()
        if idd=="0" : break
        sql_get="SELECT * FROM `sf` WHERE `sf_account`='"+idd+"' and sf_del=0 "
        cur.execute(sql_get)
        data=cur.fetchone()
        if data==None:
            print("此帳號不存在")
            continue
        print("請輸入使用者新名字:")
        name=input()
        print("請輸入新密碼:")
        pw=input()
        print("請再次輸入密碼:")
        pw2=input()
        if pw!=pw2:
            print("兩次輸入不同密碼，請重新輸入")
            continue
        sql_update="UPDATE `sf` SET `sf_name`='"+name+"',`sf_password`='"+pw+"' WHERE `sf_account`='"+idd+"'"
        cur.execute(sql_update)
        conn.commit()
        print("修改完成，請以新密碼登入")
        
            
    
def getData():
    sql_get="SELECT `sf_name`,`sf_account`,`sf_password`,`sf_level` FROM `sf` WHERE `sf_del`=0"
    cur.execute(sql_get)
    data_staff=cur.fetchall()
    print("員工資料")
    for x in data_staff:
        print(x)
    conn.commit()
    return
    
def login():
    a=3
    while 1:
        print("請輸入帳號:")
        idd=input()
        print("請輸入密碼:")
        pw=input()
        sql="SELECT * FROM `sf` WHERE `sf_account`='"+idd+"' and sf_del=0"
        cur.execute(sql)
        data=cur.fetchone()
        if data==None or pw not in data or idd=="" or pw=="":
            print("帳號或密碼錯誤，您還有"+str(a)+"次輸入機會")
            conn.commit() #位置注意
            a=a-1
            if a==0:
                break
            else:
                continue
        else:
            menu2_cho()
            break
            

        
def save():
    while 1:
        print("請輸入姓名:")
        name=input()
        if name=="":break
        print("請設定帳號:")
        idd=input()
        if idd=="":
            break
        elif idd=="0":
            print("帳號不得設定為0")
            break
        sql="SELECT sf_account FROM `sf` WHERE sf_account='"+idd+"' and sf_del=0"
        cur.execute(sql)
        data=cur.fetchone()
        if data!= None:
            print("此帳號已存在")
            continue
        print("請設定密碼:")
        pw=input()
        if pw=="":break
        sql_into="INSERT into `sf` (`sf_name`,`sf_account`,`sf_password`)values('"+name+"','"+idd+"','"+pw+"')"
        cur.execute(sql_into)
        conn.commit()
        print("{}註冊成功".format(idd))
        break

def delete():
    while 1:
        print("請輸入要刪除的帳號ID或輸入0回上一層")
        idd=input()
        if idd=="" or idd=="0": break
        sql="SELECT sf_account FROM `sf` WHERE sf_account='"+idd+"' and sf_del=0"
        cur.execute(sql)
        data=cur.fetchone()
        if data==None :
            print("此帳號不存在")
            continue
        print("確定要刪除帳號"+idd+"嗎?，(Y/N)")
        check=input()
        if check=="Y" or check=="y":
            sql_de="DELETE FROM `sf` WHERE `sf_account`='"+idd+"' and sf_del=0"
            cur.execute(sql_de)
            conn.commit()
            print(idd+"已刪除")
            break


menu1_cho()
            