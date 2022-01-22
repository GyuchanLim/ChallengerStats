"""
Created on Tue Jan 18 20:39:27 2022

@author: Gyuchan

Which position has the biggest impact at winning the game? (Statistics wise) 
and more specifically, which champion from those positions are shown to be stronger? 

This product will give statistics of the list of challengers given their champion pool base and their position. 
These will just be done by simple api commands using python. 
Further on the development process, if this project is successful, I want to create a match-up analyzer for 
challenger queues providing stats for different match-ups.
"""

from riotwatcher import LolWatcher, ApiError

def getAPI_Key():
    f = open("C:/Users/Gyuchan/Documents/api_key.txt","r")
    return f.read()

def getChallengerPlayersPuuid(server):
    puuid = []
    for player in lol_watcher.league.challenger_by_queue(server, 'RANKED_SOLO_5x5')['entries']:
        puuid.append(lol_watcher.summoner.by_name(server,player['summonerName'])['puuid'])
    return puuid

def getMatchIDFromPuuid(server, puuid):
    matches = []
    for entry in puuid:
        matches+=lol_watcher.match.matchlist_by_puuid('ASIA', entry,0,4,420)
    return list(dict.fromkeys(matches))
    
def getMatchMetaData_ID(server, matchID):
    match = lol_watcher.match.by_id(server, matchID)
    return match['metadata'], match['info']

def challengerLaneStats(match, role):
    laneStatistics = [match]
    teamCount = 0; 
    metaData, info = getMatchMetaData_ID('ASIA', match)
    for participant in info['participants']:
        if participant['teamPosition'] == role:
            laneStatistics.append([participant['championName'],participant['win']])
            teamCount+=1
    return laneStatistics

def championWinLose(champList):
    played = {}
    won = {}
    winRate = []
    for champ in champList:
        if champ[0] not in played:
            played.update({champ[0]:1})
            if champ[1] == True:
                won.update({champ[0]:1})
            else:
                won.update({champ[0]:0})
        else:
            played[champ[0]]+=1
            if champ[1] == True:
                won[champ[0]]+=1
    for item in played:
        winRate.append([item, f'{won[item]/played[item]*100:.1f}'])
    return winRate
    

if __name__=="__main__":
    lol_watcher = LolWatcher(getAPI_Key())
    response = input("Challenger queue or personal stats?\n")
    if response.lower() == 'challenger queue':
        
        role = input("Which role would you like to compare?\nTOP, JUNGLE, MIDDLE, BOTTOM, UTILITY\n")
        server = input("What server is would you like to search?\nBR1, EUN1, EUW1, JP1, Kr, LA1, LA2, NA1, OC1, RU, TR1\n")
        
        challengerPuuid = getChallengerPlayersPuuid(server)
        print("ChallengerPuuid retrieval Successful")
        
        matches = getMatchIDFromPuuid(server, challengerPuuid)
        print("playerMatchID retrieval Successful")
        print(len(matches))
        
        championToAnalyze=[]
        for match in matches:
            championMatchUp = challengerLaneStats(match, role.upper())
            championToAnalyze.append(championMatchUp[1])
            championToAnalyze.append(championMatchUp[2])
        #print(championToAnalyze)
        print(championWinLose(championToAnalyze))
        
        # for puid in metaData['participants']:
        #     print(lol_watcher.summoner.by_puuid('oc1', puid))
            
        # info = lol_watcher.match.by_id('AMERICAS', 'OC1_503778638')['info']
        # for participant in info['participants']:
        #     print(participant['championId'])
        #     print(participant['championName'])
        #     print(participant['teamPosition'], participant['individualPosition'])
    elif response.lower() == 'personal stats':
        found = False
        server = input("What server is your account located in?\nBR1, EUN1, EUW1, JP1, Kr, LA1, LA2, NA1, OC1, RU, TR1\n")
        while(not found):
            summonerName = input("What is your summoner name?\n")
            try:
                response = lol_watcher.summoner.by_name(server, summonerName)
                found = True
            except ApiError as err:
                if err.response.status_code == 404:
                    print("Summoner with that name in %s not found.\n(Name is case sensitive)"%server, end="")
        print(response)
    else:
        info = lol_watcher.match.by_id('AMERICAS', 'OC1_504263587')['info']['participants']
        for a in info:
            print(a['championName'])
        print(info)
        
    
    
    
#for player in challengers['entries']:
#    playerName.append(player['summonerName'])
#    print(lol_watcher.summoner.by_name('oc1',player['summonerName'])['puuid'])
    
#print(playerName)

#print(lol_watcher.match.matchlist_by_puuid('AMERICAS', 'CvwncRD5RvcAzPCglCktYW60qoUQpY2-vCx4He0nKbRx5wFXvmncml3cskf4COihUSGJju999OGS5w',0,4))
#print(lol_watcher.match.by_id('AMERICAS','OC1_503778638')['info']['participants'][1]['role'])

# try:
#     response = lol_watcher.summoner.by_name('oc1', 'moirengu')
# except ApiError as err:
#     if err.response.status_code == 429:
#         print('We should retry in {} seconds.'.format(err.response.headers['Retry-After']))
#         print('this retry-after is handled by default by the RiotWatcher library')
#         print('future requests wait until the retry-after time passes')
#     elif err.response.status_code == 404:
#         print('Summoner with that ridiculous name not found.')
#     else:
#         raise