# Items Overview

```dataview
TABLE WITHOUT ID file.name as Name, description as Description, magical as Magical from "Red Hand of Doom/Compendium/Items"
WHERE contains(type, "item")
SORT file.name asc
```
