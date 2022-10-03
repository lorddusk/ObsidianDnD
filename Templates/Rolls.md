<%*
let title = tp.file.title 
	if (title.startsWith("Untitled")) { 
		title = await tp.system.prompt("Session Number?");
		if (title.length == 1){
			await tp.file.rename(`Rolls S00${title}`); 
		}
		if (title.length == 2){
			await tp.file.rename(`Rolls S0${title}`); 
		}
		if (title.length > 2){
			await tp.file.rename(`Rolls S${title}`); 
		}
	} 
%>

###### Rolls
| Id. | What           | Dice | Roll | Extra | Adv. | Dis. | Note                             |
| --- | -------------- | ---- | ---- | ----- | ---- | ---- | -------------------------------- |