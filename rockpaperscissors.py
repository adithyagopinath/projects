import random

def mode():
    while True:
        try:
            m = int(input("Would you like to play til a fixed score [option 1] or keep going until you want to stop [option 2]? Respond with 1 or 2."))
            if m in [1,2]:
                break
            else: 
                print("Try again. Please enter 1 or 2.\n")
        except ValueError:
            print("Try again. Enter a number: 1 or 2.\n")
    if m == 1:
        fixed_score = abs(int(input("What score would you like to play til? Enter a number. ")))
        sc = fixed_score
        return sc
    else:
        sc = -1
        return sc
    
def game(sc):
    user = 0
    pc = 0
    turns = 0
    
    if sc > 0:
        while user < sc and pc < sc:
          while True:
            u_rps = input("\nRock, paper, scissors, go! (Select r, p, or s.)").lower()
            if u_rps in ['r', 'p', 's']:
                break
            else:
                print("\nYou didn't select rock (r), paper (p), or scissors (s). Try again.")
          pc_rps = random.choice(['r', 'p', 's'])
          turns += 1
          if u_rps == 'r' and pc_rps == 's' or u_rps == 's' and pc_rps == 'p' or u_rps == 'p' and pc_rps == 'r':
              print(f"\nCongrats. You chose {u_rps} while your opponent elected to go with {pc_rps}. You win this round!")  
              user += 1
          elif pc_rps == 'r' and u_rps == 's' or pc_rps == 's' and u_rps == 'p' or pc_rps == 'p' and u_rps == 'r':
              print(f"\nYikes. Your opponent took this round by selecting {pc_rps} over your decision to go {u_rps}. Better luck next round.")
              pc += 1
          else:
              print(f"\nYou and your opponent were thinking alike with both of you choosing {pc_rps}")
          print(f"\nThe score is {user} to {pc}. The target score is {sc}. {turns} rounds have been completed.")
        if user == sc:
            print(f"\nCongratulations. You win {user} to {pc}!")
        else:
            print(f"\nSorry. You lost {user} to {pc}. Better luck next time.")
   
    else:
        cont = True
        while cont:
            while True:
                u_rps = input("\nRock, paper, scissors, go! (Select r, p, or s.)").lower()
                if u_rps in ['r', 'p', 's']:
                    break
                else:
                    print("\nYou didn't select rock (r), paper (p), or scissors (s). Try again.")
            pc_rps = random.choice(['r', 'p', 's'])
            
            if u_rps == 'r' and pc_rps == 's' or u_rps == 's' and pc_rps == 'p' or u_rps == 'p' and pc_rps == 'r':
                print(f"\nCongrats. You chose {u_rps} while your opponent elected to go with {pc_rps}. You win this round!")  
                user += 1
            elif pc_rps == 'r' and u_rps == 's' or pc_rps == 's' and u_rps == 'p' or pc_rps == 'p' and u_rps == 'r':
                print(f"\nYikes. Your opponent took this round by selecting {pc_rps} over your decision to go {u_rps}. Better luck next round.")
                pc += 1
            else:
                print(f"\nYou and your opponent were thinking alike with both of you choosing {pc_rps}")
            
            while True:
                keep_going = input("\nWould you like to keep going? (y/n)").lower()
                if keep_going == 'y':
                    cont = True
                    break
                elif keep_going == 'n':
                    cont = False
                    break
                else:
                    print("\nPlease answer again properly (y/n).")
                    
        print(f"\nThe final score is {user} to {pc}.")
        
def play_game():
   targ = mode()
   game(targ) 
   
play_game()