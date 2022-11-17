listA=[1,2,3,4,5]
classA={"1":"A","2":"B","3":"C","4":"D","5":"E",}
# print(type(classA))
# print(classA["1"])

num=input()
try: #嘗試做以下
    float(num) #若num不是數值，會在這邊轉型失敗，直接跳到except
    print("TODO")#計算
except:
    print('Error')#不計算
    
#isdigit()會判斷該變數是否為數字然後返回boolean
# print(type(num))#這行可以看判斷結果
# if num.isdigit():
#     print("計算")
# #以下可省略 
# else:
#     print("不計算")


