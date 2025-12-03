# Simple dictionary
alien_0 = {'color':'green', 'points': 5}


# The simpliest dictionary
alien_1 = {}
alien_1 = {'color':'yellow'}

# Accessing values in dictionary
print(alien_1['color'])
#########   print(alien_1['points'])

# Empty dictionary
alien_2 = {}

# Modifying values in a dictionary 
alien_2 = {'color': 'yellow'}
alien_2['color'] = 'blue'

# Adding new key-value pairs
alien_2['x_position'] = 0
alien_2['y_position'] = 25

print(alien_2)

"""

covenant_grunts = {
 "color": "orange",
 "height": "small",
 "weapon": "plasma-gun",
 "hit-points": 6,
 "health": 3,
 "points": 1
   }

covenant_elites = {
 "color": "blue",
 "height": "big",
 "weapon": "plasma-sword",
 "hit-points": 6,
 "health": 6,
 "points": 3

}

covenant_jackal = {
 "color": "green",
 "height": "medium",
 "weapon": "plasma-sword",
 "hit-points": 7,
 "health": 3,
 "points": 2

}

for key, value in covenant_grunts.items():
    print(key, value)

# NESTING

# Estudiar - Listas de diccionarios    
# Estudiar - Listas en diccionarios  
# Estudiar - Diccionario de diccionarios  


# LISTAS DE DICCIONARIOS
covenants = [
covenant_grunts,
covenant_elites,
covenant_jackal
]

for aux in covenants:
    print("\n Covenant: ", aux)
    for key, value in aux.items():
        print(key, value)

"""


# LISTAS EN DICCIONARIOS


students = {
    "pablo": ["cars", "progamar en  python", "hacer tareas"],
    "gerardo-pelon": ["motos","programar en arduino","no le gusta hacer tareas"],
    "gerardo-ame": ["America"]
}
print(students["pablo"])


# DICCIONARIO DE DICCIONARIOS
sensors = {

    "temperature": {
          "id": "temp_1",
          "value":20
},

 "humidity": {
     "id": "hum_1",
     "location": "classroom_a2",
     "value": 60,
      
 }

}


# Imprimir el valor de la temperatura
print("Temperature")
print(sensor["humidity"]["id"])

# INVESTIGAR EL METODO GET