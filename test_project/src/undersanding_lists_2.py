"""
   Slicing a list
"""
players = ['charles', 'martina', 'floreces', 'eli']
print("Lista original", players)
print("Slicing", players[0:3]) # ->  ['charles', 'martina', 'floreces']


print("Slice: ", players [1:4])
print("Slice: ", players [:4])
print("Slice: ", players [2:])
print("Slice: ", players [-2:])
print("Slice: ", players [-3:])

# Slicing en un for

players = ['charles', 'martina', 'floreces', 'eli']
print("Aqui se presentan los primeros 3 jugadores del equipo")
for player in players[0:3]:
    print(player.title())

"""
 ## Copiando una lista
 # players = ['charles', 'martina', 'floreces', 'eli']
 # player_2 = players ->ERROR asi no se copia una lista

 players_2 = players[:]
 players_2 = list(players)
 players_3 = players.copy()
"""

cars = ["bwm","toyota","volkswagen","porche"]
print(cars)
cars[0]="bmw"
cars[3]="porsche"
print(cars)ñ