
import os

file_path = "C:/Ascension Launcher/resources/client/Interface/AddOns/Carbonite/Carbonite.lua"
output_path = "debug_mm_setparent.txt"

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
        for i, line in enumerate(lines):
            if "SetParent" in line and ("Minimap" in line or "Nx.Map" in line):
                 f.write(f"{i+1}: {line.strip()}\n")
                 
            # Also check for MapMMOwn usage
            if "MapMMOwn" in line:
                 f.write(f"{i+1} (MapMMOwn): {line.strip()}\n")

            # Check for NXCmdMMOwnChange definition
            if "function" in line and "NXCmdMMOwnChange" in line:
                 # Print context
                 f.write(f"\n--- Function Def at {i+1} ---\n")
                 for j in range(i, min(len(lines), i+30)):
                     f.write(f"{j+1}: {lines[j].strip()}\n")
                 f.write("----------------\n")

    print(f"Saved {output_path}")

except Exception as e:
    print(f"Error: {e}")
