from Dice import Roll

class Player(object): #But seriously what's the point of this?
  def __init__(self, name):
    self.name = name

  def movement(self):
    while True:
      print_map()
      print("\n   Which direction would you like to go?")
      print("   1.North, 2.South, 3.East, 4.West, 0. Quit")
      move = input("   > ").lower()
      if move == '1':
        x, y = (-1, 0)
      elif move == '2':
        x, y = (1, 0)
      elif move == '3':
        x, y = (0, 1)
      elif move == '4':
        x, y = (0, -1)
      elif move == '0':
        break
      else:
        print("\n   You stand still")
        continue

      a = room.column + x
      b = room.row + y
      if 0 <= a < len(tilemap) and 0 <= b < len(tilemap[0]):
        room.userpos = tilemap[a][b]
        if room.userpos == 1:
          Astronomy()
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
        print("   You cannot move in that direction.")


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
  print(" \n ")
  for i in range(len(tilemap)):
    for j in range(len(tilemap[i])):
      if i == room.column and j == room.row:
        print("W", end=" ")  # Print "W" at the player's position
      else:
        print(tilemap[i][j], end=" ")
    print()

def FoxlightFestival():
  while True:
    print("\n \n   Would you like to explore the festival?")
    explore = input("   >   ").strip().lower()
    if explore == "yes":
      user.movement()
      break
    elif explore == "no":
      break
    else:
      print("   Error: Please type yes or no.")
      continue

  print("\n   You wait until it is time for the Foxlights to appear.")

def main():
	print("   It’s a beautiful day in the city of Adenasa.")
	print("   The last day of the month of Leaffall, today is the celebration of the Foxlight festival.")
	print("   Tonight when the world goes dark, an iridescent light in the shape of a fox will fill the sky. ")
	print("   Everyone gathered in the city will watch in wonder and awe at the unexplained magic that fills the realm of Kysmanthia. ")

	FoxlightFestival()

def Astronomy():
    print("\n   As a part of the festival a local astronomer has set up a makeshift observatory, offering stargazing sessions.")
    print("   A cluster of telescopes, their lenses gleaming in the moonlight, points skyward, inviting eager stargazers to peer into the cosmos.")
    print("   The astronomer, a figure of quiet intensity, stands beside a chalkboard adorned with celestial diagrams, ready to unravel the mysteries of the night sky.")
    print("\n   Would you like to stargaze? yes or no?")
    choice = input("   >   ")
    while True:
        if choice in ("Yes", "yes"):
            print("   Making a Perception Check...")
            print("   Rolling...")
            roll_results, total = Roll.d20(1)
            print("   ", total)
            if total < 12:
                print("   The sky is beautiful but you don't see any constellations.")
            elif total == 12 or total == 13:
                print("   You see the Fox's Tail. This constellation resembles a graceful fox with its tail extended. It's said to represent the Foxlights themselves and is associated with good fortune and protection.")
            elif total == 14 or total == 15:
                print("   You see the Starfall Cascade. A dazzling meteor shower that appears as a cascade of shimmering stars. It's believed to be the leftover memory of a long forgotten fallen angel.")
            elif total == 16 or total == 17:
                print("   You see the Twilight Serpent. A long, winding constellation resembling a serpent with iridescent scales. It is associated with mysteries and hidden knowledge.")
            elif total == 18 or total == 19:
                print("   You see the Aurora Phoenix. An incredibly rare celestial event that occurs just before the Foxlights' arrival. It resembles a blazing phoenix in the twilight sky, seemingly heralding the imminent arrival of the Foxlights.")
            elif total == 20:
                print("   You see the Dragon's Eclipse.  A complex alignment of stars that forms the shape of a dragon partially eclipsing the moon. It is said to foretell the awakening of an ancient dragon or a great conflict.")
            else:
                print("Error")
            break
        elif choice in ("No", "no"):
            print("You move on to the next part of the festival.")
            break
        else:
            print("Invalid choice. Try again.")
            continue

main()
