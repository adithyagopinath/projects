import random

def words():
    words = ["Apple","Brave","Charm","Drift","Eagle","Frost","Giant","Happy","Ivory","Jelly","Knife","Lemon","Mango","Novel","Ocean","Puppy","Queen","Rapid","Storm","Tiger","Urban","Vivid","Witty","Xenon","Zesty"]
    return words.lower()

def wordle(words):
    characters = list(words)
    w = {}
    for i in range(len(characters)):
        if characters[i] not in w:
            w[characters[i]] = [i + 1]
        else:
            w[characters[i]].append(i+1)
    attempts = 0
    print("Welcome to Wordle.\n")
    g = input("Type your 5-letter guess:\n")
    while attempts <= 6 or list(g) == w:
        attempts += 1
        
    
def game():
   word = words()
   wordle(word)

game()