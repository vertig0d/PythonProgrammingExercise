'''
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''

digits = []
words = []
print('Enter a sentence with numbers: ')
ip = input()
for item in ip:
    if item.isdigit():
        digits.append(item)
    #you need to mention the item is alpha otherwise the count is incorrect
    elif item.isalpha():    
        words.append(item)
print('LETTERS ',len(words))
print('DIGITS ', len(digits))