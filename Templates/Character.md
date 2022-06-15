<%* 
	let title = tp.file.title 
	if (title.startsWith("Untitled")) { 
		title = await tp.system.prompt("Title"); 
		await tp.file.rename(`${title}`); 
	} 
	tR += "---" 
%>
--- 
type: character
tags: Note <%tp.file.creation_date("YYYY")%>
---
# <%* tR += `${title}` %> 
<% tp.file.cursor() %> 
___ 
## References: - 
--- creation date:: [[<%tp.file.creation_date("YYYY-MM-DD")%>]] <%tp.file.creation_date("HH:mm")%>