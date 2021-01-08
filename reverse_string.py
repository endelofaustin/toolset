#!/bin/python

# Given any string return a reversed string

# 'austin rules' 'selur nitsua'
# 'austinrulez' 'zelurnitsua'

basket_of_characters = []
string = 'hillo'

def reverse_string(string):
    
   # for character in string:
     runner1 = 0
     runner2 = 0
     while runner2 < len(string):
         
         middle = int(len(string) // 2)
         runner1 = 0
         runner2 = len(string)

         character = string[runner]
         basket_of_characters.insert(0, character)
         runner1 += 1
         runner2 -= 1

         
    
    return ''.join(basket_of_characters)






