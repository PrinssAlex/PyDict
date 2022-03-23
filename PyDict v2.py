
 # 28th Jan 2022:
#===============

#Author: P. A. Ogbodum
#=====================

#Program Description:
#====================

#Program Name: PyDict v2 (modified)
#==================================

 # A dictionary program that takes a user input word and returns its definition.
 # If the user entered a wrongly spelt word, it returns a word closest to the user entered word and its definition if the user desire.
 # If the word does not exist, it returns an error message which asks the user to double check the word entered. 
 # Update: Added the function that returns multiple words closest in spelling to that which the users enters. In a case where the user enters a 
 # misspelt word or word that does not exist in the dictionary.
 

from difflib import get_close_matches # a library that can be used to compare string values

jsonFile = open("C:/Users/PRINCE PC/Desktop/App Dev/PyApp/data.json")
data = json.load(jsonFile)

def wordLookup():
    user_word = input('Enter word: \n')
    word = str(user_word).lower()
    print(' ')
#check if the word the user entered is correctly spelt
    if word in data:
        word_found = data[word]
        print(','.join(word_found))
#if the word the user entered is mistakenly spelt, give suggetions
    elif len(get_close_matches(word, data.keys(), n=5, cutoff=0.5)) > 0:
	#return suggested word closely matching the user defined word
        word_guessed = get_close_matches(word, data.keys(), n=3, cutoff=0.5)
        if len(word_guessed) > 1:
            word_guessed = ','.join(word_guessed)
            type_check = input (f'Did you mean any of the following words? {word_guessed}\nIf yes, type\
 Y to re-enter the correct word. If Not, type N \n')
            re_exec = str(type_check).upper()
            if re_exec == 'Y':
                user_word = input('Enter word: \n')
                word = str(user_word).lower()
                print(' ')
                if word in data:
                    word_found = data[word]
                    print(' ')
                    print(','.join(word_found))
                elif word not in data:
                    print('Word does not exist')
            elif re_exec == 'N':
                print(' ')
                print('Sorry, word does not exist. Kindly cross check the word and try again')
            else:
                print(' ')
                print('Error! Query not recognized')
#if the word entered is wrong, prompt the user to double check the word 
    else:
        print(' ')
        print('!Error: The word you entered does not exist. Kindly check and re-enter the word you entered')