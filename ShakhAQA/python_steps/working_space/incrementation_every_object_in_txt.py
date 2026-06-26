import re

# full path to your file
input_file = r"C:\Users\user\Downloads\report_new.txt"
output_file = r"C:\Users\user\Downloads\report_new_ia111m.txt"

# starting number
counter = 111

with open(input_file, "r", encoding="utf-8") as infile:
    content = infile.read()

# regex: match "p_request_id": "dsfk-...-12ор-338"
pattern = r'"p_request_id":\s*"dsfk-[^"]*-12ор-338"'

def replacer(match):
    global counter
    return f'"p_request_id": "dsfk-x{counter}-12ор-338"'.replace("\u202f", " ")  # normalize spaces

    # increments after replacement
    counter += 1

# fix: need to increment correctly outside .replace()
def replacer(match):
    global counter
    replacement = f'"p_request_id": "dsfk-x{counter}-12ор-338"'
    counter += 1
    return replacement

updated_content = re.sub(pattern, replacer, content)

with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.write(updated_content)

print(f"✅ Done! Updated file saved at: {output_file}")