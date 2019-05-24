#有1、2、3、4个数字，能组成多少互不相同且无重复数字的三位数？都是多少
count  = 0 
#i代表百位
for i in range(1,5):
#j代表十位
	for j in range(1,5):
#h代表个位
		for h in range(1,5):
#各位，百位和十位不能重复
			if i==j or j==h or h==i:
				continue
			count=count +1
			print("{0}{1}{2}".format(i,j,h))
print(count)