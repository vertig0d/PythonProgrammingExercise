"""
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""
#Method 2
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

num = input("Enter a number:")
print(fact(num))