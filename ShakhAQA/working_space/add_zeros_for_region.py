import pandas as pd

# Paths
input_csv = r"C:regiontest.csv"
output_csv = r"C:regiontest_fixed.csv"

# Load CSV (no header)
df = pd.read_csv(input_csv, header=None)

def pad_region(val):
    """Pad region (first number): if 1 digit → add 0, else keep"""
    val = str(val).strip()
    return val.zfill(2) if len(val) == 1 else val

def pad_region2(val):
    """Pad region2 (second number):
       1 digit → 2 zeros (005), 2 digits → 1 zero (051), 3 digits → keep"""
    val = str(val).strip()
    if len(val) == 1:
        return val.zfill(3)  # 5 → 005
    elif len(val) == 2:
        return val.zfill(3)  # 26 → 026
    else:
        return val           # keep 3 digits

# Get indexes of last 7 columns
last7 = df.columns[-7:]

# Apply formatting
df[last7[0]] = df[last7[0]].apply(pad_region)   # region
df[last7[1]] = df[last7[1]].apply(pad_region2)  # region2
df[last7[2]] = df[last7[2]].apply(pad_region)   # region1_1
df[last7[3]] = df[last7[3]].apply(pad_region2)  # region2_1

# Save
df.to_csv(output_csv, index=False, header=False)

print(f"✅ Fixed CSV saved at: {output_csv}")