
file_path = "C:/Ascension Launcher/resources/client/Interface/AddOns/Carbonite/Carbonite.lua"
output_path = "debug_regressions.txt"

# Adjusting slightly for potential shifts, but using the reported numbers as anchors.
ranges = [
    (5830, 5860),
    (24760, 24800)
]

def read_file_safely(path):
    encodings = ['utf-8', 'latin-1', 'cp1252', 'utf-16']
    for enc in encodings:
        try:
            with open(path, 'r', encoding=enc) as f:
                return f.readlines()
        except UnicodeDecodeError:
            continue
        except Exception:
            continue
    with open(path, 'rb') as f:
        return [x.decode('utf-8', 'replace') for x in f.readlines()]

try:
    lines = read_file_safely(file_path)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        for start, end in ranges:
            f.write(f"--- Range {start} to {end} ---\n")
            for i in range(start - 1, end):
                 if i < len(lines):
                     f.write(f"{i+1}: {lines[i].strip()}\n")
            f.write("\n")

    print(f"Saved regression contexts")

except Exception as e:
    print(f"Error: {e}")
