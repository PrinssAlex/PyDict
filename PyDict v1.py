
# 25th Jan 2022:
#===============

#Author: P. A. Ogbodum
#=====================

#Program Description:
#====================

#Program Name: PyDict v1
#=======================

 # A dictionary program that takes a user input word and returns its definition.
 # If the user entered a wrongly spelt word, it returns a word closest to the user entered word and its definition if the user desire.
 # If the word does not exist, it returns an error message which asks the user to double check the word entered. 
 

from difflib import get_close_matches # a library that can be used to compare string values

jsonFile = open("json/File/Path")
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
    elif len(get_close_matches(word, data.keys(), n=1, cutoff=0.85)) > 0:
	#return suggested word closely matching the user defined word
        word_guessed = get_close_matches(word, data.keys(), n=1, cutoff=0.85)
        word_guessed = ','.join(word_guessed)
        print( f'Did you mean {word_guessed} ? \n')
        re_exec = input('If Yes type Y, if No type N \n\n')
        re_exec = re_exec.upper()
        re_word = data[word_guessed]
	#check if the suggested word is correct or not 
        if re_exec == 'Y':
            print(' ')
            print(','.join(re_word))
        elif re_exec == 'N':
            print('Word doesn\'t exist. Kindly double check and try again. ')
        else:
            print('\nQuery not recognized')
#if the word entered is wrong, prompt the user to double check the word 
    else:
        print('!Error: The word you entered does not exist. Kindly check and re-enter the word you entered')