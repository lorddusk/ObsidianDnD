```dataview
TABLE WITHOUT ID file.link as Name, location as Location, desc as Description from "Red Hand of Doom/Compendium/Groups"
WHERE contains(type, "group")
SORT file.name asc
```
