
import os
import re

file_path = "C:/Ascension Launcher/resources/client/Interface/AddOns/Carbonite/Carbonite.lua"

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
    
    print(f"File length: {len(content)}")

    # 1. Search for aliases
    # local X = Minimap
    alias_matches = re.findall(r"local\s+(\w+)\s*=\s*Minimap", content)
    print(f"Minimap aliases found: {alias_matches}")
    
    # 2. Search for MMO1 usage
    keyword = "MMO1"
    idx = content.find(keyword)
    print(f"\n--- Searching for '{keyword}' ---")
    count = 0
    while idx != -1:
        start = max(0, idx - 100)
        end = min(len(content), idx + 200)
        snippet = content[start:end].replace("\n", " ")
        print(f"Match {count+1}: ...{snippet}...")
        
        idx = content.find(keyword, idx + 1)
        count += 1
        if count > 20: 
            print("... limit reached ...")
            break

    # 3. Search for any SetParent calls that involve the minimap alias if found
    if alias_matches:
        for alias in alias_matches:
            kp = f"{alias}:SetParent"
            print(f"\n--- Searching for '{kp}' ---")
            idx = content.find(kp)
            if idx != -1:
                start = max(0, idx - 100)
                end = min(len(content), idx + 200)
                print(f"Match: ...{content[start:end]}...")
            else:
                print("No matches.")

except Exception as e:
    print(f"Error: {e}")
