import code_5 # 导入自己写的模块
import math# 导入math模块(内置模块)
import geometry.test as g # 导入geometry模块(自己写的模块)

李四 = code_5.Person("李四", 25, "男") # 创建Person对象
李四.say_hello()

print(math.pi) # 调用math模块的pi属性
print(g.test()) # 调用geometry模块的函数