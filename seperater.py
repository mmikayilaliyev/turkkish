from cgi import print_arguments
import sort
from data import *

"""
func allornot():
checks if all words are numbers or not 
if it is True it starts calculate
else starts find words
"""

def allornot(sentence):
        sentence_splitted =sentence.split(' ')    
        booleanlizt = []
        for i in sentence_splitted:
            if (i in all_turk)  == True:
                booleanlizt.append(True)
            else:
                booleanlizt.append(False)
       
        for i in booleanlizt:
            if i == False:
                return getnumbers(sentence)    
        return sort.result(sentence)


""""
func getnumbers()
in this function we add words step by step
if word is number  it adds it to numlist and calculating
"""

"""
func decision()
its recursive function 
it checks step by step for and decide which way to go

p.s. i added ' .' at starting to string and at the end i deleted it to avoid errors
"""
def getnumbers(sentence):
    sentence = sentence +' .'
    text = []
    numlist = []
    sentence_splitted =sentence.split(' ')
    
 


    def decision(ind):
        nextword = sentence_splitted[ind+1]

        if (nextword in all_turk) and (word in all_turk):
            numlist.append(word)


        elif ( (nextword not in all_turk) and (word in all_turk) ) or (nextword =='' and (word in all_turk)):
            numlist.append(word)
            word1 =  ' '.join(numlist)
            res=str(sort.result(word1))
            numlist.clear()
            text.append(res)


    for i in sentence_splitted:
        if i in all_turk:
            word = i
            ind = sentence_splitted.index(i)
            decision(ind)
        else:
            text.append(i)

    end = " ".join(text)
    
    return end[ :-1]