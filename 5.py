#Recursive program to check if the number is palindrome or not

def rev(n, temp):
    if (n == 0):
        return temp;

    temp = (temp * 10) + (n % 10);

    return rev(n / 10, temp);

n = 353;
temp = rev(n, 0);

if (temp != n):
    print("yes");
else:
    print("no");

