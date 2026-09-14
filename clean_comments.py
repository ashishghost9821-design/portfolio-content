import shutil
import glob

files = sorted(glob.glob("project*.c"))
removed_total = 0
report = []

for fname in files:
    with open(fname, "r") as f:
        lines = f.readlines()

    new_lines = []
    removed = 0
    for line in lines:
        # Only strips the decorative box border + the tutorial attribution line.
        # Everything else (Concepts practiced, FORMULAS, WARNING notes,
        # section dividers, inline explanations) is left completely untouched.
        if "╔" in line or "╚" in line or "Bro Code Tutorial" in line:
            removed += 1
            continue
        new_lines.append(line)

    if removed:
        shutil.copy(fname, fname + ".bak")
        with open(fname, "w") as f:
            f.writelines(new_lines)
        report.append(f"{fname}: removed {removed} line(s), backup at {fname}.bak")
        removed_total += removed
    else:
        report.append(f"{fname}: nothing to remove")

for line in report:
    print(line)
print(f"\nTotal lines removed: {removed_total}")
