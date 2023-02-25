import csv
import os
from NPCGenerator import NPCGenerator

# Create the necessary directory if it doesn't exist
directory = os.path.join(os.path.expanduser("~"), "Desktop", "NPCs")
if not os.path.exists(directory):
    os.makedirs(directory)

# Get the number of NPCs to generate from the user
num_npcs = int(input("How many NPCs do you want to generate? "))

# Generate the NPCs and write them to CSV file
npc_generator = NPCGenerator(num_npcs)
npcs = npc_generator.generate_npcs()

"""Below writes the top row in the CSV"""

csv_filename = os.path.join(directory, "NPC Random Generator.csv")
with open(csv_filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["race", "age", "gender",
                 "skin_color", "physical_feature", "hair_color",
                 "hair_length", "hair_texture", "facial_hair",
                 "speech_patterns", "personality_traits", "mannerisms"])

    """Below is the part that writes a row in the CSV"""
    for npc in npcs:
        writer.writerow([npc.race, npc.age, npc.gender,
                         npc.skin_color, npc.physical_feature,
                         npc.hair_color, npc.hair_length, npc.hair_texture,
                         npc.facial_hair, npc.speech_patterns,
                         npc.personality_traits, npc.mannerisms])

print(f"Generated {num_npcs} NPCs in {csv_filename}")

def main():
    num_npcs = int(input("Enter the number of NPCs to generate: "))
    npc_generator = NPCGenerator(num_npcs)
    npcs = npc_generator.generate_npcs()
    save_npcs_to_file(npcs)

if __name__ == "__main__":
    main()