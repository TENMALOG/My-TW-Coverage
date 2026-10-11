--[[
Turn evidence markers 〔id；id〕 written in the manuscripts into Pandoc citations.
The marker → [{key, locator}] map is produced by scripts/build_bib.py
(data/aerospace-defense/ref-map.json). Unknown ids abort the render so that
no unsupported marker can reach the published page.
Range markers such as R01–R03 expand to every id in the range.
]]

local refmap = nil

local function load_map()
  if refmap then return refmap end
  local dir = pandoc.path.directory(PANDOC_SCRIPT_FILE)
  local path = pandoc.path.join({dir, '..', 'data', 'aerospace-defense', 'ref-map.json'})
  local f = assert(io.open(path, 'r'), 'cannot open ' .. path)
  refmap = pandoc.json.decode(f:read('a'))
  f:close()
  return refmap
end

local function expand(id)
  local a, b = id:match('^R(%d+)–R(%d+)$')
  if a then
    local out = {}
    for i = tonumber(a), tonumber(b) do out[#out + 1] = string.format('R%02d', i) end
    return out
  end
  return {id}
end

local function citations_for(group)
  local map = load_map()
  local cites, seen = {}, {}
  for raw in (group .. '；'):gmatch('(.-)；') do
    for part in (raw .. '、'):gmatch('(.-)、') do
      local id = part:gsub('^%s+', ''):gsub('%s+$', '')
      if id ~= '' then
        for _, one in ipairs(expand(id)) do
          local refs = map[one]
          if refs == nil then error('refs.lua: unknown evidence marker 〔' .. one .. '〕') end
          for _, r in ipairs(refs) do
            local sig = r.key .. '|' .. tostring(r.locator)
            if not seen[sig] then
              seen[sig] = true
              local c = pandoc.Citation(r.key, 'NormalCitation')
              if r.locator ~= nil and r.locator ~= pandoc.json.null then
                c.suffix = pandoc.Inlines({pandoc.Str(', ' .. r.locator)})
              end
              cites[#cites + 1] = c
            end
          end
        end
      end
    end
  end
  return cites
end

function Str(el)
  local text = el.text
  if not text:find('〔', 1, true) then return nil end
  local out = pandoc.Inlines({})
  local pos = 1
  while true do
    local s, e, group = text:find('〔(.-)〕', pos)
    if not s then break end
    if s > pos then out:insert(pandoc.Str(text:sub(pos, s - 1))) end
    local cites = citations_for(group)
    out:insert(pandoc.Cite({pandoc.Str('〔' .. group .. '〕')}, cites))
    pos = e + 1
  end
  if pos <= #text then out:insert(pandoc.Str(text:sub(pos))) end
  return out
end
