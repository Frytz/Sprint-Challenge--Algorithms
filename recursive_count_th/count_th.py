'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
#length of "th" == 2
#is the word less tha 2?
#if the first 2 are not "th" remove the fist letter and conintue along the string 

def count_th(word):
    #if the length is less then 2 "th" cannot exist
    #base
    if (len(word) < 2):
        return 0
    #if the first 2 letters are "th"
    if (word[:2] == "th"):
        return count_th(word[1:]) + 1
    #continues the search if the first 2 functions are false
    else:
        return count_th(word[1:])
    
    # TBC
    
    # pass
