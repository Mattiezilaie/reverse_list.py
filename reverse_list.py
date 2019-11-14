# Author: Mahtab Zilaie
# Date: November 13 2019
# Description: a function that reverses the order of a list

def reverse_list(L):
    i = 0
    z = len(L) - 1
    while(i<z):
        order = L[i]
        L[i]= L[z]
        L[z]= order
        i += 1
        z -= 1

