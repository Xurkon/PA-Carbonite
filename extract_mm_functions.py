
import os

file_path = "C:/Ascension Launcher/resources/client/Interface/AddOns/Carbonite/Carbonite.lua"
output_path = "debug_mm_functions.txt"

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
    
    keywords = ["function Nx.Map:MUE()", "function Nx.Map:MiU()"]
    
    with open(output_path, 'w', encoding='utf-8') as f:
        for kw in keywords:
            idx = content.find(kw)
            if idx != -1:
                f.write(f"\n--- {kw} ---\n")
                # Extract until next function definition or reasonable length
                start = idx
                end = content.find("function Nx", idx + 1)
                if end == -1 or end - start > 5000:
                    end = min(len(content), start + 2000)
                
                snippet = content[start:end].replace("\n", " ") # Flatten for easier reading if minified
                
                # Try to format it a bit? No, just raw is safer to match.
                f.write(snippet + "\n")
            else:
                 f.write(f"\n--- {kw} NOT FOUND ---\n")

    print(f"Saved {output_path}")

except Exception as e:
    print(f"Error: {e}")
