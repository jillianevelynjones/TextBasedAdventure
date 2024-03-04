import random


def rolldice(sides, num_rolls):

    rolls = [random.randint(1, sides) for _ in range(num_rolls)]
    total = sum(rolls)
    print(f"Rolling {num_rolls}d{sides}: {rolls} -> Total: {total}")
    return total

