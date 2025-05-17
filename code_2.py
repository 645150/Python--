# if语句
a=input("输入你的年龄\n")
a=int(a)
if a<0:
    print("输入错误")
else:
    if a<0:
        print("你逗我呢")
    elif 10<=a<=20:
        print("ss")
    else:
        print("s")

# while语句
while a>0:
    print("ss")
    a-=1
    if a%2!=0:
        continue

# for in语句
for i in range(10):
    if i==8:
        break
    print(i)
    
for i in [1,2,3,4,5]:
    print(i)