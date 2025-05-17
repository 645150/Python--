# 类：self（this指针），__名称（私有属性），__init(self)__构造方法，静态属性，多继承，多态
class Person:
    name="张三"
    age="11"
    sex="男"
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def say_hello(self):
        print("你好，我是"+self.name+"，今年"+str(self.age)+"岁，性别"+self.sex)
    def work(self):
        None

class Dog:
    dog_name="张三"
    dog_age="11"
    def __init__(self,name,age):
        self.dog_name=name
        self.dog_age=age
    def bark(self):
        print("狗叫")

class 张三(Person,Dog):
    def __init__(self,age,sex):
        Dog.__init__(self,"狗张三", age) 
        super().__init__("张三",age,sex)
    def __吃鸡(self):
        print("张三正在吃鸡")
    def work(self):
        self.__吃鸡()
        print("张三在狗叫")

张三=张三(12,"男")
张三.say_hello()
张三.bark()
张三.work()
print(张三.dog_name)