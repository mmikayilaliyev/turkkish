from data import *

"""
fun(calculation):
doing calc from words to number by its floor place

fun(main_calc):
actually main_calc do calculation and get answer for the fun(calculation)

variables:
sum- its sum of calculation
str1 - the sring which will be given for calculation
"""

def calculate(str1):
        def main_calc(n=str1):
            if n == 'yüz':
                pass
            elif len(n) == 1:
                    sum = numsunderhundred[numsunderhun_tur.index(n[0])]
            elif (n in numsunderhun_tur) or (n in bignum_n):
                for i in numsunderhun_tur:
                    if n == i:
                        sum = numsunderhundred[numsunderhun_tur.index(i)]
                for i in bignum_n:
                    if n == i:
                        sum =  bignum[bignum_n.index(i)]
            else:
                if (bignum_n[0] == n[1]) and len(n) == 4:
                    sum = (100 * (numsunderhundred[numsunderhun_tur.index(n[0])]) + (numsunderhundred[numsunderhun_tur.index(n[2])]) + numsunderhundred[
                        numsunderhun_tur.index(n[3])])
                elif (bignum_n[0] == n[1]) and len(n) == 3:
                    sum = (100 * (numsunderhundred[numsunderhun_tur.index(n[0])]) + (numsunderhundred[numsunderhun_tur.index(n[2])]))
                elif (bignum_n[0] == n[1]) and len(n) == 2:
                    sum = (100 * (numsunderhundred[numsunderhun_tur.index(n[0])]))
                elif (bignum_n[0] == n[0]) and len(n) == 3:
                    sum = (100 + (numsunderhundred[numsunderhun_tur.index(n[1])]) + (numsunderhundred[numsunderhun_tur.index(n[2])]))
                elif (bignum_n[0] == n[0]) and len(n) == 2:
                    sum = (100 + (numsunderhundred[numsunderhun_tur.index(n[1])]))
                elif (bignum_n[0] not in n) and len(n) == 2:
                    sum = ((numsunderhundred[numsunderhun_tur.index(n[1])]) + (numsunderhundred[numsunderhun_tur.index(n[0])]))
            return sum

        if str1 != []:
            return main_calc(n=str1)
        else:
            return 1
