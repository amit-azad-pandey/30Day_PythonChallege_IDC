import re
 
email=input("Enter the mail address:")

if re.match(r".+@gmail\.com$",email):
    print("Gmail id is valid")
else:
    print("Gmail id is not valid")