from operator import truediv


num = 173
flag = False
if num > 1:
    for i in range(2, num):
        if(num % 1) == 0:
            flag = True
if(num % 2) == 0:
    print(num, "is  not a prime number")
else :
    print ("prime number")