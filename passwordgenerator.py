import sys
import random

# Creating a password generator

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
characters = '!@#$%^&*()_-+]=}{[><?/~`.,|'

# 1 - Automatic generator
def auto_generator():
    lowercase = random.choices(letters, k=4)
    uppercase = random.choices(letters.upper(), k=4)
    num = random.choices(numbers, k=4)
    chars = random.choices(characters, k=4)
    
    password = lowercase + uppercase + num + chars
    random.shuffle(password)
    password = ''.join(password)
    print(f"Your automatic generated password is '{password}'. Thank you for using the automatic password generator.")

# 2 - Easier to memorize password but still stronger

def word_password():
    words = []
    
    print("Hello! You chose this option because you want a secure but easier to remember password.\nThis is known as a passphrase.\n")
    print("Please input 4 words with 4 letters at minimum. You'll be asked to redo a word if not inputted correctly.")
    
    count = 1
    
    while len(words) < 4:
        word = input(f"Input Word {count}: ")
        while len(word) < 4:
            word = input(f"Try again and follow the 4+ letter requirement. Input Word {count}: ")
        if len(word) >= 4:
            words.append(word)
            count += 1
    
    password = ".".join(words)
    print(f"Your generated password is '{password}'\nThank you for using the password generator.")

# 3 - CISA Strong Unique Password Walkthrough (String of mixed-case letters)
def cisa():
    print("""For a strong password, you should include a randomized string of at least: 
  1. 1 uppercase letter
  2. 1 lowercase letter
  3. 1 special character
  4. 1 number""")
    password = input("Please input a password that is a minimum of 16 characters and follows the above requirements.")
    while (len(password) < 16 
           or not any(char.isupper() for char in password)
           or not any(char.islower() for char in password)
           or not any(char.isdigit() for char in password)
           or not any(not char.isalnum() for char in password)):
        password = input("Please try again and follow the requirements.") 
    print(f"\nYour strong password is '{password}'.\nGreat job following CISA recommendations.")
# Main

def main_program():
    print(f"""Welcome to the password generator.\nYou'll have three options to choose from.
    \n  1. Automatic Generator (Generates strong password for you)
    \n  2. Four Word Password Walkthrough 
    \n  3. CISA Password Walkthrough\n""")
    
    decision = input(f"Please choose option 1, 2, or 3. If you would like to exit, press any other character.")
    if decision in ['1', '2', '3']:
        if decision == '1':
            auto_generator()
        elif decision == '2':
            word_password()
        else:
            cisa()
            
    else:
        sys.exit(0)

main_program()