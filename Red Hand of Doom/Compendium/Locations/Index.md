```dataview
TABLE WITHOUT ID file.link as Name, desc as Description from "Red Hand of Doom/Compendium/Locations"
WHERE contains(type, "location")
SORT file.name asc
```