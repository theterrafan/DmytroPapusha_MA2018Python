import random
game_mode=int(input('Type 100 or 1000 to choose game mode! '))
if game_mode == 100:
              guesses = 6
              number = random.randint(1,100)
              win = False

   
else:
   guesses = 14
   number = random.randint(1,1000)
   win = False


while guesses > 0:
    guess = int(input('Guess: '))
    
    guesses -=1
    
    if guess > number:
        print('Your guess is too high! You have', guesses, 'remaining')
    elif guess < number:
        print('Your guess is too low! You have', guesses, 'remaining')
    else:
        print('Congratulations! You guessed the correct number!')
        win = True
        guesses = 0
        
        
if win == False:
    print("Sorry, you lost :( The number was", number)
