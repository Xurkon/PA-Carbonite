
import os

file_path = "C:/Ascension Launcher/resources/client/Interface/AddOns/Carbonite/Carbonite.lua"
keyword = "function Nx.Fav:CIN()"
context = 50

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
        return [x.decode('utf-8', 'replace') for x in f.readlines()]

try:
    lines = read_file_safely(file_path)
    
    target_lines = []
    for i, line in enumerate(lines):
        if keyword in line:
            target_lines.append(i + 1)
            
    print(f"Found {len(target_lines)} matches for '{keyword}'")
    
    for lineno in target_lines:
         print(f"--- MATCH at line {lineno} ---")
         idx = lineno - 1
         start = max(0, idx)
         end = min(len(lines), idx + context)
         for i in range(start, end):
             print(f"{i+1}: {lines[i].strip()}")

except Exception as e:
    print(f"Error: {e}")
