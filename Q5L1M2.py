'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''
class MyClass:
    def __init__(self):
        self.val = ''

    def getString(self):
        self.val = input('Enter a string: ')    

    def printString(self):
        print('No i/p value provided') if len(self.val) == 0 else print(self.val.upper())    

x = MyClass()
x.getString()
x.printString()        