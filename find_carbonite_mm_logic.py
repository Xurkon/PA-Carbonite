
import os
import re

file_path = "C:/Ascension Launcher/resources/client/Interface/AddOns/Carbonite/Carbonite.lua"

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
    print(f"Searching {len(lines)} lines for Minimap logic...")

    # Regex definitions
    re_mm_own = re.compile(r"NXCmdMMOwnChange")
    re_set_parent = re.compile(r"Minimap:SetParent")
    re_map_mm_own = re.compile(r"MapMMOwn") # The setting variable

    matches = []

    for i, line in enumerate(lines):
        # Gather interesting lines
        if re_mm_own.search(line) or re_set_parent.search(line) or re_map_mm_own.search(line):
             matches.append(i)

    # Group close matches to avoid spam, but for now just printing contexts
    # If too many, we limit.
    
    print(f"Found {len(matches)} matches. Showing first 5 and relevant contexts around function definitions.")
    
    shown_indices = set()
    
    for i in matches:
        if i in shown_indices: continue
        
        # Checking if this looks like a function definition or a significant block
        # "function NXCmdMMOwnChange" or just usage?
        
        is_func_def = "function" in lines[i] and ("NXCmd" in lines[i] or "SetParent" in lines[i])
        
        # We want to show logic blocks. 
        # Let's just show context for unique regions.
        
        start = max(0, i - 5)
        end = min(len(lines), i + 20)
        
        # Don't overlap too much
        already_shown = False
        for k in range(start, end):
            if k in shown_indices:
                already_shown = True
                break
        
        if not already_shown or is_func_def:
            print(f"\n--- Match at Line {i+1}: {lines[i].strip()} ---")
            for j in range(start, end):
                prefix = "> " if j == i else "  "
                print(f"{prefix}{j+1}: {lines[j].strip()}")
                shown_indices.add(j)
                
            if len(shown_indices) > 500: # Safety break if too much output
                print("\n... limit reached ...")
                break

except Exception as e:
    print(f"Error: {e}")
