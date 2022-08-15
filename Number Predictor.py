import random 

topRange = input("Enter a number: ")

if topRange.isdigit():
    topRange = int(topRange)

    if topRange <= 0:
        print('Please enter a number greater than 0 next time! ')
        quit()

else:
    print('Please enter a number next time.')
    quit()

random_namba = random.randint(0, topRange)
guesses = 0
while True:
    guesses += 1
    user_guess = input("What\'s your guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please enter a number next time! ')
        continue
    
    if user_guess == random_namba:
        print("You got it!")
        break
    elif user_guess > random_namba:
         print('You are above the number!')
    else:
        print("You are below the number!")     
        
print("You got it in", guesses, "guesses")
input("")