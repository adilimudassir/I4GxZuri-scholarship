"""
This file is part of the tasks for the Counting Words. It is part of the tasks/projects carried out in 
the I4GxZuri Scholarship in the Fullstack Track.


Author: Mudassir Adili Ahmad (adilimudassir)
Date: 2022-05-16
"""

#count and return the number of words in a string
def count_words(string):
    """
    This function is the main function of the Counting Words task. It takes one argument:
    string - the string to be counted
    and returns the number of words in the string.
    """
    #split the string into words
    words = string.split()
    #return the number of words
    return len(words)

#call method
print(count_words('Hello world!'))