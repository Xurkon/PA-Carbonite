
import os

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
    
    keywords = ["NXCmdMMOwnChange", "function Nx.Map:MM_Update", "Minimap:SetParent"]
    
    print(f"File length: {len(content)} characters.")

    for kw in keywords:
        print(f"\n--- Searching for '{kw}' ---")
        idx = content.find(kw)
        while idx != -1:
            # Context window
            start = max(0, idx - 300)
            end = min(len(content), idx + 500)
            snippet = content[start:end]
            
            # Clean up newlines for display
            # snippet = snippet.replace('\r', '') 
            
            print(f"...{snippet}...")
            
            # Find next
            idx = content.find(kw, idx + 1)
            # Limit to first few matches to avoid spam
            if idx > 100000 and kw == "Minimap:SetParent": # Just an example limit
                 print("(Stopping search for this keyword)")
                 break

except Exception as e:
    print(f"Error: {e}")
