import random 

def d4(num_dice):
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1,4)
        roll_results.append(roll)
        total = sum(roll_results)
    return total

def d6(num_dice):
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1,6)
        total = sum(roll_results)
    return total

def d8(num_dice):
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1,8)
        total = sum(roll_results)
    return total

def d10(num_dice):
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1,10)
        total = sum(roll_results)
    return total

def d12(num_dice):
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1,12)
        total = sum(roll_results)
    return total

def d20(num_dice):
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1,20)
        total = sum(roll_results)
    return total

def d100(num_dice):
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1,100)
        total = sum(roll_results)
    return total

