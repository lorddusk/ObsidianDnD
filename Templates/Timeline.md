---
tags: [timeline, campaign]
---
<%* 
	let title = tp.file.title 
	if (title.startsWith("Untitled")) { 
		title = await tp.system.prompt("Timeline title?"); 
		await tp.file.rename(`${title}`); 
	} 
%> 

<span 
	  class='ob-timelines' 
	  data-date='2000-10-10-00' 
	  data-title='<%* tR += `${title}` %>' 
	  data-class='orange' 
	  data-type='range' 
	  data-end='2000-10-20-00'> 
	INSERT TIMELINE TEXT HERE
'<%* tR += `</span>` %>'