"""
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
lst = list(range(2000,3200))
final_lst = list(filter(lambda x: (x % 7 == 0 and x % 5 != 0), lst))
print(final_lst)