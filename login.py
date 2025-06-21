users = {"Mike": "password123", "Tim":"green53", "Melissa":"Tiger1!24jd"}

def authenticate():
    user_finished = False
    while user_finished == False:
        user = input("Would you like to authenticate yourself or add a new user? (1 or 2?): ")
        if user not in ['1','2']:
            print("Please try again. Enter 1 or 2.")
            continue
        
        if user == '1':
            username = input("What is your username?: ")
            if username in users:
                user_pass = input("Please enter the password.: ")
                if user_pass == users[username]:
                    print("You have been authenticated. The password matches with the associated username.")
                else:
                    print("Try again. The username and password do not match. ")   
            else:
                print("The username does not exist. Please try again. ")
       
        else:
            while True:
                new_user = input("What is the new username you would like to add?: ")
                if new_user in users:
                    print("Username already exists. Please try a different username.\n")
                    continue
                    
                new_password_first_attempt = input("What is the password for the associated username?: ")
                new_password_retry = input("Type in the password to confirm: ")
                
                if new_password_first_attempt == new_password_retry:
                    users[new_user] = new_password_first_attempt
                    print(f"{new_user} added successfully.")
                    break
                else:
                    print("Passwords did not match. Please try again.")
        
        exit_auth = input("Would you like to continue (y/n)? ").lower()
        if exit_auth == 'n':
            user_finished = True
            print("Exiting authentication mode.")

def reset_password():
    pass

def log_off():
    pass

def prompt():
   logged_off = False
   while logged_off == False:
       if cont_prompt not in [str(1),str(2),str(3)]:
            print("Please try again. Respond with 1, 2, or 3.\n")   
            cont_prompt = input("Would you like to (answer with 1, 2, or 3):\n  1. Authenticate\n  2. Reset Password\n  3. Log Off\n")
       elif cont_prompt == 1:
            authenticate()
       elif cont_prompt == 2:
            reset_password()
       else:
           print(f"You have been logged off!")                    

