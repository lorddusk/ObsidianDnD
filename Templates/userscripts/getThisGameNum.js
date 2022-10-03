function getSessionNumber(tp, add = 0){
    let folderName = tp.file.folder(false);
    let numOfGames = 0;
    app.plugins.plugins.dataview.api.pages(`"Red Hand of Doom/${folderName}"`)
    .forEach(page => {
        if(page.type === 'session'){
            if(page.campaign === "Red Hand of Doom"){
                numOfGames += 1;
            }
        }
    });
    
    numOfGames = JSON.stringify(numOfGames+=add);
    while(numOfGames.length < 3){
        numOfGames = "0"+numOfGames;
    }
    return numOfGames;
}

module.exports = getSessionNumber;