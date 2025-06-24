#file imports 
from rxns import *
import time

#reactions 
x = 0

#Menu for what you would like to do
#prime, run, calibrate etc

should_prime = input("Would you like to prime? (Y/N) ")

if should_prime.upper() == 'Y':
    prime_all()

#list the automated synthesis here
automated_synthesis()


