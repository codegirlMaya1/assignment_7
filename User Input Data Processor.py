#The aim of this assignment is to process and format user input data.
#Task 1: Input Length Validator Write a script that checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.
username = input("Enter First Name:")
signup=username
username1 = input("Enter Last Name:")
signup1=username

if len(signup)<2:
    print( "Please enter more than 2 characters.")
    
    if len(signup)>2:
        if len(signup1)<2:
            print( "Please enter more than 2 characters.")
    
    if len(signup1)>2:
        while True:
          continue

import re
#Task 2: Password Complexity Checker Create a function that checks the complexity of a user's password. The password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, and one number. 
def validate():
    while True:
        password =input("Enter a password: ")
        if len(password) < 8:
            print("Your password is invalid. It needs at least 8 characters....")
        elif re.search('[0-9]',password) is None:
            print(" Your password is invalid. It needs a number in it....")
        elif re.search('[A-Z]',password) is None: 
            print("Your password is invalid. It needs a capital letter in it....")
        elif re.search('[a-z]',password) is None:
           print(" Your password is invalid. It needs a lower letter in it....")  
        else:
            print("Your password is valid!")
            break

validate()
#Task 3: Email Formatter Implement a script that ensures all user email addresses are in a standard format.
pass

regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
emails = input(" Please enter a verified email ")
pass
if re.match(regex, emails):
    if (regex,emails):
            print(" Email is valid") 
else:
    email_1=input(" You just entered an invalid email. Would you like to try again in 15 minutes? Enter 1 for YES or 2 for NO!")
    
    if email_1 ==1:
        print("Good choice, please return in 15 min")
    else:
        print("Please return to the site after 15 minutes or whenever your ready to enter your verified email address....")
        
    