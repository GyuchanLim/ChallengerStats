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

lol_watcher = LolWatcher(getAPI_Key())

my_region = 'oc1'

me = lol_watcher.summoner.by_name(my_region, 'Kangapooh')
print(me)

players = lol_watcher.league.challenger_by_queue('oc1', 'RANKED_SOLO_5x5')
print(players)
#for player in players['entries']:
#    print(player['summonerName'])
#print(lol_watcher.league.challenger_by_queue('oc1','RANKED_SOLO_5x5'))


try:
    response = lol_watcher.summoner.by_name(my_region, 'moirengu')
except ApiError as err:
    if err.response.status_code == 429:
        print('We should retry in {} seconds.'.format(err.response.headers['Retry-After']))
        print('this retry-after is handled by default by the RiotWatcher library')
        print('future requests wait until the retry-after time passes')
    elif err.response.status_code == 404:
        print('Summoner with that ridiculous name not found.')
    else:
        raise