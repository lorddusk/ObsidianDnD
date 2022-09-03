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

```ad-ooc
collapse:closed
```