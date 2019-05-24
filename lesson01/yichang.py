
# data=int(input("请输入一个数字：")) 
# try:
# print(data/0)
# print("这里没有被执行1")
# except ZeroDivisionError:
# 	pass
# 	print("这里被执行")
# finally：
# print("这里肯定被执行了")
# 
file = open("bigcat.txt",encoding="utf-8")
try:
	#file.write("可定会出问题")
	filed.read()
except Exception:
	print("这里发生了异常")
	
finally:
	file.close()