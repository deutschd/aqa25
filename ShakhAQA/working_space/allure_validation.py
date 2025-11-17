
import re
from pathlib import Path

"""
replace_placeholder_cases.py

Usage:
- Configure the CONFIG section below.
- Run:  python replace_placeholder_cases.py

Core behavior (simple):
- Copies the entire template line (full body) from the input CSV and replaces ALL occurrences of PLACEHOLDER
  with each value from REPLACEMENTS_CSV (comma-separated).
- Writes the generated lines to OUTPUT_FILE (one line per replacement).

Optional toggles:
- INCREMENT_LEADING_NUMBER: if True, increments the leading number (before the first ';') by +1 per case.
- INCREMENT_REQUEST_ID: if True, for every occurrence of "p_request_id": "<value>":
    - if <value> ends with digits, increments those digits,
    - otherwise appends "-<counter>" (counter increases each time we touch an id).
"""

# ===================== CONFIG =====================
INPUT_FILE  = r"D:\OCTOBANK\testing methods\test_for_script.csv"
OUTPUT_FILE = r"D:\OCTOBANK\testing methods\test_put.csv"
ENCODING    = "utf-8"

PLACEHOLDER = "J_DIRECTOR_NAME"
REPLACEMENTS_CSV = "EMPTY_VALUE,TOO_LONG_VALUE,NON_ASCII,WITH_SPACES,LEADING_SPACE,TRAILING_SPACE"

# Toggles
INCREMENT_LEADING_NUMBER = False
INCREMENT_REQUEST_ID     = False

# If you enable INCREMENT_LEADING_NUMBER and want to force base (e.g., 20048), set below;
# otherwise it will auto-detect from the template line.
FORCE_LEADING_BASE = None

# Starting counter if some p_request_id values lack trailing digits and we need to append "-<counter>"
REQUEST_ID_START_NUM = 1
# =================== END CONFIG ===================


def parse_replacements(csv_text: str):
    return [x.strip() for x in csv_text.split(",") if x.strip()]


leading_num_re = re.compile(r"^(\s*)(\d+)(;)", re.ASCII)
req_field_re   = re.compile(r'("{1,2}p_request_id"{1,2}\s*:\s*"{1,2})([^"]+?)("{1,2})')

def detect_leading_base(line: str):
    m = leading_num_re.match(line)
    return int(m.group(2)) if m else None

def set_leading_number(line: str, new_number: int) -> str:
    m = leading_num_re.match(line)
    if not m:
        return line
    prefix, _, semi = m.groups()
    return f"{prefix}{new_number}{semi}{line[m.end():]}"

def replace_all_placeholder(text: str, old: str, new: str) -> str:
    return text.replace(old, new)

def bump_all_req_ids(text: str, case_index: int, counter_state: dict) -> str:
    """
    For each p_request_id occurrence:
    - If value ends with digits, increment those digits by +case_index (so each case moves forward).
    - Else, append "-<counter>" using counter_state['next'] and increment it.
    """
    def repl(m):
        start, value, endq = m.groups()
        # trailing digits?
        mnum = re.search(r'(\d+)$', value)
        if mnum:
            num_s = mnum.group(1)
            num_i = int(num_s) + case_index
            new_value = value[:-len(num_s)] + str(num_i)
        else:
            # Append a running counter
            new_value = f"{value}-{counter_state['next']}"
            counter_state['next'] += 1
        return f"{start}{new_value}{endq}"
    return req_field_re.sub(repl, text)

def main():
    inp = Path(INPUT_FILE)
    if not inp.exists():
        raise FileNotFoundError(f"Input file not found: {inp}")
    lines = inp.read_text(encoding=ENCODING, errors="replace").splitlines()

    # pick template line: first containing PLACEHOLDER, else first line
    template_idx = next((i for i, ln in enumerate(lines) if PLACEHOLDER in ln), 0)
    template = lines[template_idx]

    # replacements
    replacements = parse_replacements(REPLACEMENTS_CSV)
    if not replacements:
        raise ValueError("No replacements provided in REPLACEMENTS_CSV.")

    # base number (if enabled)
    base_leading = FORCE_LEADING_BASE if FORCE_LEADING_BASE is not None else detect_leading_base(template)

    out_lines = []
    req_counter = {'next': REQUEST_ID_START_NUM}

    for i, rep in enumerate(replacements, start=1):
        text = template

        # (optional) leading number
        if INCREMENT_LEADING_NUMBER and base_leading is not None:
            text = set_leading_number(text, base_leading + i)

        # replace placeholder everywhere
        text = replace_all_placeholder(text, PLACEHOLDER, rep)

        # (optional) bump p_request_id values
        if INCREMENT_REQUEST_ID:
            text = bump_all_req_ids(text, i, req_counter)

        out_lines.append(text)

    Path(OUTPUT_FILE).write_text("\n".join(out_lines), encoding=ENCODING)
    print(f"Generated {len(out_lines)} line(s) -> {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
