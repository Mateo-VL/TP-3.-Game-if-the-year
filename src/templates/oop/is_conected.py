from typing import List, Set, Tuple

from copy import copy
Location = Tuple[int, int]

def is_inside_map(rows: int, columns: int, point: Location) -> bool:
    if point[0] < 0 or point[0] >= rows:
        return False
    if point[1] < 0 or point[1] >= columns:
        return False
    return True

def get_neighbours(level: List[List[object]], point: Location) -> List[Location]:
    directions = {
            '0': [1, 0],
            '90': [0, -1],
            '180': [-1, 0],
            '270': [0, 1]
            }
    neighbours = []
    for direction in directions:
        possible_neighbour = (point[0] + directions[direction][0], point[1] + directions[direction][1])
        if is_inside_map(level.rows, level.columns, possible_neighbour):
            neighbours.append(possible_neighbour)
    return neighbours

def search_path(level, initial: Location, end: Location, visited: Set) -> bool:
    if initial == end:
        return True
    found = False
    for point in get_neighbours(level, initial):
        if is_available(level, point, visited):
            visited.add(point)
            current_visited = copy(visited)
            found = search_path(level, point, end, current_visited)
        if found:
            break
    return found


def is_available(level, point: Location, visited: Set) -> bool:
    if point in visited:
        return False
    if not level.is_walkable(point):
        return False
    return True