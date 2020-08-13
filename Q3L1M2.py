
"""
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such 
that is an integral number between 1 and n (both included). and then the program should print the 
dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""
#Method2

num = input("Enter a number: ")
dicti = dict() 
key = range(1, num + 1)
value = map(lambda x: x * x, key) 
final = map(lambda k,v : dicti.update({k:v}), key, value)
print(dicti)