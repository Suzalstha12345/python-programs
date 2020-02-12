#Write a recursive function to check if the string is palindrome or not

def reverse(s):
    return s[::-1]

def isPalindrome(s):
    rev = reverse(s)

    if (s == rev):
        return True
    return False

s = "tat"
ans = isPalindrome(s)

if ans == 1:
    print("Yes")
else:
    print("No")


