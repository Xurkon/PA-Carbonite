-- Carbonite-ElvUI Compatibility Module
-- When ElvUI's minimap module is enabled, disable Carbonite's minimap ownership
-- so both can coexist (ElvUI manages Blizzard Minimap, Carbonite uses its own map window)

local function FixConflict()
    -- Check if ElvUI's minimap is enabled
    local elvuiMinimapEnabled = ElvUI and ElvUI[1] and ElvUI[1].private and 
                                 ElvUI[1].private.general and 
                                 ElvUI[1].private.general.minimap and 
                                 ElvUI[1].private.general.minimap.enable

    -- Check if Carbonite is loaded
    local carboniteLoaded = Nx and Nx.Map and Nx.Map.GeM
    local map = carboniteLoaded and Nx.Map:GeM(1)

    if elvuiMinimapEnabled and map then
        -- Disable Carbonite's minimap control
        map.MMO1 = false
        
        -- Rescue the Minimap from Carbonite's window
        -- We parent it to UIParent because ElvUI handles its own anchoring
        if Minimap:GetParent() ~= UIParent then
            Minimap:SetParent(UIParent)
            Minimap:SetFrameStrata("LOW")
            Minimap:SetFrameLevel(10)
        end

        -- Tell ElvUI to refresh its minimap settings if the module is initialized
        local E = ElvUI[1]
        local M = E:GetModule("Minimap")
        if M and M.Initialized then
            -- Re-run ElvUI's minimap setup/update
            if M.UpdateSettings then
                M:UpdateSettings()
            end
            
            -- Ensure it's square for ElvUI
            Minimap:SetMaskTexture("Interface\\ChatFrame\\ChatFrameBackground")
            Minimap:Show()
            
            print("|cFF00FF00Carbonite:|r ElvUI minimap detected. Carbonite minimap ownership disabled.")
            return true -- Success
        end
    end
    return false
end

-- Polling approach to handle async loading of both addons
local totalElapsed = 0
local pollFrame = CreateFrame("Frame")
pollFrame:SetScript("OnUpdate", function(self, elapsed)
    totalElapsed = totalElapsed + elapsed
    if totalElapsed > 0.1 then
        totalElapsed = 0
        if FixConflict() then
            -- Once fixed, we can stop polling
            self:SetScript("OnUpdate", nil)
        end
    end
    
    -- Safety timeout (10 seconds)
    if totalElapsed > 10 then
        self:SetScript("OnUpdate", nil)
    end
end)
