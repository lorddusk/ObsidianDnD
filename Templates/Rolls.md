<%*
let title = tp.file.title 
	if (title.startsWith("Untitled")) { 
		title = await tp.system.prompt("Session Number?");
		if (title.length == 1){
			await tp.file.rename(`$Rolls 00{title}`); 
		}
		if (title.length == 2){
			await tp.file.rename(`$Rolls 0{title}`); 
		}
		if (title.length > 2){
			await tp.file.rename(`$Rolls {title}`); 
		}
	} 
%>
# <%* tR += `${title}` %> 

###### Rolls
| Id. | What           | Dice | Roll | Extra | Adv. | Dis. | Note                             |
| --- | -------------- | ---- | ---- | ----- | ---- | ---- | -------------------------------- |