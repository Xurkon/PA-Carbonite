
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
    
    # Fix 1: OP__3 pairs error
    # Original:
    # local pq=self.PaQ
    # for nam in pairs(pq) do
    
    fix1_search = "local pq=self.PaQ\nfor nam in pairs(pq) do"
    fix1_replace = "local pq=self.PaQ\nif pq then\nfor nam in pairs(pq) do"
    
    # We also need to close the "if" block.
    # The block ends with "end" at 5854.
    # 5850: if not fou then ... end
    # 5854: end (for loop)
    # We need to add an 'end' after the for loop end.
    
    # Simpler replacement: replace the FOR line with IF + FOR
    # and find the end of the for loop to add another END?
    # Context based replacement is safer.
    
    # Let's search for the whole block if possible, or key lines.
    
    if fix1_search in content:
        # We need to find where the loop ends. 
        # It's risky to just regex replace without finding the matching end.
        # But looking at code:
        # 5841: for nam in pairs(pq) do
        # ...
        # 5854: end
        # 5855: if GetNumRaidMembers()
        
        # So we can look for the block end sequence
        block_signature = """if not fou then
pq[nam]=nil
Nx.Tim:Sta("QPartyUpdate",1,self,self.PUT)
end
end"""
        
        if block_signature in content:
            # Replace start
            content = content.replace(fix1_search, fix1_replace)
            # Replace end
            content = content.replace(block_signature, block_signature + "\nend")
            print("Fix 1 applied: OP__3 nil check")
        else:
             print("Warning: Fix 1 block signature not found exactly as expected.")
             # Fallback: Just wrap the loop line and hope we can find the end? 
             # No, better to be safe. Let's try to match the lines directly from our debug output.
             # 5854: end
             # 5855: if GetNumRaidMembers()>0 then
             
             sig2 = "end\nif GetNumRaidMembers()>0 then"
             if fix1_search in content and sig2 in content:
                 content = content.replace(fix1_search, fix1_replace)
                 content = content.replace(sig2, "end\nend\nif GetNumRaidMembers()>0 then")
                 print("Fix 1 applied (fallback signature)")
             else:
                 print("Error: Could not apply Fix 1 reliably.")

    else:
        print("Warning: Fix 1 start code not found (already applied?)")

    # Fix 2: InT1 arithmetic error
    # Original:
    # local na2=strbyte(str,i)
    # local na21=na2==0 and "" or strsub(str,i+1,i+na2)
    
    fix2_search = "local na2=strbyte(str,i)"
    fix2_replace = "local na2=strbyte(str,i)\nna2=na2 or 0"
    
    if fix2_search in content:
        content = content.replace(fix2_search, fix2_replace)
        print("Fix 2 applied: InT1 na2 nil check")
    else:
        print("Warning: Fix 2 code not found.")
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("File saved.")

except Exception as e:
    print(f"Error: {e}")
