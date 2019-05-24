
total,fenzi,fenmu=0,2,1
for i in range(0,20):
	
	total=total +fenzi/fenmu
	#这里先使用tmp保存删一个fenzi值，后面计算新fenzi值回更新fenzi
	# tmp=fenzi
	# fenzi=fenmu+fenzi
	# fenmu=tmp
	#同一行用都好分隔的变量可同时计算
	fenzi,fenmu =fenzi+fenmu,fenzi
print(total)

