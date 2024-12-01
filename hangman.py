import random

#Random Nonsense

print("Hello! Welcome to the word guessing game! A random word is chosen and you will have 5 attempts to guess it! \nAre You Ready?")

#Actual game starts

words=['python', 'game', 'icecream', 'clouds', 'rain', 'pencil', ]
w=random.choice(words)
wl='_'*len(w)
wl1=list(wl)
c=5
guessed=''
print("Current word: ", wl1)
while c>0:
    x=input("Enter a character: ")
    if len(x)!=1:
        print("Please enter a single character.")
        continue
    elif x in guessed:
        print("You already guessed this character. Please guess another one.")
        continue
    elif x in w:
        for i in range(len(w)):
            if x==w[i]:
                wl1[i]=x
        print("Good guess! The letter is indeed in the word")
        print("Current word: ", wl1)
        guessed+=x
    else:
        print("Bad guess, the letter is not in the word..")
        print("Current word: ", wl1)
        c-=1
        print("Number of guesses left: ", c)
        guessed+=x
    if wl1==list(w):
        print("You win! Congratulations! \nThe word was '", w, "'", sep='')
        break
if c==0:
    print("You lose! The word was: '", w, "'", sep='')
