from django.shortcuts import render
import requests

def index(request):

    url = 'https://br.api.riotgames.com/val/ranked/v1/leaderboards/by-act/SUA API KEY?size=200&startIndex=0&api_key= API KEY RIOT'

    data_full = requests.get(url).json()

    data_players = []

    for player in data_full['players']:
        if 'gameName' in player:
            data = {
                'nickname': player['gameName'],
                'rank': player['leaderboardRank'],
                'points': player['rankedRating'],
                'wins': player['numberOfWins']
            }
            data_players.append(data)
        else:
            data = {
                'nickname': 'Secreto',
                'rank': player['leaderboardRank'],
                'points': player['rankedRating'],
                'wins': player['numberOfWins']
            }
            data_players.append(data)

    context = {'data_players': data_players}

    return render(request, 'ranking/index.html', context)
