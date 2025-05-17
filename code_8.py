# 异常与自定义异常
class MyException(Exception):
    pass # 空类

try:
    raise MyException("This is a custom exception") # raise语句强制抛出异常
except MyException as e:
    print(e)
except:
    print("Caught a non-custom exception") # 多个except语句只能执行一个，所以这里只会执行第一个except语句
finally:
    print("This is the finally block") # finally语句总会执行，无论是否有异常发生