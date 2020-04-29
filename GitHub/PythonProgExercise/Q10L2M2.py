'''
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''

ip = input('Enter a sentence with repeated words: ')
#ipList = ip.split(' ')
op = list(set(ip.split(' ')))

#set() drawback is that it ordering of the element is lost, try it by commenting the sort line.
op.sort()
print(' '.join(op))