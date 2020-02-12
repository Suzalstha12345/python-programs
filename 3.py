#write a recursive python function that returns the sum of first n integers

def getSum(S):
    if len(S) == 0:
        return 0
    else:
        return S[0] + getSum(S[1:])
print (getSum([1, 3, 4, 2, 5]))
