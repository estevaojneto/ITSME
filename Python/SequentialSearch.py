'''Write a Python program for a sequential search search'''
import math

def sequential_search(haystack, needle):
    for l in range(0, len(haystack)):
        if haystack[l] == needle:
            return l
    return False
    
'''As an example, we'll try to find a 8 on this array: it returns the position 
of the element. '''
print("Position:"+str(sequential_search([1,2,3,5,8], 8)))

'''Now we will try to find an element not contained in the array; returns "False" 
(which we convert to string so we can print it)'''
print("Position:"+str(sequential_search([1,2,3,5,8], 7)))
