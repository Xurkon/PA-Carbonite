
import os

file_path = "C:/Ascension Launcher/resources/client/Interface/AddOns/Carbonite/Carbonite.lua"
keyword = "NXCmdFavCartImport"
context = 20

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
    # Fallback to binary and decode errors ignore
    with open(path, 'rb') as f:
        # read binary, decode replace
        return [x.decode('utf-8', 'replace') for x in f.readlines()]

try:
    lines = read_file_safely(file_path)
    
    target_line = -1
    for i, line in enumerate(lines):
        if keyword in line:
            target_line = i + 1
            print(f"MATCH at line {target_line}: {line.strip()}")
            # We want the definition, so if this is just a menu item we keep looking?
            # actually let's see context
    
    if target_line != -1:
         # Extract context around the LAST match (likely definition?)
         # Or list all matches?
         print("--- Context ---")
         idx = target_line - 1
         start = max(0, idx - context)
         end = min(len(lines), idx + context + 30)
         for i in range(start, end):
             print(f"{i+1}: {lines[i].strip()}")

except Exception as e:
    print(f"Error: {e}")
