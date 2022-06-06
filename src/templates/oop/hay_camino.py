from copy import copy
from typing import List, Set, Tuple
import mapping

Location = Tuple[int,int]
# conceptualmente
'''
mapa: List[List[int]] = []

point =  Tuple[int, int]
'''
WALL = mapping.WALL
EMPTY = mapping.AIR
INICIO = mapping.STAIR_UP
FIN = mapping.STAIR_DOWN


DUNGEON = mapping.Dungeon(25,80)


'''
Obs:
La unica función que subre modificaciones en esta implementación es search_path.
Dado que la lógica para obtener vecinos y verificar si un espacio esta disponible
no se modofican.
'''


def are_connected(dungeon: mapping.Dungeon, from_point: Location, to_point: Location) -> bool:
    '''
    Esta funcion devuelve si existe un camino posible entre los puntos
    que se piden.
    Params:
        - mapa: lista de listas represetando una matriz de enteros.
        - from_point: tupla de (row, col) representando un punto en la matriz desde donde partir.
        - to_point: tupla de (row, col) representando un punto en la matriz a donde se quiere ir
    Returns:
        True si es existe el camino, False si no.
    '''
    return search_path(dungeon.dungeon[dungeon.level], from_point, to_point, set())


def search_path(
        level: mapping.Level, 
        current_point: Location, 
        to_point: Location, 
        visited: Set
    ) -> bool:
    '''
    Dado una instancia de un mapa y 2 puntos efectivamente busca si existe el camino.
    Parmas:
    Params:
        - mapa: lista de listas represetando una matriz de enteros.
        - current_point: tupla de (row, col) representando un punto en la matriz desde donde partir.
        - to_point: tupla de (row, col) representando un punto en la matriz a donde se quiere ir
        - visited: es un set de puntos ya visitados.
    Returns:
        True si es existe el camino, False si no.
    
    '''

    found = False
    queue_of_points = get_neighbours(level, current_point)

    while not found and len(queue_of_points) > 0:

        current = queue_of_points.pop(0)
        
        if current in visited: # chequeamos que el espacio no fue recorrido
            continue

        visited.add(current)

        if current == to_point:
            found = True


        for p in get_neighbours(level, current):
            if is_available(visited, level, p):
                queue_of_points.append(p)
        

    
    return found


def get_neighbours(level: mapping.Level, point: Location) -> List[Location]:
    '''
    Dado un mapa y un punto, retorna la lista de puntos en su vecindario.
    Parmas:
        - mapa: lista de listas representando una matrix
        - point: tuple de (row, col) representando un punto dentro del mapa.
    Returns: 
        Lista de points
    '''
    directions = {
        '0': [1, 0],
        '90': [0, -1],
        '180': [-1, 0],
        '270': [0, 1]
    }
    rows = level.rows
    cols = level.columns
    neighbours = []
    for deltas in directions.values():
        possible_neighbour = (point[0]+ deltas[0], point[1]+ deltas[1])
        if is_inside_map(rows, cols, possible_neighbour):
            neighbours.append(possible_neighbour)
    return neighbours


def is_inside_map(num_rows: int, num_cols: int, point: Location) -> bool:
    '''
    Dado un punto y los limites del mapa determinar si el punto es válido.
    Params:
        - num_rows: int representa la cantidad de filas en la matriz
        - num_cols: int representa la cantidad de columnas en la matriz
        - point: tupla (row, col) que representa un punto en la matriz.
    Returns:
        True si esta adentro false si no
    '''
    if point[0] < 0 or point[0] >= num_cols:
        return False
    
    if point[1] < 0 or point[1] >= num_rows:
        return False
    return True


def is_available(visited: Set, level: mapping.Level, point: Location):
    '''
    Dado un punto y un mapa, verficar si la posición esta vacía y es posible utiilizarla o no.
    Paras:
        - visited: set de puntos que ya fueron utilizados.
        - mapa: lista de listas representando una matriz
        - point: Tupla de (row, col) representando el punto en el mapa.
    Returns:
        True si es posible usarlo, False si no.
    '''
    if point in visited:
        return False
    
    if not level.is_walkable(point):
        return False
    return True


