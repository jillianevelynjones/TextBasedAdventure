import csv
import os
from NPCGenerator import NPCGenerator


# Create the necessary directory if it doesn't exist
def save_npcs_to_file(npcs, csv_filename):
    directory = os.path.join(os.path.expanduser("~"), "Desktop", "NPCs")
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Generate the NPCs and write them to CSV file
    with open(csv_filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "race", "age", "gender",
                         "skin_color", "physical_feature", "hair_color",
                         "hair_length", "hair_texture", "facial_hair",
                         "speech_patterns", "personality_traits", "mannerisms"])

        for npc in npcs:
            writer.writerow([npc.first_name, npc.race, npc.age, npc.gender,
                             npc.skin_color, npc.physical_feature, npc.hair_color,
                             npc.hair_length, npc.hair_texture, npc.facial_hair,
                             npc.speech_patterns, npc.personality_traits, npc.mannerisms])


def main():
    # Get the number of NPCs to generate from the user
    num_npcs = int(input("How many NPCs do you want to generate? "))

    # Define the CSV filename
    csv_filename = os.path.join(os.path.expanduser("~"), "Desktop", "NPCs", "NPC Random Generator.csv")

    npc_generator = NPCGenerator(num_npcs)
    npcs = npc_generator.generate_npcs()

    save_npcs_to_file(npcs, csv_filename)

    print(f"Generated {num_npcs} NPCs in {csv_filename}")


if __name__ == "__main__":
    main()
