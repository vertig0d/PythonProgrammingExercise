'''
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''

digits = []
numbs = ['1','2','3','4','5','6','7','8','9','0']
print('Enter a sentence with numbers: ')
ip = input().split(' ')
for item in ip:
    if numbs in item:
        digits.append(item)
        ip.remove(item)
print('LETTERS ',len(ip))
print('DIGITS ', len(digits))