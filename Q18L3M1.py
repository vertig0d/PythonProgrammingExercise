'''
Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:


Then, the output of the program should be:
ABd1234@1

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

import string
vaild_char = ['$','@','#']
final_arr =[]
low_char_arr = [char for char in string.ascii_lowercase]
cap_char_arr = [char for char in string.ascii_uppercase]
arr = input().split(',')
for item in arr:
	if not ((len(item) > 5) and (len(item) <13)):
		continue
	arr2 = list(item)
	check1 = any(val in arr2 for val in low_char_arr)	
	check2 = any(val in arr2 for val in cap_char_arr)
	check3 = any(val in arr2 for val in vaild_char)
	check4 = any(val in arr2 for val in str(range(0,10)))
	if check1 is False:
		continue
	if check2 is False:
		continue
	if check3 is False:
		continue
	if check4 is False:
		continue
	final_arr.append(item)
print(final_arr)
