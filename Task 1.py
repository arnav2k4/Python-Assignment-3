def Factorial(n):
    if n == 0:
        return 1
    n *= Factorial(n-1)
    return n

num = int(input("Enter a number: "))
print("Factorial of {} is: {}".format(num, Factorial(num)))
