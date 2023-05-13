"""A number-guessing game."""

# Put your code here
#greet player

name = "Anna";


print(name, "I'm thinking of a number between 1 and 100. Try to guess my number.")
number = int(input("Your guess: ")) 
correct_guess = 90
guess_count = 0
Isguess = False
while (Isguess == False):
    guess_count += 1
    if number == correct_guess:
        print(f'Well done {name}! You found my number in {guess_count} tries.')
        Isguess = True
        guess_count = 0
        
        break
    elif number > correct_guess:
        print("Your guess is too high. Try again.")
        number = int(input('Your guess: '))
    elif number < correct_guess:
        print("Your guess is too low. Try again.")
        number = int(input('Your guess: '))

    
    
    
