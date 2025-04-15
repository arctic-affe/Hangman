from random import *
word_list = ["Kerze"]
non_letter_symbols = """`~!@#$%^&*()-_0123456789 =+[{]}\|;:'",<.>/?"""

def get_word(): 
    return word_list[randint(0,len(word_list))-1]

def display_hangman(tries):
    stages = ['''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                  '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                  '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                ''']

    print(stages[tries])

def enter_guess(tries, word):
    print(f"Trag das ganze Word oder die Buchstabe rein. Du hast noch {tries} Versuche")
    print()
    text = input().strip()
    flag = False

    while flag == False:
        if len(text) == 1 or len(text) == len(word):
            flag = True
            break 
        else:    
            print()
            print(f"Ungültiger Eintrag! Trag das ganze Word oder die Buchstabe rein. Du hast noch {tries} Versuche")
            print()
            text = input().strip()

        for i in range(len(text)):
            if text[i] not in non_letter_symbols:
                flag = True
            else:
                flag = False
                print()
                print(f"Ungültiger Eintrag! Trag das ganze Word oder die Buchstabe rein. Du hast noch {tries} Versuche")
                print()
                text = input().strip()
                break
    return text

def play(): 
    word = get_word()
    word_completion = '_' * len(word)  
    guessed = False                    
    guessed_letters = []               
    guessed_words = []                 
    tries = 6   

    print("Lasst uns spielen!")
    while tries != 0: 
        display_hangman(tries)
        word_completion = word_completion[0].upper() + word_completion[1:].lower()
        print()
        print(f"Word completion - {word_completion}")
        print()
        user_answer = enter_guess(tries, word)
        flag = False

        if user_answer.title() == word:
            print()
            print(f"Jawohl! Du hast Recht! Das Wort heißt {word}")
            break

        if len(user_answer) == 1:
            for i in range(len(word)):
                if word[i].lower() == user_answer.lower():
                    flag =True
                    word_completion = word_completion[:i] + user_answer + word_completion[i+1:]
            
        if flag == False:
            tries -= 1
            print()
            print("-" * 10)
            print("Falsche Antwort!")
            print("-" * 10)
        else:
            print()
            print("-" * 10)
            print("Jawohl! Jetz geht´s weiter!")
            print("-" * 10)

    if tries == 0 and word_completion != word:
        print()
        print(f"Es tut mir leid! Du hast verloren! Das Wort ist '{word}'")
        display_hangman(tries)

user_answer = "ja" 


while user_answer == "ja":
    play() 
    print("\nWillst noch ein Spiel haben? Beantworte mit 'ja' oder 'nein'.\n")
    user_answer = input().strip().lower()

    while user_answer not in ["ja", "nein"]:
        print("\nUngültiger Eintrag! Beantworte mit 'ja' oder 'nein'.\n")
        user_answer = input().strip().lower()

    if user_answer == "nein":
        print("\nSchön, dass du da warst! Bis bald!")
        break
    


        









