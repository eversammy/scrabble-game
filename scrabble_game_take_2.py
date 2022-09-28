def scrabble2():    # Rejects starting game with "r"
    """
    Scrabble game with hand dealt randomly and user inputs words from hand and receives a score
    """
    import random
    dictionary = open("words.txt", 'r')     # Counting Dictionary Words
    count = 0
    for i1 in dictionary:
        if i1 != "\n":
            count += 1
    print(f'''Loading word list from file...\n    {count} words loaded!''')

    def score(inp):
        score = {'A': 1, 'B': 3, 'C': 3, 'D': 2,     # Function Scoring Dictionary Words
                 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1,
                 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}
        tscore = 0
        for i2 in inp:
            tscore += score.get(i2)
        if len(inp) < 7:
            return tscore * len(inp)
        elif len(inp) == 7:
            return tscore * len(inp) + 50

    words = {'A': 9, 'B': 2, 'C': 2, 'D': 4,     # Dealing Current Hand
             'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8,
             'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1}
    tiles = []
    for i3 in words:
        tiles.append(i3 * words.get(i3))  # Dealing Initial Hand
    scr_tiles = ''.join(tiles)

    while True:
        try:
            total_score = 0
            deal = input('Enter "n" to deal a new hand, "r" to replay the last hand, or "e" to end game: ')
            if deal == 'n':
                hand1 = ' '.join(random.choices(scr_tiles, k=7))  # Dealing Initial Hand
                hand_convert = hand1
                print('Current Hand:', hand1.lower())

                while True:
                    hand1_comb = hand1.replace(' ', '')
                    hand1_list = list(hand1_comb)
                    dictionary = open('words.txt', 'r')  # Search word in dictionary
                    inp = input('Enter word, or a "." to indicate that you are finished: ').upper()

                    current_score = 0
                    dictionary_list = []
                    if inp != '.':
                        for i4 in inp.upper():
                            if i4 not in hand1:  # Search word not in dictionary
                                print('Enter letters in current hand only!')
                                break
                        else:
                            for i5 in dictionary:
                                dictionary_list.append(i5)  # Combine dictionary words to a list
                            if inp.upper() + '\n' in dictionary_list:  # Search word in dictionary
                                total_score += int(score(inp))  # Calling Score Function
                                current_score += int(score(inp))
                                print(f'''"{inp.lower()}" earned {current_score} points. Total: {total_score} points''')
                                for i6 in inp.upper():  # Removing input word from hand
                                    hand1_list.remove(i6)
                                hand1new = ' '.join(hand1_list)

                                if len(hand1new) == 0:  # Check if hand is empty
                                    print(f'''Run out of letters. Total score: {total_score} points.\n''')
                                    break
                                else:  # Dealing new hand by removing inputted word from initial hand
                                    print('Current Hand:', hand1new.lower())
                                    hand1 = hand1new
                            else:
                                print('Invalid word, please try again.')
                    else:
                        print(f'''Total score: {total_score} points.\n''')
                        break

            elif deal == 'r':
                hand2 = hand_convert
                print('Current Hand:', hand2.lower())
                while True:
                    hand2_comb = hand2.replace(' ', '')
                    hand2_list = list(hand2_comb)
                    dictionary = open('words.txt', 'r')  # Search word in dictionary
                    inp = input('Enter word, or a "." to indicate that you are finished: ').upper()
                    current_score = 0
                    dictionary_list = []
                    if inp != '.':
                        for i4 in inp.upper():
                            if i4 not in hand2:  # Search word not in dictionary
                                print('Enter letters in current hand only!')
                                break
                        else:
                            for i5 in dictionary:
                                dictionary_list.append(i5)  # Combine dictionary words to a list
                            if inp.upper() + '\n' in dictionary_list:  # Search word in dic
                                total_score += int(score(inp))  # Calling Score Function
                                current_score += int(score(inp))
                                print(f'''"{inp.lower()}" earned {current_score} points. Total: {total_score} points''')
                                for i6 in inp.upper():  # Removing input word from hand
                                    hand2_list.remove(i6)
                                hand2new = ' '.join(hand2_list)

                                if len(hand2new) == 0:  # Check if hand is empty
                                    print(f'''Run out of letters. Total score: {total_score} points.\n''')
                                    break
                                else:  # Dealing new hand by removing inputted word from initial hand
                                    print('Current Hand:', hand2new.lower())
                                    hand2 = hand2new
                            else:
                                print('Invalid word, please try again.')
                                print('Current Hand', hand2.lower())
                    else:
                        print(f'''Total score: {total_score} points.\n''')
                        break

            elif deal == 'e':
                break

            else:
                print(f'''Enter "n", "r", or "e" to continue...\n''')
        except UnboundLocalError:
            print('Enter "n" to deal a new hand...\n')


scrabble2()
