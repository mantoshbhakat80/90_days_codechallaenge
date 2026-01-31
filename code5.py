# wap to input a number and check if it is a palindrome number or not.
n = int(input("Enter a number:"))
def is_palindrome(num):
    or_num = num
    rev_num = 0
    while num > 0:
        digit = num % 10
        rev_num = rev_num * 10 + digit
        num = num // 10
    return or_num == rev_num
if is_palindrome(n):
    print(f"{n} is a palindrome number.")
else:
    print(f"{n} is not a palindrome number.")