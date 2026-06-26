
import re
from pathlib import Path

"""
make_cases_from_csv.py

What it does (per user rules):
1) Takes a CSV where each line starts with a number like "20048;" and contains a big test-case blob.
2) Copies the entire line as a template and produces N cases (N = number of replacements you provide).
3) For each generated case:
   - Increments the *leading* number (before the first ';') by +1, +2, ... (continuing across cases).
   - Replaces all occurrences of PLACEHOLDER (e.g., J_DIRECTOR_NAME) with the current replacement value.
   - Finds every "p_request_id": "<BASE_PREFIX><num>" and increments <num> sequentially across all occurrences
     and across all cases (global counter). Example base "d11x-45ca-2c-" with start=1 -> 2,3,4,...
4) Writes the new cases to an output CSV.

Configure the CONFIG section below.
"""

# ===================== CONFIG (EDIT BELOW) =====================
INPUT_FILE  = r"D:\OCTOBANK\testing methods\test_for_script.csv"     # Source CSV with your example row(s)
OUTPUT_FILE = r"D:\OCTOBANK\testing methods\result.csv" # Where to save the generated cases
ENCODING    = "utf-8"

# Which placeholder token to replace everywhere in the line body:
PLACEHOLDER = "J_DIRECTOR_NAME"

# Comma-separated list of values that should replace PLACEHOLDER in order.
# You can put a single value (same as placeholder) if you only want to test number/req_id increments.
REPLACEMENTS_CSV = "J_SMALL_BUSINESS,J_DISTR,J_REGION,J_INN_HEAD_ORGANIZATION,J_OKPO,J_SOATO,J_OPF,J_SIGN_TRADE"  # e.g.: "J_DIRECTOR_NAME,J_DIRECTOR_PINFL,J_DIRECTOR_POSITION"

# Request ID handling:
# We will search for p_request_id values like:  "p_request_id": "d11x-45ca-2c-1"
# and increment the trailing number globally across all matches.
REQUEST_ID_BASE_PREFIX = "d11x-45ca-2c-"  # Everything before the trailing number
REQUEST_ID_START_NUM   = 1                # Starting number; the script will output 2,3,4,...

# If your line starts with something like 20048; we detect and increment from that number.
# If you want to force a specific base, set FORCE_LEADING_BASE = 20048 (or None to auto-detect)
FORCE_LEADING_BASE = None
# =================== END OF CONFIG ============================


def parse_replacements(csv_text: str):
    return [x.strip() for x in csv_text.split(",") if x.strip()]


leading_num_re = re.compile(r"^(\s*)(\d+)(;)", re.ASCII)

# Matches: "p_request_id": "d11x-45ca-2c-<digits>"
# Also supports doubled quotes in CSV: ""p_request_id"": ""...""
req_id_re = re.compile(
    r'("{1,2}p_request_id"{1,2}\s*:\s*"{1,2})('
    + re.escape(REQUEST_ID_BASE_PREFIX) +
    r')(\d+)("{1,2})'
)


def detect_leading_base(line: str):
    m = leading_num_re.match(line)
    if not m:
        return None
    return int(m.group(2))


def set_leading_number(line: str, new_number: int) -> str:
    m = leading_num_re.match(line)
    if not m:
        return line
    prefix, _, semi = m.groups()
    return f"{prefix}{new_number}{semi}{line[m.end():]}"


def replace_placeholder(line: str, old: str, new: str) -> str:
    # Replace ALL occurrences (the user examples show the field can appear in many places)
    return line.replace(old, new)


def bump_all_request_ids_globally(text: str, next_number: int) -> tuple[str, int]:
    """
    Replace every p_request_id that matches the base prefix + trailing digits,
    incrementing the number each time we see a match. Returns (new_text, new_next_number).
    """
    def repl(m):
        nonlocal next_number
        start, base, num, endq = m.groups()
        next_number += 1
        return f"{start}{base}{next_number}{endq}"

    new_text = req_id_re.sub(repl, text)
    return new_text, next_number


def main():
    src = Path(INPUT_FILE)
    if not src.exists():
        raise FileNotFoundError(f"Input file not found: {src}")

    lines = src.read_text(encoding=ENCODING, errors="replace").splitlines()

    # Use the first line containing the placeholder as template.
    template_idx = None
    for i, ln in enumerate(lines):
        if PLACEHOLDER in ln:
            template_idx = i
            break
    if template_idx is None:
        # If not found, fallback to the first line
        template_idx = 0

    template = lines[template_idx]
    base_leading = FORCE_LEADING_BASE if FORCE_LEADING_BASE is not None else detect_leading_base(template)

    replacements = parse_replacements(REPLACEMENTS_CSV)
    if not replacements:
        raise ValueError("No replacements provided in REPLACEMENTS_CSV.")

    # Global counter for p_request_id suffix number
    next_req_num = REQUEST_ID_START_NUM

    out_lines = []
    for idx, rep in enumerate(replacements, start=1):
        ln = template

        # 1) Leading number: base + idx
        if base_leading is not None:
            ln = set_leading_number(ln, base_leading + idx)

        # 2) Replace placeholder everywhere
        ln = replace_placeholder(ln, PLACEHOLDER, rep)

        # 3) Increment ALL p_request_id occurrences globally, continuing across cases
        ln, next_req_num = bump_all_request_ids_globally(ln, next_req_num)

        out_lines.append(ln)

    # Save only the generated cases (by design)
    Path(OUTPUT_FILE).parent.mkdir(parents=True, exist_ok=True)
    Path(OUTPUT_FILE).write_text("\n".join(out_lines), encoding=ENCODING)

    print(f"Generated {len(out_lines)} case(s).")
    if base_leading is not None:
        print(f"Leading number started from {base_leading} -> now up to {base_leading + len(out_lines)}.")
    print(f"p_request_id numbering continued from {REQUEST_ID_START_NUM} to {next_req_num}.")
    print(f"Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
