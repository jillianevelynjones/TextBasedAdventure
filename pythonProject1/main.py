import csv
import os
from NPCGenerator import NPCGenerator


# Create the necessary directory if it doesn't exist
def save_npcs_to_file(npcs, csv_filename):
    directory = os.path.join(os.path.expanduser("~"), "Desktop", "NPCs")
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Write the NPCs to a CSV file
    csv_path = os.path.join(directory, csv_filename)
    with open(csv_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["race", "age", "gender",
                         "skin_color", "physical_feature", "hair_color",
                         "hair_length", "hair_texture", "facial_hair",
                         "speech_patterns", "personality_traits", "mannerisms"])
        for npc in npcs:
            writer.writerow([npc.race, npc.age, npc.gender,
                             npc.skin_color, npc.physical_feature,
                             npc.hair_color, npc.hair_length, npc.hair_texture,
                             npc.facial_hair, npc.speech_patterns,
                             npc.personality_traits, npc.mannerisms])

    print(f"Generated {len(npcs)} NPCs in {csv_path}")


def main():
    # Get the number of NPCs to generate from the user
    num_npcs = int(input("How many NPCs do you want to generate? "))

    # Define the CSV filename
    csv_filename = "NPC Random Generator.csv"

    npc_generator = NPCGenerator(num_npcs)
    npcs = npc_generator.generate_npcs()

    save_npcs_to_file(npcs, csv_filename)


if __name__ == "__main__":
    main()
