def bankroll():
    while True: 
        try:
            money = int(input("What is your bankroll? (total amount of money you are wiling to spend)"))
            return money
        except ValueError:
            f"You need to type integer values only. Try again."

def deck():
    card_suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
    card_values = {'1': 1, '2': 2, '3': 3,'4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': [1, 11]}
    return card_suits, card_values

def blackjack(money):
    cont = True 
    suits = deck()[0]
    vals = deck()[1]
    
    
    while cont or money < 0:
        pass
        
        


bankroll()
#blackjack(bankroll())