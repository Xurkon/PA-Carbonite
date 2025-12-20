
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
    
    # Fix 3: ReC nil map index
    # Context (from debug_regressions_2.txt):
    # 24841: local map=self.Map:GeM(1)
    # 24842: if map.RMI then
    
    # Error: "attempt to index local 'map' (a nil value)" at 24842
    # So `map` is nil.
    # Fix: check if map exists.
    
    fix3_search = "local map=self.Map:GeM(1)\nif map.RMI then"
    fix3_replace = "local map=self.Map:GeM(1)\nif map and map.RMI then"
    
    if fix3_search in content:
        content = content.replace(fix3_search, fix3_replace)
        print("Fix 3 applied: ReC map nil check")
    else:
        print("Warning: Fix 3 code not found.")

    # Fix 4: ITCZ compare number with nil
    # Context (from debug_regressions_2.txt):
    # 6983: function Nx.Map:ITCZ(maI)
    # 6984: if maI>=10000 then
    
    # Error: "attempt to compare number with nil" at 6984
    # So `maI` is nil.
    # Fix: add default or check.
    
    fix4_search = "function Nx.Map:ITCZ(maI)\nif maI>=10000 then"
    fix4_replace = "function Nx.Map:ITCZ(maI)\nif maI and maI>=10000 then"
    
    if fix4_search in content:
        content = content.replace(fix4_search, fix4_replace)
        print("Fix 4 applied: ITCZ maI nil check")
    else:
        print("Warning: Fix 4 code not found.")
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("File saved.")

except Exception as e:
    print(f"Error: {e}")
