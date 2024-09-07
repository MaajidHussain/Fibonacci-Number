import math
def is_perfectSquare(number):
    if number<0:
        return False
    squareRoot=int(math.sqrt(number))
    return squareRoot*squareRoot==number
def is_Fibonacci(num):
    return is_perfectSquare(5*num*num+4) or is_perfectSquare(5*num*num-4)
Number=int(input("Enter a number: "))
if is_Fibonacci(Number):
    print(f"{Number},is a Fibonacci number.")
else:
    print(f"{Number},is not a Fibonacci number")