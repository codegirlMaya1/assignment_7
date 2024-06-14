#Objective:The aim of this assignment is to create an interactive help desk bot that processes user queries and responds appropriately for a SaaS application.
#Task 1: Command Parser Write a script that takes a user's text input and identifies if it contains one of the predefined commands (e.g., "help", "issue", "contact support"). If a command is found, print a response related to the command.

user_words = ("help", "issue", "support")
user_words1=("issue")
user_words2= ("login")
user_words3=("performance")
user_words4=( "support")
category=["login", "performance","support"]

#Task 1: Command Parser Write a script that takes a user's text input and identifies if it contains one of the predefined commands (e.g., "help", "issue", "contact support"). If a command is found, print a response related to the command.

user_input = input(" What do you need help with? Type your message for assistance: ")

if any(i in user_words for i in user_input.split()):
    print("Your concern has been received. The best solution is to call support at 555-555-5555 between 9am-5pm Mon-Fri....")
    pass
#Task 2: Issue Categorizer If the user's input contains the word "issue", further categorize the issue based on keywords such as "login", "performance", "error", etc. Print out the category of the issue for the support team.
if any(i in user_words1 for i in user_input.split()):   
    user_input=input(" What is your issue? Type: login, performance, or support ")
if any(i in user_words2 for i in  user_input.split()):
    print(" The user has indicted a problem with LOGIN. The support team was notified ")
elif user_words1:
    if user_input=="performance":
        print(" The user has indicted a problem with the systems PERFORMANCEh. The support team was notified ")
    else:
        print(" The user needs to reach the SUPPORT TEAM. The support team was notified ")
    
   
    
   