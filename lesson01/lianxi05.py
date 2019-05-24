#回文：两边对称"abccba"

for i in "abcde":
	print(i)
print("abcde"[0])
print("abcde"[-1])
print("abcde"[-4])

data= input("请输入")
#len函数返回字符窜长度
for i in range(len(data)):
	#判断如果字符窜前后不一致则不是回文
	if data[i]!==data[-(i+1)] 
		print("{0}不是回文".format(data))
		break
else:
	print("字符窜{0}是回文！".format(data))