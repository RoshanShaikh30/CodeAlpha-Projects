#Roshan Shaikh : Task 01

'''randomly choose a word
give _ _ on the basis of the length of the word chosen by comp
'''
import random

words = ['rose','apple','charge','network','burger']

#secret word selection frm list
target = random.choice(words)
# n - length of the word stored in target
#print(target) #leaving this line to test if target works - instead of typing again n again
n = len(target)
print("Guess the word:")
display = ["_"] * n
for i in range(n):
    print("_ ",end="")

#giving the user 5 chances to guess!
wrong_guess = 0
max_guess = 5

while wrong_guess < max_guess:
    guess = input("\n Enter an alphabet:")
    guess = guess.lower() #so it works even if user inputs cap letter.
    if guess in target:
        #rvling the letter at it's respective position.
        for i in range(len(target)):
         if target[i] == guess:
          display[i] = guess
    else:
        wrong_guess += 1
        print("Wrong guess! Remaining guesses:", max_guess - wrong_guess)
        
    for letter in display:
        print(letter,end="")
    if "_" not in display:
        print("\n You guessed the word!")
        break
    
if wrong_guess == max_guess:
            print("You ran out of guesses!! :( \n The word was:",target)