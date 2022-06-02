from typing import List, Tuple
def are_connected(level: List[List[int]], from_point: Tuple[int, int], to_point: Tuple[int, int]) -> bool:
    return search_path(level, from_point, to_point, set())

def search_path(
        level: List[List[int]],
        current_point: Location,
        to_point: Location,
        visited: Set
    ) -> bool:
    if current_point == to_point:
        return True
        
    found = False
    for point in get_neighbours(level, current_point):
        if is_available(visited, level, point):
            visited.add(point)
            current_visited = copy(visited)
            found = search_path(level, point, to_point, current_visited)
        if found:
            break

    return found

def get_neighbours(level : List[List[int]], point: Location) -> List[Location]:
    directions = {
        '0': [1, 0],
        '90': [0, -1],
        '180': [-1, 0],
        '270': [0, 1]
    }
    neighbours = []
    for direction in directions:
        possible_neighbour = (point[0]+ directions[direction][0], point[1]+ directions[direction][1])
        if is_inside_map(level.rows, level.cols, possible_neighbour):
            neighbours.append(possible_neighbour)
    return neighbours

def is_inside_map(rows: int, cols: int, point: Location) -> bool:
    if point[0] < 0 or point[0] >= rows:
        return False
    if point[1] < 0 or point[1] >= cols:
        return False
    return True

def is_available(visited: Set, level: List[List[int]], point: Location) -> bool:
    if point in visited:
        return False
    
    if level[point[0]][point[1]] == 1:
        return False
        
    return True
