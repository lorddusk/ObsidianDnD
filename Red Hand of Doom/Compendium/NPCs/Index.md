```dataview
TABLE WITHOUT ID file.link as Name, location as Location, desc as Description from "Red Hand of Doom/Compendium/NPCs"
WHERE contains(type, "npc")
SORT file.name asc
```