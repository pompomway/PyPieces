a=["sddsfas","asdfg-3","assewcfdsa-12","ds--weff-a1","ssd-sda-3","fs-3106b"]
b=[10,2,7,9,1,3]
c=[]
n=0
for x in a:
    i=x.count("-") #有幾個-
    for y in range(i-1): #跑-數量-1次,跑完只剩最後一個-
        i=x.find("-") #找到第一個-
        x=x.replace("-", "",1) #把-去掉
    i=x.find("-") #看-第幾位
    x=x[i+1:i+10]  #取出-後的字串
    if x.isdigit()==True: 
        b[n]=b[n]*int(x)
    n=n+1

print(b)
        

