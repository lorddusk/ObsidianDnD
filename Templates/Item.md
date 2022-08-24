---
type: item
tags: Item
---
<%* 
	let title = tp.file.title 
	if (title.startsWith("Untitled")) { 
		title = await tp.system.prompt("Item Name?"); 
		await tp.file.rename(`${title}`); 
	} 
%>
# <%* tR += `${title}` %> 

```ad-ooc
collapse:closed
```