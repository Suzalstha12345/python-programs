a = float(input('enter first number: '))
b = float(input('enter second number: '))
c = float(input('enter third number: '))
if (a>b) and (a>c):
    temp = a
elif (b>a) and (b>c):
    temp = b
else:
    temp = c
print('the greatest number is', temp)