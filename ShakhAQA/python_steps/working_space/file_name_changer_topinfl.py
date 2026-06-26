# import os
# import re
#
# # TAKE LAST PINFL AND MAKE A NAME FROM IT
# # Folder with your .txt files
# folder_path = r"C:\OCTOBANK_OCTOBANK_OCTOBANK\petr\txt_files"
#
# # Regex to find pinfl values
# pinfl_regex = re.compile(r'"pinfl"\s*:\s*"(\d+)"')
#
# # Go through all .txt files
# for filename in os.listdir(folder_path):
#     if not filename.lower().endswith(".txt"):
#         continue
#
#     file_path = os.path.join(folder_path, filename)
#
#     with open(file_path, 'r', encoding='utf-8') as f:
#         content = f.read()
#
#     # Find all pinfls
#     pinfls = pinfl_regex.findall(content)
#     if not pinfls:
#         print(f"❌ No PINFL found in {filename}")
#         continue
#
#     last_pinfl = pinfls[-1]
#     new_filename = f"{last_pinfl}.txt"
#     new_path = os.path.join(folder_path, new_filename)
#
#     # Avoid overwriting
#     if os.path.exists(new_path):
#         print(f"⚠️ Skipped: {new_filename} already exists")
#         continue
#
#     # Rename file
#     os.rename(file_path, new_path)
#     print(f"✅ Renamed: {filename} → {new_filename}")

# import os
# import re
#
# folder_path = r"C:\OCTOBANK_OCTOBANK_OCTOBANK\petr\txt_files"
#
# # Match pattern: pinfl_123.txt
# pattern = re.compile(r'^(30101119\d{3})(\d{3})_(\d+)\.txt$')
#
# for filename in os.listdir(folder_path):
#     match = pattern.match(filename)
#     if not match:
#         continue
#
#     pinfl_start, pinfl_suffix, suffix_number = match.groups()
#
#     # Format new 3-digit suffix (e.g. 1 → 001)
#     new_suffix = f"{int(suffix_number):03d}"
#
#     new_pinfl = pinfl_start + new_suffix
#     new_filename = f"{new_pinfl}.txt"
#
#     old_path = os.path.join(folder_path, filename)
#     new_path = os.path.join(folder_path, new_filename)
#
#     # Read and update content
#     with open(old_path, 'r', encoding='utf-8') as f:
#         content = f.read()
#
#     # Replace old pinfl with new one
#     old_pinfl = pinfl_start + pinfl_suffix
#     content = content.replace(old_pinfl, new_pinfl)
#
#     # Write updated content
#     with open(old_path, 'w', encoding='utf-8') as f:
#         f.write(content)
#
#     # Rename file
#     if os.path.exists(new_path):
#         print(f"⚠️ Skipped (already exists): {new_filename}")
#         continue
#
#     os.rename(old_path, new_path)
#     print(f"✅ Renamed: {filename} → {new_filename} and updated PINFL")
#


# MAKE PINFL = FILE NAME
import os
import re

folder_path = r"C:txt_files"

# Match pinfl values
pinfl_regex = re.compile(r'"pinfl"\s*:\s*"(\d{14})"')

for filename in os.listdir(folder_path):
    if not filename.lower().endswith('.txt'):
        continue

    old_path = os.path.join(folder_path, filename)

    with open(old_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all PINFLs
    pinfls = pinfl_regex.findall(content)
    if not pinfls:
        print(f"❌ No pinfl found in {filename}")
        continue

    last_pinfl = pinfls[-1]

    # Update all pinfls in file to last one (optional, or remove this block)
    content_updated = pinfl_regex.sub(f'"pinfl":"{last_pinfl}"', content)

    # Save updated content back to file
    with open(old_path, 'w', encoding='utf-8') as f:
        f.write(content_updated)

    # Rename file
    new_filename = f"{last_pinfl}.txt"
    new_path = os.path.join(folder_path, new_filename)

    # Avoid overwrite
    if os.path.exists(new_path):
        print(f"⚠️ Skipped renaming: {new_filename} already exists")
        continue

    os.rename(old_path, new_path)
    print(f"✅ Renamed: {filename} → {new_filename}")