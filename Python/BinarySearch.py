'''Write a Python program for binary search'''
import math

def binary_search(haystack, needle):
    l = 0
    r = len(haystack)-1
    while(l <= r):
        m = math.floor((l+r)/2)
        if haystack[m] < needle:
            l =  m+1
        elif haystack[m] > needle:
            r = m-1
        else:
            return m
    return False;
    
'''As an example, we'll try to find a 3 on this array: it returns the position 
of the element. '''
print("Position:"+str(binary_search([1,2,3,5,8], 3)))

'''Now we will try to find an element not contained in the array; returns "False" 
(which we convert to string so we can print it)'''
print("Position:"+str(binary_search([1,2,3,5,8], 7)))
