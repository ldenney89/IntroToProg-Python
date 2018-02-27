#-------------------------------------------------#
# Title: Python Pickling Example
# Dev:   LDenney
# Date:  February 26, 2018
# ChangeLog: (Who, When, What)
#   Laura Denney, 2/26/18, Created File
#-------------------------------------------------#

#---Data------------------------------------------------------
FILENAME = "Pickle.dat" #Constant for file name
userOption = None #user menu option choice
lstTableData = [] #table of product lists
lst = [] #stores a products ID, name, price
#---Processing------------------------------------------------------
def ShowOptions():
    print("""
    Menu:
    1 - Add Product Data to list
    2 - Save list to File
    3 - Load list from File
    4 - Exit
    """)
def getUserOption():
    option = input("Please pick a number based on what you'd like to do: ")
    return option
def addData():
    productId = int(input("What is the product ID: "))
    productName = input("What is the product Name: ")
    productPrice = input("What is the product Price: ")
    lstData = [productId, productName, productPrice]
    return lstData
def OpenReadData(File):
    objFile = open(File, "rb")
    Datalst = pickle.load(objFile)
    objFile.close()
    return Datalst
def SaveData(File, Data):
    objFile = open(File, "wb")
    pickle.dump(Data, objFile)
    objFile.close()

#---Presentation-----------------------------------------------------
import pickle

print("This program makes a list of product IDs, product names and product prices.\n\
It can also store this list for future use. ")
while(True):
    ShowOptions()
    userOption = getUserOption()
    if userOption == "1": #add items to list
        lst = addData()
        lstTableData.append(lst)
        print(lst, "added.")
    elif userOption == "2": #save list to file
        SaveData(FILENAME, lstTableData)
        print(lstTableData, "saved to file.")
    elif userOption == "3": #load list from file
        lstTableData = OpenReadData(FILENAME)
        print("Here is the current list:", lstTableData)
    elif userOption == "4": #exit
        break
    else:
        print("Please choose a valid option.")
print("Thank you. Goodbye.")