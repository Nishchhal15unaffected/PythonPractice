import random
r=random.randint(1,20)
while(True):
	print("enter the number")
	h=int(input())
	if(h>r):
		print("wrong guues dear your number is greater try again")
	elif(h<r):
		print("wrong guees dear your number is less try again")
	else:
		print("Congretss right gues dear your number is equel ")
		break;	