"""
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""
#Methhod1
def fact(n):
    i = 1
    for val in n:
        i = i * val
    return i

input_num = input("Enter a number to compute factorial:") 
#input_num = 5
print(fact(list(range(1, input_num + 1))))