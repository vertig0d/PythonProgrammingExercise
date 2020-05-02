'''
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such 
that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

val = []
for item in range(1000, 3000):
    numb = list(map(int,str(item)))
    numb2 = list(map(lambda x: x%2, numb))
    if numb2.count(0) > 3:
        val.append(item)
print(val)
 