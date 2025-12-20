
import os

file_path = "C:/Ascension Launcher/resources/client/Interface/AddOns/Carbonite/Carbonite.lua"

# User reported lines: 5841 and 24784. 
# Since I added code, these should be relatively accurate to the current file state.

locations = [
    {"line": 5841, "name": "Error 1 (pairs nil)", "context": 20},
    {"line": 24784, "name": "Error 2 (na2 nil)", "context": 20}
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
    print(f"File has {len(lines)} lines.\n")
    
    for loc in locations:
        target = loc["line"] - 1 # 0-indexed
        context = loc["context"]
        print(f"--- {loc['name']} around Line {loc['line']} ---")
        
        start = max(0, target - context)
        end = min(len(lines), target + context + 1)
        
        # Check if line is within bounds
        if target < len(lines):
             # Print range
             for i in range(start, end):
                 marker = ">> " if i == target else "   "
                 print(f"{marker}{i+1}: {lines[i].strip()}")
        else:
            print(f"Line {loc['line']} is out of bounds.")
        print("\n")

except Exception as e:
    print(f"Error: {e}")
