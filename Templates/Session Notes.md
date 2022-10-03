---
type: session
tag: Session
world: Faerun
campaign: Red Hand of Doom
sessionNum: <% tp.user.getSessionNumber(tp) %>
game_year: 1491 DR
game_date: []
players: [Guido, Peter, Danny, Rob, Tim]
create_date: {{<% tp.date.now("DD MMMM YYYY") %>}}
---

<%* 
	await tp.file.rename(`Session ${tp.user.getSessionNumber(tp)}`);
	await tp.file.create_new(tp.file.find_tfile("Rolls"), false, "Red Hand of Doom/Session Notes/Rolls");
%>

## Summary of This Session:

^summary

## Recap of Last Session:
![[Red Hand of Doom/Session Notes/Session <%tp.user.getSessionNumber(tp, -1)%>#^summary]]

## Housekeeping:

## Notes:

## Loot:
