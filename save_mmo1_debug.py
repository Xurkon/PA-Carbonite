
import os

file_path = "C:/Ascension Launcher/resources/client/Interface/AddOns/Carbonite/Carbonite.lua"
output_path = "debug_mmo1.txt"

def read_file_safely(path):
    encodings = ['utf-8', 'latin-1', 'cp1252', 'utf-16']
    for enc in encodings:
        try:
            with open(path, 'r', encoding=enc) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
        except Exception:
            continue
    with open(path, 'rb') as f:
        return f.read().decode('utf-8', 'replace')

try:
    content = read_file_safely(file_path)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        idx = content.find("MMO1")
        while idx != -1:
            # Context window
            start = max(0, idx - 150)
            end = min(len(content), idx + 150)
            snippet = content[start:end].replace('\n', ' ')
            f.write(f"--- Match at index {idx} ---\n")
            f.write(f"...{snippet}...\n\n")
            
            idx = content.find("MMO1", idx + 1)

    print(f"Saved {output_path}")

except Exception as e:
    print(f"Error: {e}")
