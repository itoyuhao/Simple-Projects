"""
File: hangman.py
Name: Kevin Chen
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Algorithm decomposition:
    Step 1: Set the answer randomly and encrypt it to a dashed form.
    Step 2: Let users start guessing until they win or use up their lives
    """
    # Step 1: Set and encrypt the answer to a dashed one
    answer = random_word()
    dashed = encrpyt(answer)
    # Users chances to make a wrong guess
    lives = N_TURNS

    # Step 2: Start guessing!
    while True:
        # Show the progress and the lives remained, then let users make a guess.
        print('The word looks like: ' + dashed)
        input_ch = input('You have ' + str(lives) + ' guesses left.\nYour guess: ')

        # Check the validity of the guess and make it be uppercase. Let users guess again if not valid.
        while len(input_ch) != 1 or input_ch.isalpha() is False:
            input_ch = input('Illegal format.\nYour guess: ')
        input_ch = input_ch.upper()

        # Situation of wrong Guess: lose a life, show the progress
        if answer.find(input_ch) == -1:
            lives -= 1
            print('There is no ' + str(input_ch) + '\'s in the word.')
            # Break if no lives remained
            if lives == 0:
                print('You are completely hung : (\nThe word was: ' + answer)
                break
        # Situation of guess right: update and show the progress
        else:
            dashed = update(input_ch, answer, dashed)
            # Break if the progress(dashed) is totally the same as answer
            if dashed == answer:
                print('You win!!\nThe word was: ' + answer)
                break
            print('You are correct!')


def update(input_ch, answer, dashed):
    """
    This function update the progress when users make a right guess (string manipulation)
    :param input_ch: str, an alphabet users enter in this round
    :param answer: str, the final answer
    :param dashed: str, the dashed answer
    :return decrypted: str, the updated progress
    """
    # Create an empty string
    decrypted = ''
    for i in range(len(answer)):
        # Find the position of character users guess right and update it
        if answer[i] == input_ch:
            decrypted += input_ch
        else:
            # Remain the part users already solved, and fill the unsolved part with dash sign
            if dashed[i] != '-':
                decrypted += dashed[i]
            else:
                decrypted += '-'
    return decrypted


def encrpyt(answer):
    """
    This program encrpyt the answer to dash
    :param answer: str, the final answer
    :return encrpyted: str, the dashed answer
    """
    encrpyted = ''
    for ch in answer:
        encrpyted += '-'
    return encrpyted


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
