l = [1,2,3,4,5,6]
n = len(l)
for i in range(n):
    if i % 2 != 0:
        l.remove(i)
print(l)

