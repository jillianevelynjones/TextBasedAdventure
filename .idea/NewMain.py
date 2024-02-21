from NewNPCGenerator import NewNPCGenerator
from NewNPC import NewNPC

def main():
    num_npcs = int(input("How many NPCs do you want to generate?"))

    npc_generator = NewNPCGenerator(num_npcs)
    npcs = npc_generator.generate_npcs()

    print(f"Generated {num_npcs} NPCS: ")
    for npc in npcs:
        print (npc)

if __name__ == "__main__":
    main()