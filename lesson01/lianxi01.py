#输入输出
#引号里面的内容是字符窜
# print("你好世界！")
# #没有加引号是数字
# print(3.1415926)
# type函数用来判断数据类型
# print(type("你好世界！"))
# print(type(3.1415926))
# print(input("请你输入数字："))
# print(type(input("请你输入")))
# print(type(float(input("请你输入数字"))))
# str是字符窜，int是整形，float是小数
# i=int(input("请你输入数字"))
# print(i*"你好世界！")
# 注释快捷键 ctrl+？

#只有字符窜才有format方法
#字符窜格式化
#format函数用于格式化，可以填充数据
template= "我是{},今年{},喜欢{}"
print(template.format("小花",99,"py"))
#####################################################

#文件读写操作
#打开文件读取内容个，第一个是文件名，第二个是文件编码
file = open ("lianxi01.py",encoding='utf-8')
print(file.read())
file.close()

data = '''
	*
   ***
  *****
	'''
	#写入文件，第一个是文件名，第二个是打开模式，不写为‘r’读取，写文件需要w
# file = open ("bigcat.txt",mode='w',encoding='utf-8')
# file.write(data)
# file.close()

data = input("请输入:")
file = open("bigcat.txt",mode='w',encoding='utf-8')
file.write(data)
file.close()
