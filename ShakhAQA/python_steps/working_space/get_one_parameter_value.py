import re

# Path to your original file
input_file = r"D:\Scripts\thisistxt.txt"

# Path to the new file where results will be saved
output_file = r"D:\Scripts\codes_only.txt"

# Read the content with proper encoding
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# Extract all numbers after "CODE":
codes = re.findall(r'"CODE":\s*(\d+)', text)

# Join them as comma-separated string
result = ", ".join(codes)

# Write the result to a new TXT file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(result)

print(f"✅ Done! {len(codes)} codes extracted and saved to {output_file}")