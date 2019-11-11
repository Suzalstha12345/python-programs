n = 0
while n < 5:
    print(n)
    if n == 2:
        break
    n = n + 1

for i in range(5):
    print(i)
    if i == 2:
        break

#find out whether a num is prime or not
n = int(input('enter n:'))
ans = True
for i in range(2,n):
    if n % i == 0:
        ans = False
        break
print(ans)

