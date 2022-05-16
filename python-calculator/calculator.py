"""
This file is part of the tasks for the Python-calculator project. It is part of the tasks/projects carried out in 
the I4GxZuri Scholarship in the Fullstack Track.


Author: Mudassir Adili Ahmad (adilimudassir)
Date: 2022-05-16
"""

#calculator function
def calculator(a, b, c):
    """
    This function is the main function of the calculator project. It takes three arguments:
    a - the first number
    b - the second number
    c - the operator
    and returns the result of the operation.
    """
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        return a / b
    else:
        return 'Invalid operator'
    
#main function
def main():
    """
    This function is the main function of the calculator project. It takes no arguments and returns nothing.
    """
    #get the first number
    a = float(input('Enter the first number: '))
    #get the second number
    b = float(input('Enter the second number: '))
    #get the operator
    c = input('Enter the operator: ')
    #get the result
    result = calculator(a, b, c)
    #print the result
    print('The result is: ', result)


#call the main function
if __name__ == '__main__':
    main()

