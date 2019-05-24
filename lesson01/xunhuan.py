#打印0-9的数字
# i = 0 
# while i <10:
# 	print(i)
# 	i = i + 1
#range(start,end,step)  step步长
# for i in range (0,10,2):
# 	print(i)
# ---------------------------------------
# for i in range(0,100):
	
# 	#如果条件满足，continute下面的代码不会被执行，会继续循环
# 	if i <40:
# 		continue
# 	#%是数学的取模操作，结果未0是偶数	
# 	if i % 2==0 :
# 		print(i)
# 		#如果条件满足，循环退出不再执行
# 	if i >=79:
# 		break
for i in range(0,5):
	if i >3:
		continue
	if i >3:
		break
	print(i)
else:
	print("循环没有被打断！")