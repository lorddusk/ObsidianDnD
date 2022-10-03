---
type: session
tag: Session
world: Faerun
campaign: Red Hand of Doom
sessionNum: <% tp.user.getThisGameNum(tp) %>
game_year: 1491 DR
game_date: []
players: [Guido, Peter, Danny, Rob, Tim]
create_date: {{<% tp.date.now("DD MMMM YYYY") %>}}
---

<%* 
	await tp.file.rename(`Session ${tp.user.getThisGameNum(tp, 1)}`);
%>

## Summary of This Session:

^summary

## Recap of Last Session:
![[#^summary]]

## Housekeeping:

## Notes:

## Loot:
