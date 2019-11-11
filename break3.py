#find thr prime numbers of a certain range
#and put them in a list
primes = [] #empty list
n = int(input('enter the range'))
for n in range(2,n):
    ans = True
    for i in range(2,n):
        if n % i == 0:
            ans = False
            break
    if ans == True:
         primes.append(n)  #add to list if prime

print(primes)
