# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 19:46:51 2024

@author: HP EliteBook 840 G4
"""

import random


#Numpy didnt work as lists had different lenghts. numpy works on only same range lists.  
#importing Random so that we can use functions of random, otherwise python will not recognize it and throw errors.

#creating 3D arrays of different characters. Here we have 4 layers consisting upper/lower/special characters and numbers.

array_3d = ([
    list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
    list("abcdefghijklmnopqrstuvwxyz"),
    list("0123456789"),
    list("!@#$%^&*()_+-=[]{}|;':\",./<>?")
])

#to know length of each list using len fuction we will lopp through each layer.

for i in range(len(array_3d)):
  print(f"Layer {i+1}: {len(array_3d[i])}")

def generate_password(length): #function to generate password
  password = []
  password_length = 10

  generated_password = password_length
  
  for i in range(length):
    layer = random.randint(0,3) #randomply picks layer from above 4 layers
#Here 3 is inclusive unlike range function

    if layer == 0:
      char = array_3d[layer][random.randint(0,25)] #pick any random charachter from first layer (0)
    
    elif layer == 1:
      char = array_3d[layer][random.randint(0,25)]

    elif layer == 2:
      char = array_3d[layer][random.randint(0,9)]

    elif layer == 3:
      char = array_3d[layer][random.randint(0,28)]

    password.append(char)

  return "".join(password)

password = generate_password(10)
print("Generated password:", password)
