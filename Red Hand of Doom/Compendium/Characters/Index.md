```dataview
TABLE WITHOUT ID file.link as Name, surname as Surname, player as Speler, desc as Description from "Red Hand of Doom/Compendium/Characters"
WHERE contains(type, "character")
SORT file.name asc
```
