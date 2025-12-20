
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
    
    # Check if fix already applied
    if "FarmHudMapCluster" in content:
        print("FarmHud fix seems to be already present.")
        exit()

    # Fix for MUE
    # Target: function Nx.Map:MUE() if not self.MMO1 then return end
    mue_target = "function Nx.Map:MUE() if not self.MMO1 then return end"
    mue_replace = "function Nx.Map:MUE() if FarmHudMapCluster and FarmHudMapCluster:IsShown() then return end if not self.MMO1 then return end"
    
    if mue_target in content:
        content = content.replace(mue_target, mue_replace)
        print("Applied MUE fix.")
    else:
        print("Warning: MUE target not found.")

    # Fix for MiU
    # Target: function Nx.Map:MiU() if not self.MMO1 then self:MDF1() return end
    miu_target = "function Nx.Map:MiU() if not self.MMO1 then self:MDF1() return end"
    miu_replace = "function Nx.Map:MiU() if FarmHudMapCluster and FarmHudMapCluster:IsShown() then return end if not self.MMO1 then self:MDF1() return end"
    
    if miu_target in content:
        content = content.replace(miu_target, miu_replace)
        print("Applied MiU fix.")
    else:
        print("Warning: MiU target not found.")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("File saved.")

except Exception as e:
    print(f"Error: {e}")
