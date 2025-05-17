# list列表嵌套与反向下标（相当于c++的vector）
list=[[1,2,3],[4,5]]
print(list[-1]) #-1表示list的倒数第1个容器，即[4，5]
# list的常用函数
print(len(list)) # 求长度用len()函数
print(len(list[0]))

# tuple元组（相当于c++的const修饰的vector）
tuple=((1,"122",1),("slope",1))
print(tuple[-1][0])
# tuple的常用函数
print(len(tuple)) # 求长度用len()函数
print(len(tuple[0]))
print(tuple[0].count(1)) # count()函数，求1出现的个数
print(tuple[0].index("122")) # index()函数，求"122"的索引值

# str字符串
str="123abcde"
print(str[-1],str[-2])
# str的常用函数
print(len(str)) # 求长度用len()函数
print(str.replace("123","我是李刚")) # replace()函数
print(str.split("a")) # split()函数
print(str.index("a")) # index()函数
print(str.count("1")) # count()函数
print(str.strip()) # strip()函数，移除首尾空格和换行符
print(str.strip("123")) # strip()函数，移除特定字符串
# 格式化字符串format()函数
# 默认（隐式）顺序
print("{}, {} and {}".format('John','Bill','Sean'))
# 使用位置参数排序
print("{1}, {0} and {2}".format('John','Bill','Sean'))
# 使用关键字参数的排序
print("{s}, {b} and {j}".format(j='John',b='Bill',s='Sean'))

# 序列（指list，tuple，str这些有序集合）的拷贝
print(str[4::2])
print(str[::2])

# set集合
set={1,2,3}
set.add(1)
print(set)
set.remove(2)
print(set)
print(set.pop())
set.clear()
print(set)

# dict字典(相当于json数据)
dict={"张三":[1,2,3],"李四":[4,5,6]}
print(dict["张三"])