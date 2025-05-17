# 函数语句
def dfs(x,y,m,n):
    if x == m and y == n:
        return True
    if x+1<=m:
        return dfs(x+1,y,m,n)
    if y+1<=n:
        return dfs(x,y+1,m,n)
print(dfs(0,0,-1,1))

# 多返回值
def a():
    return 1,2
x,y=a()
print(f"x:{x}")
print(f"y:{y}")

# 键值对/缺省值传参
def b(name,age,gender='男'):
    print(f"名字：{name},年龄：{age},性别：{gender}")
b("nima",age=11)

# global关键字(定义在函数内)
num=100
def fun(x):
    global num
    num+=x
x=input("输入x\n")
x=int(x)
fun(x)
print(num)

# 位置传参
def func(*args):
    print(args[0])
func("sss",1)

# 关键字传参
def func(**name_args):
    print(f"名字：{name_args.get('name')}，年龄：{name_args.get('age')}")
func(name="我是李刚",age=18)

# lambda函数和函数参数
def add(z,x,y):
    return z(x,y)
result=add(lambda a,b:a+b,x=1,y=2)
print(result)