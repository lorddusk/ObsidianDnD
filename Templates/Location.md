---
type: location
tags:
  -
---
<%* 
let title = tp.file.title 
if (title.startsWith("Untitled")) { 
	title = await tp.system.prompt("Location Name?"); 
	await tp.file.rename(`${title}`); 
} 
%>