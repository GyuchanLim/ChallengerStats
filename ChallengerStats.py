"""
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

def getChallengerPlayers():
    return lol_watcher.league.challenger_by_queue('oc1', 'RANKED_SOLO_5x5')


lol_watcher = LolWatcher(getAPI_Key())

playerName = []
challengers = getChallengerPlayers()
for player in challengers['entries']:
    playerName.append(player['summonerName'])
    print(lol_watcher.summoner.by_name('oc1',player['summonerName'])['puuid'])
print(playerName)

print(lol_watcher.match.matchlist_by_puuid('AMERICAS', 'CvwncRD5RvcAzPCglCktYW60qoUQpY2-vCx4He0nKbRx5wFXvmncml3cskf4COihUSGJju999OGS5w',0,4))
print(lol_watcher.match.by_id('AMERICAS','OC1_503778638'))

try:
    response = lol_watcher.summoner.by_name('oc1', 'moirengu')
except ApiError as err:
    if err.response.status_code == 429:
        print('We should retry in {} seconds.'.format(err.response.headers['Retry-After']))
        print('this retry-after is handled by default by the RiotWatcher library')
        print('future requests wait until the retry-after time passes')
    elif err.response.status_code == 404:
        print('Summoner with that ridiculous name not found.')
    else:
        raise