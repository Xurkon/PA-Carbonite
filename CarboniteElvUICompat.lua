-- Carbonite-ElvUI Compatibility Module
-- When ElvUI's minimap module is enabled, disable Carbonite's minimap ownership
-- so both can coexist (ElvUI manages Blizzard Minimap, Carbonite uses its own map window)

local frame = CreateFrame("Frame")
frame:RegisterEvent("PLAYER_ENTERING_WORLD")

local function DisableCarboniteMinimapOwnership()
    -- Check if ElvUI's minimap is enabled
    local elvuiMinimapEnabled = ElvUI and ElvUI[1] and ElvUI[1].private and
                                 ElvUI[1].private.general and
                                 ElvUI[1].private.general.minimap and
                                 ElvUI[1].private.general.minimap.enable

    -- Check if Carbonite is loaded
    local carboniteLoaded = Nx and Nx.Map and Nx.Map.GeM

    if elvuiMinimapEnabled and carboniteLoaded then
        -- Disable Carbonite's minimap ownership
        local success, err = pcall(function()
            local map = Nx.Map:GeM(1)
            if map then
                -- Disable Carbonite's minimap control
                map.MMO1 = false

                -- Restore the Minimap to ElvUI's holder if it exists
                if MMHolder then
                    Minimap:SetParent(MMHolder)
                    Minimap:ClearAllPoints()
                    
                    -- Check ElvUI's reminder position setting
                    local E = ElvUI[1]
                    if E.db and E.db.general and E.db.general.reminder and E.db.general.reminder.position == "LEFT" then
                        Minimap:SetPoint("TOPRIGHT", MMHolder, "TOPRIGHT", -E.Border, -E.Border)
                    else
                        Minimap:SetPoint("TOPLEFT", MMHolder, "TOPLEFT", E.Border or 2, -(E.Border or 2))
                    end
                    
                    -- Restore minimap settings
                    Minimap:SetMaskTexture("Interface\\ChatFrame\\ChatFrameBackground")
                    Minimap:Show()
                    
                    -- Tell ElvUI to update
                    local M = E:GetModule("Minimap")
                    if M and M.UpdateSettings then
                        M:UpdateSettings()
                    end
                end

                print("|cFF00FF00Carbonite:|r ElvUI minimap detected. Carbonite minimap ownership disabled.")
                print("|cFF00FF00Carbonite:|r ElvUI's minimap restored. Carbonite map window still works separately.")
            end
        end)

        if not success then
            print("|cFFFF0000Carbonite-ElvUI Compat:|r Failed: " .. tostring(err))
        end
    end
end

frame:SetScript("OnEvent", function(self, event)
    self:UnregisterEvent(event)
    -- Delay slightly to ensure both addons are fully loaded
    C_Timer.After(0.5, DisableCarboniteMinimapOwnership)
end)

