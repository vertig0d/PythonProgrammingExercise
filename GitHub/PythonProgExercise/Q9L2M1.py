'''
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''

print('Enter multi line sentence: ')
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = "\n".join(lines)
print(text.upper())        