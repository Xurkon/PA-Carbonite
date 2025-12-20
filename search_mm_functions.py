
import os

file_path = "C:/Ascension Launcher/resources/client/Interface/AddOns/Carbonite/Carbonite.lua"
keywords = ["NXCmdMMOwnChange", "Minimap:SetParent", "SetParent(Minimap"]
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
    with open(path, 'rb') as f:
        return [x.decode('utf-8', 'replace') for x in f.readlines()]

try:
    lines = read_file_safely(file_path)
    print(f"Searching {len(lines)} lines")
    
    for i, line in enumerate(lines):
        line_content = line.strip()
        for kw in keywords:
            if kw in line_content:
                print(f"\n--- MATCH '{kw}' at Line {i+1} ---")
                start = max(0, i - context)
                end = min(len(lines), i + context)
                for j in range(start, end):
                    print(f"{j+1}: {lines[j].strip()}")

except Exception as e:
    print(f"Error: {e}")
