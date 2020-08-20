import random

def randomnum2():
    temparray = [int(i) for i in range(1, doors + 1)]   #creates a temporary array from 1 to the number of doors
    numbers = random.sample(range(1, doors + 1), doors - 2)   #picks (# of doors-2) numbers between 1 and the numbers of doors
    if (current_pick in numbers) or (winning_num in numbers):  
        while (current_pick in numbers) or (winning_num in numbers):    #this is to ensure that the winning number and the current
            numbers = random.sample(range(1, doors + 1), doors - 2)     #pick aren't in the numbers sampeled
    for g in numbers:            #this loop removes the sampled numbers from our temporary array. 
        temparray.remove(g)      #In the end, the array is always left with two numbers 
    return temparray             #the temporary array is returned. This array contains two numbers. The person's current pick and the winning number.
                                 #If winning number ==  current pick, the remaining number is a random number


win = 0
doors = int(input("How many doors do you want? "))

for i in range(100):
    array = [int(c) for c in range(1, doors + 1)]  #creates an array with doors numbered from 1 to the number specified
    winning_num = random.randrange(1, doors + 1)   #picks a random winning number from the range of doors
    current_pick = random.randrange(1, doors + 1)  #picks a random door that acts as the contestant's pick
    switched_pick = randomnum2()                   
    switched_pick.remove(current_pick)      #removes current pick from the returned array. This is the same as switching your door
    if winning_num in switched_pick:        #if your current pick isn't the winning door, then the remaining door will be the winning door
        win += 1                            #if your current pick is the winning door, then the remaining door will be a losing door

print("Probability of winning is " + str(win) + "%")
