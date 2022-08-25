# Characters Overview

```dataview
TABLE WITHOUT ID player as Player, file.link as Name, surname as Surname, desc as Description, race as Race, class as Class from "Red Hand of Doom/Compendium/Characters"
WHERE contains(type, "character")
SORT file.name asc
```
