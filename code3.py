# wap to input a number and check if it is a armstrong number or not.
n = int(input("Enter a number:"))
t = n
s = 0
while n>0:
    r = n%10
    s = s+r**3
    n = n//10
if s == t:
    print(f"{t} is an armstrong number.")
else:
    print(f"{t} is not an armstrong number.")