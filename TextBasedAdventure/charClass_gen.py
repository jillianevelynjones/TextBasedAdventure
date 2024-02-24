def charClass_gen():
    print("  \n   ......................")
        print("  \n   Now it's time to choose your class")
        print("   Options are: ")
        print("      Fighter")
        while True:
            charClass = input(f"   Enter class: ")
            if charClass in ("fighter", "Fighter"):
                print("stuff")
                break
            else:
                print("Sorry! Only fighter is available")
                continue

def Fighter():
    hitdice = 10
    hitpoint1 = 10+