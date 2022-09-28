from scrabble_with_myself import *


def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.
    """
    max_score = 0
    best_word = None
    for e in wordList:
        if isValidWord(e, hand, wordList):
            if getWordScore(e, n) > max_score:
                max_score = getWordScore(e, n)
                best_word = e
    return best_word


def compPlayHand(hand, wordList, n):

    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer chooses it.
    """
    total_score = 0
    print('Current Hand:', end=' ')
    displayHand(hand)
    while compChooseWord(hand, wordList.copy(), HAND_SIZE):
        g_input = compChooseWord(hand, wordList.copy(), HAND_SIZE)
        scores = getWordScore(g_input, HAND_SIZE)
        total_score += scores
        print('"{}" earned {} points. Total: {} points'.format(g_input, scores, total_score))
        hand = updateHand(hand, g_input)
        compChooseWord(hand, wordList.copy(), HAND_SIZE)
        print('Current Hand:', end=' ')
        displayHand(hand)
    else:
        print('Run out of words. Total score: {} points.'.format(total_score))
    

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
    """
    hand_convert = None
    while True:
        fff = '\nEnter "n" to deal a new hand, "r" to replay the last hand, or "e" to end game: '
        game_input = input(fff).lower()
        lll = 'Enter a "u" or a "c": '
        if game_input == 'n':
            qqq = dealHand(HAND_SIZE)
            hand_convert = qqq
            while True:
                game_input2 = input(lll).lower()
                if game_input2 == 'u':
                    playHand(qqq, wordList, HAND_SIZE)
                    break
                elif game_input2 == 'c':
                    compPlayHand(qqq, wordList, HAND_SIZE)
                    break
                else:
                    print('Invalid command.')

        elif game_input == 'r':
            if hand_convert is None:
                print('You have not played a hand yet. Please play a new hand first!')
            else:
                vvv = hand_convert
                while True:
                    game_input2 = input(lll).lower()
                    if game_input2 == 'u':
                        playHand(vvv, wordList, HAND_SIZE)
                        break
                    elif game_input2 == 'c':
                        compPlayHand(vvv, wordList, HAND_SIZE)
                        break
                    else:
                        print('Invalid command.')

        elif game_input == 'e':
            break
        else:
            print('Invalid command.')


""" 
Play game
"""
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
