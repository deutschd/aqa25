import os

# Folder to scan
FOLDER = r"D:\PythonTraining"
OUTPUT = r"D:\file_names.txt"

def main():
    # get only file names, not folders
    files = [f for f in os.listdir(FOLDER) if os.path.isfile(os.path.join(FOLDER, f))]

    with open(OUTPUT, "w", encoding="utf-8") as out:
        for name in files:
            out.write(name + "\n")

    print(f"Saved {len(files)} file names to {OUTPUT}")

if __name__ == "__main__":
    main()