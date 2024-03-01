import random

class Roll():

    def d4(num_dice):
        roll_results = []
        for _ in range(num_dice):
            roll = random.randint(1,4)
            roll_results.append(roll)
            total += roll 
        return roll_results, total
    
    def d6(num_dice):
        roll_results = []
        total = 0
        for _ in range(num_dice):
            roll = random.randint(1,6)
            roll_results.append(roll)
            total += roll
        return roll_results, total
    
    def d8(num_dice):
        roll_results = []
        total = 0
        for _ in range(num_dice):
            roll = random.randint(1,8)
            roll_results.append(roll)
            total += roll
        return roll_results, total
    
    def d10(num_dice):
        roll_results = []
        total = 0
        for _ in range(num_dice):
            roll = random.randint(1,10)
            roll_results.append(roll)
            total += roll
        return roll_results, total
    
    def d12(num_dice):
        roll_results = []
        total = 0
        for _ in range(num_dice):
            roll = random.randint(1,12)
            roll_results.append(roll)
            total += roll
        return roll_results, total
    
    def d20(num_dice):
        roll_results = []
        total = 0
        for _ in range(num_dice):
            roll = random.randint(1,20)
            roll_results.append(roll)
            total += roll
        return roll_results, total
    
    def d100(num_dice):
        roll_results = []
        total = 0
        for _ in range(num_dice):
            roll = random.randint(1,100)
            roll_results.append(roll)
            total += roll
        return roll_results, total
