#-------------------------------------------------#
# Title: Python Exception Handling
# Dev:   LDenney
# Date:  February 26, 2018
# ChangeLog: (Who, When, What)
#   Laura Denney, 2/26/18, Created File
#-------------------------------------------------#

#---Data------------------------------------------------------
value1 = None #holds first number
value2 = None #holds second number
userContinue = None  #holds askcontinue return
#---Processing------------------------------------------------------

def GetNumbers():
    try:
        n1 = int(input("Number 1: "))
        n2 = int(input("Number 2: "))
        return n1, n2
    except TypeError as e: #catches when n1 or n2 are not numbers
        print("Please pick a number.")
    except Exception as e:
        print("Python reported the following error: " + str(e))
def AddNumbers(v1, v2):
    try:
        return v1 + v2
    except Exception as e:
        print("Python reported the following error: " + str(e))
def SubtractNumbers(v1, v2):
    try:
        return v1 - v2
    except Exception as e:
        print("Python reported the following error: " + str(e))
def MultiplyNumbers(v1, v2):
    try:
        return v1 * v2
    except Exception as e:
        print("Python reported the following error: " + str(e))
def DivideNumbers(v1, v2):
    try:
        return v1 / v2
    except ZeroDivisionError as e: #catches when v2 is 0
        print("Error, cannot divide by zero!")
    except Exception as e:
        print("Python reported the following error: " + str(e))
def AskContinue():
    try:
        return input("Press enter to choose more numbers, type exit to exit.")
    except Exception as e:
        print("Python reported the following error: " + str(e))
#---Presentation-----------------------------------------------------
while not userContinue:
    try:
        print("\nPlease pick two numbers.")
        value1, value2 = GetNumbers()
        print("For the values", value1, "and", value2)
        print("The sum is:", AddNumbers(value1, value2))
        print("The difference is:", SubtractNumbers(value1, value2))
        print("The product is:", MultiplyNumbers(value1, value2))
        print("The quotient is:", DivideNumbers(value1, value2))
        userContinue = AskContinue()
    except Exception as e:
        print("Python reported the following error: " + str(e))
print("That was fun!")