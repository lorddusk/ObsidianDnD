---
type: session
world: Faerun
campaign: "Red Hand of Doom"
<%*
let session_number = await tp.user.session_number()
%>
session: <%`${sessionnumber}`%>
game_date: xx xx xx DR
players: []
create_date: {{<% tp.date.now("DD MMMM YYYY") %>}}
---

<%* 
let title = await tp.date.now("DD MMMM YYYY"); 
await tp.file.rename(`Session ${session_number} - ${title}`); 
%>

## Summary:

^summary

## Housekeeping:

## Recap:
![[#^summary]]

## Scenes:

## Loot:

## Log:


