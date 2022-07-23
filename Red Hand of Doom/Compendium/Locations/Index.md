```dataview
TABLE WITHOUT ID file.name as Name, Description from "Red Hand of Doom/Compendium/Locations"
WHERE contains(type, "location")
SORT file.name asc
```