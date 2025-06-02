
# importing modules 
import random as r  #aliasing module name as r 
import string as s

#using function to generate password
def generate_password():
    
    #using methods choice from random module and ascii_uppercase from string module
    upper = r.choice(s.ascii_uppercase)
    number = r.choice(s.digits)
    
    #adding special character in a variable named special
    special = r.choice('!@#$%^&*()_+-=[]{}|;:,.<>?')
    
    # Remaining characters from all allowed sets
    remaining_length = 8 - 3

    #generating remaining characters of the password with combination of alphabets, digit 
    # and special characters 
    all_chars = s.ascii_letters + s.digits + '!@#$%^&*()_+-=[]{}|;:,.<>?' 

    #random.choices() method in Python returns a list of randomly selected elements 
    # with replacement from a given sequence. 
    # With replacement means the same element can be picked more than once.

    remaining = r.choices(all_chars, k=remaining_length)

    # Combine all and shuffle
    password = [upper, number, special] + remaining
    r.shuffle(password)
    
    return ''.join(password)

# printing the password
print("Generated password:", generate_password())
