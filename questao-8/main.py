def selection_sort(players):
    n = len(players)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if players[j]['score'] < players[min_index]['score']:
                min_index = j
        players[i], players[min_index] = players[min_index], players[i]

players = [
    {'name': 'Jogador 1', 'score': 50},
    {'name': 'Jogador 2', 'score': 20},
    {'name': 'Jogador 3', 'score': 30},
    {'name': 'Jogador 4', 'score': 40}
]

selection_sort(players)
print(players)
