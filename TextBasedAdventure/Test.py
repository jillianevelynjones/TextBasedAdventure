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
                break

            a = room.column + x
            b = room.row + y
            if 0 <= a < len(tilemap) and 0 <= b < len(tilemap[0]):
                room.userpos = tilemap[a][b]
                if room.userpos == "A":
                    print("ACTIVITY!")
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

def main():
    inp = input("Press any button to continue.: ")
    if inp != '':
        user.movement()
        print(room.userpos)
main()