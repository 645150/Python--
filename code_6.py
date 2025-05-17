# 打开文件并写入内容.
f=open("D:\Project\Python\\test.txt",mode="w",encoding="utf-8") # 打开文件，mode为写入模式，encoding为编码格式，这俩参数可以省略不写。
f.write("This is a test file.\n")
f.seek(0)
f.close()

# 打开文件并输出文件内容.
f=open("D:\Project\Python\\test.txt",mode="r",encoding="utf-8")
print(f.read(4)) # 获取前4个字符
print(f.tell()) # 获取当前位置
print(f.read()) # 获得剩余所有内容
f.close()

""" 
mode参数：
'r'
打开文件进行读取。（默认）
'w'
打开文件进行写入。如果不存在则创建一个新文件，或者如果存在则将其截断。
'x'
打开文件以进行独占创建。如果文件已经存在，则操作失败。
'a'
打开以在文件末尾追加而不截断。如果不存在，则创建一个新文件。
't'
以文本模式打开。（默认）
'b'
以二进制模式打开。
 """
"""
f常用方法：
close()
关闭文件。
detach()
从缓冲区返回分离的原始流（raw stream）。
fileno()
从操作系统的角度返回表示流的数字。
flush()
刷新内部缓冲区。
isatty()
返回文件流是否是交互式的。
read()
返回文件内容。
readable()
返回是否能够读取文件流。
readline()
返回文件中的一行。
readlines()
返回文件中的行列表。
seek()
更改文件光标位置。
seekable()
返回文件是否允许我们更改文件光标位置。
tell()
返回当前的文件位置。
truncate()
把文件调整为指定的大小。
writeable()
返回是否能够写入文件。
write()
把指定的字符串写入文件。
writelines()
把字符串列表写入文件。 """