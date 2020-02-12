s = input("Input a string")
d = 0
v = 0
for c in s:
    if c.isdigit():
        d = d+1
    elif c.isalpha():
        v = v+1
    else:
        pass
print("Letters", v)
print("Digits", d)
