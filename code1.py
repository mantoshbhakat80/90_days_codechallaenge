# WAP to create a dictionary where keys are numbers and values are squares of numbers.
def create_square(n):
    square_dict = {}
    for i in range(1,n+1):
        square_dict[i] = i**2
    return square_dict

num = int(input("Enter a number:"))
re = create_square(num)
print(re)
