---
type: character
tags:
  -
---
<%* 
let title = tp.file.title
if (title.startsWith("Untitled")) { 
	title = await tp.system.prompt("Character Name?"); 
	await tp.file.rename(`${title}`); 
} 
%>