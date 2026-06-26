import pandas as pd

# Paths
excel_path = r"C:\"
csv_path = r"C:\"

# Load Excel (no headers since you only have numbers)
df = pd.read_excel(excel_path, header=None)

# Rename for clarity
df.columns = ["number", "connected"]

# Fixed template parts
fixed_left = [
    "99999999", "solana", "01.09.2025", "00980", "99999999", "01.09.2025",
    1, 8
]
fixed_middle = ["", 1, "12.12.1999", "998909914398", "\npinflnumber", "", "",
                6, "AD", "5111111", "24.09.2016"]
fixed_right = ["Karasu", "7956"]

# Build CSV rows
rows = []
for _, row in df.iterrows():
    num = row["number"]
    conn = row["connected"]

    csv_row = (
        fixed_left
        + [num, conn]  # replaces 1190,ODIN
        + fixed_middle
        + [str(num), str(conn), str(num), str(conn)]  # last 4 values
        + fixed_right
    )
    rows.append(csv_row)

# Define column headers
columns = [
    "col1","col2","col3","col4","col5","col6","col7","col8",
    "region","region2",
    "col9","col10","col11","col12","col13","col14","col15","col16","col17","col18","col19",
    "region1_1","region2_1","region_dup1","region_dup2",
    "col20","col21"
]

# Save CSV
out_df = pd.DataFrame(rows, columns=columns)
out_df.to_csv(csv_path, index=False, quoting=1)

print(f"✅ CSV generated at: {csv_path}")