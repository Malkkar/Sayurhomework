from datetime import date
def initializeUser():
    global dob
    
    name=input("enter your name")
    year = int(input('Enter a year: '))
    month = int(input('Enter a month: '))
    day = int(input('Enter a day: '))
    dob = date(year, month, day)
def calculatAge(dob): 
    global amount   
    currentdate=date.today()
    age=(currentdate-dob)//365
    age=age.days
    if (age<=18):
        amount=750
    elif (age>18) and (age<60):
        amount=600
    else:
        amount=400
    
def offer():
 global discountAmount
 discountAmount=amount-100
    
initializeUser()
calculatAge(dob)
offer()
today=input("enter today")
if today=="thursday" or today=="tuesday":
   print("your ticket price is",discountAmount)
else:
   print("your ticket price is",amount)
