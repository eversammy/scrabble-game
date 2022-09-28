import random

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList


def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence and the values are integer counts,
    for the number of times that an element is repeated in the sequence.
    """
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.
    """
    tscore = 0
    for i in word:
        tscore += SCRABBLE_LETTER_VALUES.get(i)
    if len(word) < n:
        return int(tscore * len(word))
    elif len(word) == n:
        return int(tscore * len(word) + 50)


def displayHand(hand):
    """
    Displays the letters currently in the hand.
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=" ")       # print all on the same line
    print('')



def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.
    """
    hand = {}
    numVowels = int(n / 3)
    for i in range(numVowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(numVowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand


def updateHand(hand, word):
    """
    updqate current hand
    """
    hand2 = hand.copy()
    for i in word:
        if i in hand2:
            hand2[i] = hand2.get(i, 0) - 1
            if hand2.get(i) == 0:
                hand2.pop(i)
    return hand2


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.
    """
    hand_ = ''
    for ii in hand:
        hand_ += hand.get(ii) * ii
    kk, gg = list(''.join(list(word))), list(hand_)
    for i in ''.join(list(word)):
        if i in gg:
            kk.remove(i), gg.remove(i)
    if len(kk) == 0 and ''.join(list(word)) in wordList:
        return True
    else:
        return False


def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    """
    num = 0
    for i in hand:
        num += hand[i]
    return num


def playHand(hand, wordList, n):
    """
    play hand
    """
    total_score = 0

    while calculateHandlen(hand) > 0:
        print('Current Hand:', end=' ')
        displayHand(hand)
        ggg = 'Enter word, or a "." to indicate that you are finished: '
        g_input = input(ggg).lower()
        if g_input == '.':
            print('Total score: {} points.'.format(total_score))
            break
        else:
            if isValidWord(g_input, hand, wordList) is False:
                print('Invalid word, please try again.\n')
            else:
                scores = getWordScore(g_input, n)
                total_score += scores
                print('"{}" earned {} points. Total: {} points'.format(g_input, scores, total_score))
                hand = updateHand(hand, g_input)
    else:
        print('Run out of letters. Total score: {} points.'.format(total_score))


def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
    """
    hand_convert = None
    while True:
        fff = '\nEnter n to deal a new hand, r to replay the last hand, or e to end game: '
        game_input = input(fff).lower()
        if game_input == 'n':
            qqq = dealHand(HAND_SIZE)
            hand_convert = qqq
            playHand(qqq, wordList, HAND_SIZE)

        elif game_input == 'r':
            if hand_convert is None:
                print('You have not played a hand yet. Please play a new hand first!')
            else:
                vvv = hand_convert
                playHand(vvv, wordList, HAND_SIZE)

        elif game_input == 'e':
            break
        else:
            print('Invalid command.')


"""
Play Game
"""
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
