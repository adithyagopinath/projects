"""
Task:
* Build a Number guessing game, in which the user selects a range
* User selects a range, i.e., from A to B, where A and B belong to Integer
* Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses
"""

import random

def range_input():
    """Choosing two integers for the range
    
    Returns:
        user_range (range): User-inputted range for the computer to select a random number from
    """
    range_num_1 = int(input("Please input integer 1. "))
    range_num_2 = int(input("Please input integer 2. "))
    
    if range_num_1 <= range_num_2:
        user_range = range(range_num_1, range_num_2 + 1)
    else:
        user_range = range(range_num_1, range_num_2 - 1, -1)
        
    return user_range
    
def system_number(user_range):
    """Selecting random number from user-provided range
    
    Args:
        user_range (range): User-inputted range for the computer to select a random number from
    
    Returns:
        random_num (int): Integer selected, within the range, by computer
    """
    random_num = random.choice(user_range)
    return random_num

def game(random_num):
    """Invokes game logic
    
    Args:
        random_num (int): Integer selected, within the range, by computer 
    
    Returns:
        Game complete
    
    """
    count = 0
    mode = input("Would you like to play easy, medium, or hard mode (respond with e, m, or h [<- default])?").lower()
    if mode == "e":
        max_attempts = 15
    elif mode =="m":
        max_attempts = 10
    else:
        max_attempts = 5
    
    while count < max_attempts:
        guess = int(input("\nWhat number do you guess? "))
        count += 1
        
        if guess < random_num:
            print(f"Your guess is less than the correct number. Try again.\n{max_attempts-count} turns remaining.\n")
        elif guess > random_num:
            print(f"Your guess is higher than the correct number. Try again.\n{max_attempts-count} turns remaining.\n")
        else:
            print(f"\nCongratulations! The correct number is {random_num}. It took you {count} tries. You had {max_attempts - count} turns remaining.")
            return
        
        
    print(f"Sorry. The max number of attempts have been fulfilled. The correct number was {random_num}.")
            
            
def final_function():
   """Runs game logic
   """
   print(f"""\nTo play this number guessing game, you will provide 2 numbers to serve as a range for the computer to select a random number from.\nNext, you will be asked to select a difficulty mode, which will determine the number of tries you have to guess the correct number. \nLastly, you will keep choosing until you select the right number or you exceed the max amount of tries.\n""")
   r = range_input() 
   s = system_number(r)
   game(s)
   
final_function()