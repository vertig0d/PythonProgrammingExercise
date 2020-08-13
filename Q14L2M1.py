'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case 
letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''

lower = 0
upper = 0
print('Enter a sentence: ')
ip = input()
for item in ip:
    if item.islower():
        lower += 1
    elif item.isupper():
        upper += 1
print('Upper Case: ', upper)
print('lower case: ',lower)             