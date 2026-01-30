# wap to input a number and check if it is a twin prime number or not.
n = int(input("Enter a number:"))
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
if is_prime(n) and is_prime(n + 2):
    print(f"{n} is a twin prime number.")
else:
    print(f"{n} is not a twin prime number.")
    