
#这里是总收入，不用考虑五险一金
salary=float(input("应纳所得税"))
#个税从3500征税，不够3500不扣税

level = salary - 3500
if level >=80000:
	tax = level*0.45 - 13505
elif level >=55000:
	tax = level*0.35 - 5505
elif level >=35000:
	tax = level*0.30 - 2755
elif level >=9000:
	tax = level*0.25 - 1005
elif level >=4500:
	tax = level*0.20 - 555
elif level >=1500:
	tax = level*0.10 - 105
elif level >=0:
	tax = level*0.03
else:
	tax = 0
	
print("应缴纳税总额为{0}".format(tax))