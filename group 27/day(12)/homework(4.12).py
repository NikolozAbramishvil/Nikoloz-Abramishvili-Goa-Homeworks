num=input()
num1=input()
num3=input()
if num + num1 > num3 and num + num3 > num1 and num3 + num1 > num:
    print(True)
else:
    print(False)