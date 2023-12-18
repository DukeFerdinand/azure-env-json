import json
import sys

# Get all arguments
args = sys.argv
# Get first argument if it exists
if len(args) > 1:
    first = args[1]
else:
    first = ".env"

print(f"Reading from {first}")

# Open file
with open(first, "r") as f:
    # Read all lines
    lines = f.readlines()

# Remove all lines that start with # or are empty
lines = [line for line in lines if not line.startswith("#") and line != "\n"]

# Remove all newlines
lines = [line.strip() for line in lines]

# Split all lines by =
lines = [line.split("=", maxsplit=1) for line in lines]

final = []
for line in lines:
    key = line[0].strip()
    value = line[1].strip().replace('"', "")
    final.append({
        "name": key,
        "value": value,
        "slotSetting": False
    })


print(json.dumps(final, indent=5))

