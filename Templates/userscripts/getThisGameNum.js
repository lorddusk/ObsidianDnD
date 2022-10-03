function getThisGameNum(tp){
    let folderName = tp.file.folder(false);
    let numOfGames = app.plugins.plugins.dataview.api
        .pages(`"Red Hand Of Doom/${folderName}"`)
        .where(page => {
            if(page.type === 'session'){
                console.log("Page found");
                if(page.campaign === "Red Hand of Doom"){
                    console.log('SessionNum: ', page.sessionNum);
                    return true;
                }
            }
        }).length
    console.log("Num of Games: ", numOfGames)
    numOfGames = JSON.stringify(numOfGames+1);
    while(numOfGames.length < 3){
        numOfGames = "0"+numOfGames;
    }
    console.log("Num of Games: ", numOfGames)
    return numOfGames;
}

module.exports = getThisGameNum;