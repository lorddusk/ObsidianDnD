---
type: npc
tags:
  -
---
<%* 
let title = tp.file.title 
if (title.startsWith("Untitled")) { 
	title = await tp.system.prompt("NPC Name?"); 
	await tp.file.rename(`${title}`); 
} 
%>