---
type: character
tags: Party
---
<%* 
	let title = tp.file.title 
	if (title.startsWith("Untitled")) { 
		title = await tp.system.prompt("Character Name?"); 
		await tp.file.rename(`${title}`); 
	} 
%>
# <%* tR += `${title}` %> 

```ad-ooc
collapse:closed
```