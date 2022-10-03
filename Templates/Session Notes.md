---
type: session
tag: Session
world: Faerun
campaign: "Red Hand of Doom"
sessionNum: <% tp.user.getThisGameNum(tp) %>
game_year: 1491 DR
game_date: []
players: [Guido, Peter, Danny, Rob, Tim]
create_date: {{<% tp.date.now("DD MMMM YYYY") %>}}
---

<%* 
	let title = tp.file.title 
	if (title.startsWith("Untitled")) { 
		title = await tp.system.prompt("Session Number?");
		if (title.length == 1) {
			await tp.file.rename(`Session 00${title}`); 
		}
		else if (title.length == 2) {
			await tp.file.rename(`Session 0${title}`); 
		}
		else {
			await tp.file.rename(`Session ${title}`); 
		}
	} 
%>

## Summary of This Session:

^summary

## Recap of Last Session:
![[#^summary]]

## Housekeeping:

## Notes:

## Loot:
