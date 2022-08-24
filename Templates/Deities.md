---
type: deity
tags: Deity
pantheon: XX
domains: [XX]
---
<%* 
	let title = tp.file.title 
	if (title.startsWith("Untitled")) { 
		title = await tp.system.prompt("Deity Name?"); 
		await tp.file.rename(`${title}`); 
	} 
%>
# <%* tR += `${title}` %> 

###### Symbol:


```ad-ooc
collapse:closed
```