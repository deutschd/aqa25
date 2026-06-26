import os
import re

# Change name to all files inside folder to the name like claim_id: "like_1", next one: "like_2"

folder_path = r"C:"
pattern = re.compile(r'"claim_id":"(de_\nSOMETHING_\d+)"') #find element change something to uat

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        match = pattern.search(content)
        if match:
            claim_id = match.group(1)  # e.g., de_nice_23
            new_filename = f"{claim_id}.json"
            new_path = os.path.join(folder_path, new_filename)

            os.rename(file_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")