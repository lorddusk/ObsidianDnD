---
type: session
world: Faerun
campaign: "Red Hand of Doom"
session: x
game_date: xx xx xx DR
characters: []
create_date: {{<% tp.date.now("DD MMMM YYYY") %>}}
mod_date: <% tp.file.last_modified_date("dddd Do MMMM YYYY HH:mm:ss") %>
---

<%* 
let title = await tp.date.now("DD MMMM YYYY"); 
await tp.file.rename(`Session xx - ${title}`); 
%>

## Summary:

^summary
## Housekeeping:
## Recap:
![[#^summary]]
## Scenes:
## Loot:
## Log:


