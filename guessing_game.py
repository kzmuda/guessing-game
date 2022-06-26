import math
import random
random_nambers = []
for i in range(10): 
    random_nambers.append(random.randint(1, 99))

for i in range(10):
    g = int(input("Enter an integer from 1 to 99: "))
    while random_nambers[i] != g:
        if g < random_nambers[i]:
            print("guess is low")
            g = int(input("Enter an integer from 1 to 99: "))
        elif g > random_nambers[i]:
            print("guess is high")
            g = int(input("Enter an integer from 1 to 99: "))
        else:
            break
    print("you guessed it!")

random_nambersb = []
for i in range(10): 
    random_nambersb.append(random.randint(1, 99))

for i in range(10):
    g = int(input("Enter an integer from 1 to 49: "))
    while random_nambersb[i] != g:
        if g < random_nambersb[i]:
            print("guess is low")
            g = int(input("Enter an integer from 1 to 49: "))
        elif g > random_nambersb[i]:
            print("guess is high")
            g = int(input("Enter an integer from 1 to 49: "))
        else:
            break
    print("you guessed it!")
