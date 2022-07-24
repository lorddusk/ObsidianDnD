---
type: npc
name: unknown
location: unknown
desc: tbd
tags: NPC
---
<%* 
	let title = tp.file.title 
	if (title.startsWith("Untitled")) { 
		title = await tp.system.prompt("NPC Name?"); 
		await tp.file.rename(`${title}`); 
	} 
%>
# <%* tR += `${title}` %> 
___ 
## References: - 
--- 
creation date:: [[<%tp.file.creation_date("YYYY-MM-DD")%>]] <%tp.file.creation_date("HH:mm")%>