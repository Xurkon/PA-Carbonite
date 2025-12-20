-- Carbonite-GatherMate2 Import Module
-- Adds ability to import GatherMate2 node data into Carbonite

local function ImportGM2Data(sourceDB, targetDB, nodeType)
    if not sourceDB then
        Nx.prt("|cFFFF0000GatherMate2 " .. nodeType .. " database not found!|r")
        return 0
    end
    
    local count = 0
    local target = NxData[targetDB]
    if not target then
        NxData[targetDB] = {}
        target = NxData[targetDB]
    end
    
    -- Iterate through GatherMate2 zones
    for zoneID, nodes in pairs(sourceDB) do
        if type(nodes) == "table" then
            if not target[zoneID] then
                target[zoneID] = {}
            end
            
            -- Import each node
            for coord, nodeID in pairs(nodes) do
                if not target[zoneID][coord] then
                    target[zoneID][coord] = nodeID
                    count = count + 1
                end
            end
        end
    end
    
    return count
end

-- Import GatherMate2 Herbalism locations
function Nx.NXCmdImportGM2Herb()
    local count = ImportGM2Data(GatherMate2HerbDB, "NXHerb", "Herbalism")
    Nx.prt("|cFF00FF00Imported " .. count .. " herb nodes from GatherMate2|r")
end

-- Import GatherMate2 Mining locations  
function Nx.NXCmdImportGM2Mine()
    local count = ImportGM2Data(GatherMate2MineDB, "NXMine", "Mining")
    Nx.prt("|cFF00FF00Imported " .. count .. " mining nodes from GatherMate2|r")
end

-- Register with Carbonite's options system
-- This hooks into the existing Guide Options menu
local function AddGM2MenuEntries()
    -- Find the Guide menu and add our entries after Cartographer imports
    if Nx and Nx.OpD then
        -- Add entries to options table
        -- Note: This may need adjustment based on Carbonite's exact menu structure
        Nx.prt("|cFF00FF00GatherMate2 Import:|r Use /gm2import herb or /gm2import mine")
    end
end

-- Slash commands as fallback
SLASH_GM2IMPORT1 = "/gm2import"
SlashCmdList["GM2IMPORT"] = function(msg)
    msg = string.lower(msg or "")
    if msg == "herb" or msg == "herbs" then
        Nx.NXCmdImportGM2Herb()
    elseif msg == "mine" or msg == "mining" then
        Nx.NXCmdImportGM2Mine()
    else
        Nx.prt("|cFFFFFF00GatherMate2 Import Commands:|r")
        Nx.prt("  /gm2import herb - Import herbalism nodes")
        Nx.prt("  /gm2import mine - Import mining nodes")
    end
end

-- Initialize when Carbonite is ready
local frame = CreateFrame("Frame")
frame:RegisterEvent("PLAYER_LOGIN")
frame:SetScript("OnEvent", function()
    if Nx then
        AddGM2MenuEntries()
    end
end)
