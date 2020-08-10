import random

def randomnum2():
    temparray = [int(i) for i in range(1, doors+1)]
    numbers = random.sample(range(1, doors+1), doors-2)
    if (current_pick in numbers) or (winning_num in numbers):
        while (current_pick in numbers) or (winning_num in numbers):
            numbers = random.sample(range(1, doors + 1), doors - 2)
    for g in numbers:
        temparray.remove(g)
    return temparray

win = 0
doors = int(input("How many doors do you want? "))

for i in range(100):
    array = [int(c) for c in range(1, doors+1)]
    winning_num = random.randrange(1, doors+1)
    current_pick = random.randrange(1, doors+1)
    switched_pick = randomnum2()
    switched_pick.remove(current_pick)
    if winning_num in switched_pick:
        win += 1
        
print("Probability of winning is " + str(win) + "%")
