#=============================================================================#
#
#    File:   number.py
#    Author: Jack Morgan
#    Date:   May 2021
#    Description:
#        Contains the class Number
#        Number class inherited by other number system classes
#
#=============================================================================#


class Number:

    def __init__(self, number):
        self.number = number

    def __str__(self):
        print(self.number)
