'''
Write a program which accepts a sequence of comma-separated numbers from console and generate a list 
and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
''' 
nums = input("Enter a series of numbers, comma sep: ")
#nums = 2,3,4,5
#lst = list(nums) this will work for python2 but not for python3. p3 input() results in string
# unlike in p2 where input() tries to find out the data type of i/p provided
#link for more info below
# https://stackoverflow.com/questions/4915361/whats-the-difference-between-raw-input-and-input-in-python-3
lst = nums.split(',') 
tup = tuple(lst)
print(lst)
print(tup)