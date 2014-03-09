#Monty Hall problem#

import random

door1 = 'Goat'
door2 = 'Goat'
door3 = 'Car'

doorList = [door1, door2, door3]
winList = []
simulationTrys = 1000000


## In this simulation, the 'contestant' always chooses the
## first door.  Since the doors are randomized anyways, it
## doesn't really matter, but it simplifies the problem.
## Next, the program checks if the second door is a goat.
## If so, in a gameshow, the host would reveal that door before
## offering the switch.  Otherwise, he would reveal the third
## door.

for choices in range(simulationTrys):
    random.shuffle(doorList)
    if doorList[1] == 'Goat':
        finalChoice = doorList[2]
    else:
        finalChoice = doorList[1]
    if finalChoice == 'Car':
        winList.append('win')
        

wins = len(winList)
winPercentage = (float(wins) / float(simulationTrys)) * 100


print 'In a simulation of a million monty halls, the win percentagage is ' + str(winPercentage) + '%.'
print 'Remember, always switch your choice!'
    
            
        


