Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

from random import choice

"""Pennywise Jumpscare Pennywise has a couple catchphrases. When Pi detects motion, initiate text to speech pulling dialogue from hard-coded list. """

#Let's start small. Get pennywise talking. 

for i in range(3):
    pennywise_says = input("Pennywise says: ")
    print(pennywise_says)
    i += 1

def speak(input):
  pass

def detect_motion():
  pass

phrases = ['hello', 'we all float down here', 'hello georgie']


#lets abstract the idea of motion for now. Take an input, say the D key. When it gets that input, it should print sometihng from that list. Something random would be easy, so the import random
# module would be useful 
