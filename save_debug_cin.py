
import os

file_path = "C:/Ascension Launcher/resources/client/Interface/AddOns/Carbonite/Carbonite.lua"
output_path = "debug_cin.txt"
keyword = "function Nx.Fav:CIN()"
context = 100

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
    
    target_lineno = -1
    for i, line in enumerate(lines):
        if keyword in line:
            target_lineno = i + 1
            break
            
    with open(output_path, 'w', encoding='utf-8') as f:
        if target_lineno != -1:
            f.write(f"Function found at line {target_lineno}\n")
            start = max(0, target_lineno - 1)
            end = min(len(lines), target_lineno - 1 + context)
            for i in range(start, end):
                 f.write(f"{i+1}: {lines[i].strip()}\n")
        else:
             f.write("Function not found\n")
             
    print("Debug file written.")

except Exception as e:
    print(f"Error: {e}")
