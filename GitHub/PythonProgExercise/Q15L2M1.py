'''
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
Then, the output should be:
11106
'''

i = 1
b = 0
a = input()
while(i < 5):
    c = int(a * i)
    b += c
    i += 1
print(b)    