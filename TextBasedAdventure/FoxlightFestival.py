class Player(object): #But seriously what's the point of this?
    def __init__(self, name):
        self.name = name

    def movement(self):
        while True:
            print_map()
            print("1.North, 2.South, 3.East, 4.West")
            move = input("> ").lower()
            if move == '1':
                x, y = (-1, 0)
            elif move == '2':
                x, y = (1, 0)
            elif move == '3':
                x, y = (0, 1)
            elif move == '4':
                x, y = (0, -1)
            else:
                print("You stand still")
                continue

            a = room.column + x
            b = room.row + y
            if 0 <= a < len(tilemap) and 0 <= b < len(tilemap[0]):
                room.userpos = tilemap[a][b]
                if room.userpos == 1:
                    print("Astronomy")
                elif room.userpos == 2:
                    print("Trinkets")
                elif room.userpos == 3:
                    print("Memory Game")
                elif room.userpos == 4:
                    print("Charades")
                elif room.userpos == 5:
                    print("Empty Street")
                elif room.userpos == 6:
                    print("Fortune Teller")
                elif room.userpos == 7:
                    print("Lantern Painting")
                elif room.userpos == 8:
                    print("Empty Street")
                elif room.userpos == 9:
                    print("Food")
                elif room.userpos == 10:
                    print("Puzzle")
                elif room.userpos == 11:
                    print("Empty Street - Start")
                elif room.userpos == 12:
                    print("Dance")
                else:
                    print("Error")
                room.column = a
                room.row = b
            else:
                print("You cannot move in that direction.")


class Room(object):
    def __init__(self, column, row):
        self.userpos = tilemap[column][row]
        self.column = column
        self.row = row

ground = 0
activity = 1
tilemap = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           [10, 11, 12]]

room = Room(3, 1)
user = Player('Bryce')

def print_map():
    for i in range(len(tilemap)):
        for j in range(len(tilemap[i])):
            if i == room.column and j == room.row:
                print("W", end=" ")  # Print "W" at the player's position
            else:
                print(tilemap[i][j], end=" ")
        print()

print("It’s a beautiful day in the city of Adenasa.")
print("The last day of the month of Leaffall, today is the celebration of the Foxlight festival.")
print("Tonight when the world goes dark, an iridescent light in the shape of a fox will fill the sky. ")
print("Everyone gathered in the city will watch in wonder and awe at the unexplained magic that fills the realm of Kysmanthia. ")

while True:
    explore = input("Would you like to explore the festival?")
    if explore in ("Yes", "yes"):
        user.movement()
        break
    elif explore in ("No", "no"):
        break
    else:
        print("Error: Please type yes or no.")
        continue

print("You wait until it is time for the Foxlights to appear.")