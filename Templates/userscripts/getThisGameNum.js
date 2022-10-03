function getThisGameNum(tp){
    thisCampaign = tp.file.folder(false);
    console.log("Dataview: ", app.plugins.plugins.dataview.api.pages(`"Red Hand of Doom/${thisCampaign}"`));
    let numOfGames = app.plugins.plugins.dataview.api
        .pages(`"Red Hand Of Doom/${thisCampaign}"`)
        .where(page => {
            if(page.type === 'session'){
                if(page.campaign === thisCampaign.replace("/Session Notes", "")){
                    return true;
                }
            }
        }).length
    numOfGames = JSON.stringify(numOfGames+1);
    while(numOfGames.length < 3){
        numOfGames = "0"+numOfGames;
    }
    return numOfGames;
}

module.exports = getThisGameNum;