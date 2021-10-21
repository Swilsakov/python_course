a = int(input())
if a >= 100 and a < 1000:
	print ('yes')
else:
	print ('no')
if a%2 == 0 and a > 0:
	print ('poloj i cetnoe')
else:
	print ('ne cetnoe')
if a%31 == 0:
	print ('withoiut ostatok')
else:
	print ('ostatok')
if a > 100 and a%17==0 or a > 150 and a == 13**2:
	print('yes')
