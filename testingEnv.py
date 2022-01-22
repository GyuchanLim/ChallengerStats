# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 00:21:10 2022

TESTING ENVIRONMENT

@author: Gyuchan
"""
    if server.lower() in ['br1', 'la1', 'la2', 'na1', 'oc1']:
        region = 'AMERICAS'
    elif server.lower() in ['eun1', 'euw2', 'ru', 'tr1']:
        region = "EUROPE"
    else:
        region = "ASIA"
server = 'A'
testingList = ['a','b','c','d']
if server.lower() in testingList:
    print("YES")
else:
    print("NO")
# champList = [['Fiora', False], 
# ['Akali', True], 
# ['Kennen', False], 
# ['Fiora', True], 
# ['Irelia', True], 
# ['Karma', False], 
# ['Gwen', True], 
# ['Yone', False], 
# ['Viktor', False], 
# ['Fiora', True], 
# ['Fiora', True], 
# ['Shen', False], 
# ['Akali', True], 
# ['Riven', False], 
# ['Urgot', False], 
# ['Rumble', True], 
# ['Yone', True],
# ['Gwen', False], 
# ['Vayne', False],
# ['Jax', True], 
# ['Urgot', False], 
# ['Cassiopeia', True], 
# ['Akali', False],
# ['Fiora', True], 
# ['Urgot', False],
# ['Yone', True], 
# ['Singed', True],
# ['Jax', False], 
# ['Tryndamere', False],
# ['Graves', True], 
# ['MonkeyKing', True],
# ['Graves', False],
# ['Yorick', False], 
# ['Aatrox', True],
# ['Shen', True],
# ['Camille', False],
# ['Mordekaiser', False],
# ['Irelia', True],
# ['Camille', True],
# ['Riven', False],
# ['Graves', False], 
# ['Vayne', True], 
# ['Akali', False], 
# ['Riven', True],
# ['Camille', False],
# ['Fiora', True],
# ['Irelia', False], 
# ['Fiora', True], 
# ['Yone', True], 
# ['Jax', False],
# ['Jax', False],
# ['Camille', True],
# ['Vayne', False], 
# ['Fiora', True], 
# ['Urgot', True],
# ['Fiora', False],
# ['Akali', False],
# ['Jayce', True], 
# ['Jax', True],
# ['Camille', False],
# ['Akali', False],
# ['Akshan', True],
# ['Riven', True],
# ['Fiora', False], 
# ['Jax', False],
# ['Vladimir', True],
# ['Sion', False],
# ['Irelia', True],
# ['Urgot', True],
# ['Viktor', False],
# ['Singed', True],
# ['Graves', False],
# ['Riven', False], 
# ['Vladimir', True], 
# ['Irelia', False], 
# ['Vayne', True]]


# played = {}
# won = {}
# for champ in champList:
#     if champ[0] not in played:
#         played.update({champ[0]:1})
#         if champ[1] == True:
#             won.update({champ[0]:1})
#         else:
#             won.update({champ[0]:0})
#     else:
#         played[champ[0]]+=1
#         if champ[1] == True:
#             won[champ[0]]+=1
# for item in played:
#     print(item, f'{won[item]/played[item]*100:.1f}')
# #print(played, won)