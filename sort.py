from data import *
import dfunction


"""
fun result():
this function checks that is the number directly equal to one of the floor numbers or not
then takes number from calculation and gives an answer
"""

def result(k):
    for i in numsunderhun_tur:
        if i == k:
            return numsunderhundred[numsunderhun_tur.index(i)]
    for i in bignum_n:
        if i == k:
            return bignum[bignum_n.index(i)]
    for i in numbers_tur :
        if i == k:
            return str(numbers[numbers_tur.index(i)])+'-'+k[-2:]
    for i in symbols_in_word:
        if i in k:
            return symbolic(i,k)
    if 'yüzde' in k:
            return ispercentage(k)
    return isdecimal(k)


"""
fun ispercentage():

this function checks if the given variable percentage or nor
k1 - the number side which needs to be checked

"""

def ispercentage(k):
    k1 = k.split('yüzde ')[1]
    result = str(isdecimal(k1))
    return result+' %'

"""
fun symbolic():

this function seperates symbols from words then brings them together
k1 - not symbolic side
"""

def symbolic(i,k):
    k1 = k.split(i)[0]
    result = isdecimal(k1)
    return str(result) + symbols[symbols_in_word.index(i)]


"""
fun isdecimal():

this function defines that if the number is decimal or not
if it is decimal number it get result as string and bring them together
else goes on for culcation
"""


def isdecimal(k):
    if 'nokta' in k:
        k1 = k.split(' nokta ')[0]
        k2 = k.split(' nokta ')[1]
        res_k1 = str(check(k1))
        res_k2 = str(check(k2))
        return  res_k1+'.'+res_k2      
    else:
        return check(k)


"""
fun check():
checks the number belongs to which classification
makes string a list
checking number and do calculation
"""

def check(k):
    k1 = k.split(' ')
    for i in numbers_tur:
        if k1[-1] == i:
            k1[-1] = numbers_row[numbers_tur.index(i)]
            return str(sum(k1))+'-{}'.format(k[-2:])
    return sum(k1)


"""
fun sum():
summing result from fun(calculate) and get a string
num - the result of calculation 
"""

def sum(k1):
    num=0

    for i in bignum_n_reverse:
        if i in k1:
            word = k1[:k1.index(i)]
            num = num + dfunction.calculate(word)*bignum_reverse[bignum_n_reverse.index(i)]
            k1 = k1[k1.index(i)+1:] 
            if k1 == [] and word == []:
                return num 
    if k1==[]:    
        return num
    num = num + dfunction.calculate(k1)
    return num