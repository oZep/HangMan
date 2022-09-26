
#hang man let goo
#september 25, 2022

def art(n):
    if n == 0:
        print(' +---+')
        print(' |   |')
        print(' 0   |')
        print('/|\  |')
        print('/ \  |')
        print('     |')
        print('=========')

    elif n == 1:
        print(' +---+')
        print(' |   |')
        print(' 0   |')
        print('/|\  |')
        print('/    |')
        print('     |')
        print('=========')

    elif n == 2:
        print(' +---+')
        print(' |   |')
        print(' 0   |')
        print('/|\  |')
        print('     |')
        print('     |')
        print('=========')
    elif n == 3:
        print(' +---+')
        print(' |   |')
        print(' 0   |')
        print('/|   |')
        print('     |')
        print('     |')
        print('=========')

    elif n == 4:
        print('+---+')
        print('|   |')
        print('0   |')
        print('|   |')
        print('    |')
        print('    |')
        print('=========')
    elif n == 5:
        print('+---+')
        print('|   |')
        print('0   |')
        print('    |')
        print('    |')
        print('    |')
        print('=========')
    else:
        print('+---+')
        print('|   |')
        print('    |')
        print('    |')
        print('    |')
        print('    |')
        print('=========')
        return


def pickWord():
    word = input("What is the word you want the player to guess? ")
    print("Well... that will surely trick someone.")
    print("Pass the computer onto the other participants")
    return word

def guessWord(wordHanged):
        print("It's time to guess the word!")
        wordGuessed = str(input("What is the word? "))
        if wordGuessed == wordHanged:
            print("Congrats you've won!")
            exit()
        else:
            print("Sorry but that's not correct, your man has been... HANGED")
            exit()

def askLetter(wordHanged):
    n = 6 #number of turns the person has to guess the word
    guess = str(input("Hello new player to get started press x: "))
    if guess == 'x' or guess == 'X':
        while n >= 0: #the player has 6 lives
            letter = str(input("what letter do you want to guess? "))
            if letter in wordHanged:
                print("Congrats " + letter + " is in the word")
                guess = str(input("Do you want to guess now? If so, type x: "))
                if guess == 'x' or guess == 'X':
                    guessWord(wordHanged)
                else:
                    continue
            else:
                print("oh No, " + letter + " is not in the word")
                n -= 1
                art(n)
                if n == 0:
                    print("Sorry but you've ran out of tries, your man has been... HANGED")
                else:
                    print("You now have", n, "lives left")
                    continue
                    
            
    else:
        print("It's time to guess the word!")
        wordGuessed = str(input("What is the word? "))
        if wordGuessed == wordHanged:
            print("Congrats you've won!")
            exit()
        else:
            print("Sorry but that's not correct, your man has been... HANGED")
            exit()


def startgame():
    print("Hello, welcome to the game hangman")
    startGame = str(input("Press x to start: "))
    if startGame == 'x' or startGame == 'X':
        wordHanged = pickWord() #we have the word
        askLetter(wordHanged)
    else:
        print("Well... there is always next time.")


startgame()
