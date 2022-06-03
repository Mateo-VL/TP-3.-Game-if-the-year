from __future__ import annotations
#from arrancando_el_tp import DUNGEON
import src.templates.oop.player as player
import src.templates.oop.items as items
import random
from typing import Optional
from typing import List, Tuple, Set
from copy import copy


Location = Tuple[int, int]

class Tile:
    """Tile(char: str, walkable: bool=True)

    A Tile is the object used to represent the type of the dungeon floor.

    Arguments

    char (str) -- string of length 1 that is rendered when rendering a map.
    walkable (bool) -- states if the tile is walkable or not.
    """
    def __init__(self, char: str, walkable: bool = True):
        self.walkable = walkable
        self.face = char

    def is_walkable(self) -> bool:
        """Returns True if the tile is walkable, False otherwise."""
        return self.walkable


AIR = Tile(' ')
WALL = Tile('▓', False)
STAIR_UP = Tile('<')
STAIR_DOWN = Tile('>')


class Level:
    """Level(rows: int, columns: int) -> Level

    Arguments

    rows (int) -- is the number of rows for the level.
    columns (int) -- is the number of columns for the level.

    Returns an instance of a level.
    """
    def __init__(self, rows: int, columns: int):
        """Initializes a dungeon level class. See class documentation."""
        tiles = [[1] * 12 + [0] * (columns - 24) + [1] * 12]  # 0=air 1=rocks
        for row in range(1, rows):
            local = tiles[row - 1][:]
            for i in range(2, columns - 2):
                vecindad = local[i - 1] + local[i] + local[i + 1]
                local[i] = random.choice([0]*100+[1]*(vecindad**3*40+1))
            tiles.append(local)

        for row in range(0, rows):
            for col in range(0, columns):
                tiles[row][col] = AIR if tiles[row][col] == 0 else WALL

        self.tiles = tiles
        self.rows, self.columns = rows, columns
        self.items = {}

    def find_free_tile(self) -> Location:
        """Randomly searches for a free location inside the level's map.
        This method might never end.
        """
        i, j = random.randint(0, self.rows - 1), random.randint(0, self.columns - 1)
        while self.tiles[i][j] != AIR:
            i, j = random.randint(0, self.rows - 1), random.randint(0, self.columns - 1)
        return (j, i)

    def get_random_location(self) -> Location:
        """Compute and return a random location in the map."""
        return random.randint(0, self.columns - 1), random.randint(0, self.rows - 1)

    def add_stair_up(self, location: Optional[Location] = None):
        """Add an ascending stair tile to a given or random location in the map."""
        if location is not None:
            j, i = location
        else:
            i = random.randint(0, self.rows - 1)
            j = random.randint(0, self.columns - 1)
        self.tiles[i][j] = STAIR_UP

    def add_stair_down(self, location: Optional[Location] = None):
        """Add a descending stair tile to a give or random location in the map."""
        if location is not None:
            j, i = location
        else:
            i = random.randint(0, self.rows - 1)
            j = random.randint(0, self.columns - 1)
        self.tiles[i][j] = STAIR_DOWN

    def add_item(self, item: items.Item, location: Optional[Location] = None):
        """Add an item to a given location in the map. If no location is given, one free space is randomly searched.
        This method might never if the probability of finding a free space is low.
        """
        if location is None:
            j, i = self.find_free_tile()
        else:
            j, i = location
        items = self.items.get((i, j), [])
        items.append(item)
        self.items[(i, j)] = items

    def render(self, player: player.Player, gnome: player.Player, level):
        """Draw the map onto the terminal, including player and items. Player must have a loc() method, returning its
        location, and a face attribute. All items in the map must have a face attribute which is going to be shown. If
        there are multiple items in one location, only one will be rendered.
        """
        print("-" + "-" * len(self.tiles[0]) + "-")
        print(f" Level:", (level+1), "   Turns:", "   ", "       ", player.show_items(), "\n",  "HP:", player.hp,"    ", "Gnome HP:" , gnome.hp)
        
        print("-" + "-" * len(self.tiles[0]) + "-")
        for i, row in enumerate(self.tiles):
            print("|", end="")
            for j, cell in enumerate(row):
                if (j, i) == player.loc():     #hice lo = con gnome
                    print(player.face, end='')
                elif (j, i) == gnome.loc():     
                    print(gnome.face, end='')
                elif (i, j) in self.items:
                    print(self.items[(i, j)][0].face, end='')
                else:
                    print(cell.face, end='')
            print("|")
        print("-" + "-" * len(self.tiles[0]) + "-")

    def is_walkable(self, location: Location):
        """Check if a player can walk through a given location."""
        j, i = location
        return self.tiles[i % self.rows][j % self.columns].walkable

    def index(self, tile: Tile) -> Location:
        """Get the location of a given tile in the map. If there are multiple tiles of that type, then only one is
        returned.

        Arguments

        tile (Tile) -- one of the known tile types (AIR, WALL, STAIR_DOWN, STAIR_UP)

        Returns the location of that tile type or raises ValueError
        """
        for i in range(self.rows):
            try:
                j = self.tiles[i].index(tile)
                return j, i
            except ValueError:
                pass
        raise ValueError

    def loc(self, xy: Location) -> Tile:
        """Get the tile type at a give location."""
        j, i = xy
        return self.tiles[i][j]

    def get_items(self, xy: Location) -> List[items.Item]:
        """Get a list of all items at a given location. Removes the items from that location."""
        j, i = xy
        if (i, j) in self.items:
            items = self.items[(i, j)]
            del(self.items[(i, j)])
        else:
            items = []
        return items

    def dig(self, xy: Location) -> None:   #cuando rompe pared?
        """Replace a WALL at the given location, by AIR."""
        j, i = xy
        if self.tiles[i][j] is WALL:
            self.tiles[i][j] = AIR

    def is_free(self, xy: Location) -> bool:
        """Check if a given location is free of other entities."""
        # completar   
        #if self.is_walkable(xy) ==True:
            #return True
        #else:
            #return False

        raise NotImplementedError

    def are_connected(self,level: Level, initial: Location, end: Location) -> bool:
        return search_path(level, initial, end, set())
        
    def is_inside_map(rows: int, columns: int, point: Location) -> bool:
        if point[0] < 0 or point[0] >= rows:
            return False
        if point[1] < 0 or point[1] >= columns:
            return False
        return True

    def get_neighbours(level: Level, point: Location) -> List[Location]:
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

    def search_path(level : Level, initial: Location, end: Location, visited: Set) -> bool:
        if initial == end:
            return True
        found = False
        for point in get_neighbours(level, initial):
            if is_available(level, point, visited):
                visited.add(point)
                current_visited = copy(visited)
                found = search_path(level, point, end, visited)
            if found:
                break
        return found
    
    
    def is_available(level: Level, point: Location, visited: Set) -> bool:
        if point in visited:
            return False
        if not level.is_walkable(point):
            return False
        return True

    def get_path(self, initial: Location, end: Location) -> bool:
        """Return a sequence of locations between initial location and end location, if it exits."""
        # completar
        #if initial == end:
            #return True
       # elif:
        raise NotImplementedError


    
class Dungeon:
    """Dungeon(rows: int, columns: int, levels: int = 3) -> Dungeon

    Arguments

    rows (int) -- is the number of rows for the dungeon.
    columns (int) -- is the number of columns for the dungeon.
    levels (int) -- is the number of levels for the dungeon (default: 3).

    Returns an instance of a dungeon.
    """
    def __init__(self, rows: int, columns: int, levels: int = 3):
        """Initializes a dungeon class. See class documentation."""
        self.dungeon = [Level(rows, columns) for _ in range(levels)]
        self.rows = rows
        self.columns = columns
        self.level = 0

        self.stairs_up = [level.get_random_location() for level in self.dungeon]
        self.stairs_down = [level.get_random_location() for level in self.dungeon[:-1]]

        for level, loc_up, loc_down in zip(self.dungeon[:-1], self.stairs_up[:-1], self.stairs_down):
            # Ubicar escalera que sube
            level.add_stair_up(loc_up)

            # Ubicar escalera que baja
            level.add_stair_down(loc_down)

        # Ubicar escalera del nivel inferior
        self.dungeon[-1].add_stair_up(self.stairs_up[-1])

    def render(self, player: player.Player, gnome: player.Player, level):
        """Draw current level onto the terminal, including player and items. Player must have a loc() method, returning
        its location, and a face attribute. All items in the map must have a face attribute which is going to be shown.
        If there are multiple items in one location, only one will be rendered.
        """
        self.dungeon[self.level].render(player,gnome, level)

    def find_free_tile(self) -> Location:
        """Randomly searches for a free location inside the level's map.
        This method might never end.
        """
        return self.dungeon[self.level].find_free_tile()

    def is_walkable(self, tile: Tile):
        """Check if a player can walk through a given location. See Level.is_walkable()."""
        return self.dungeon[self.level].is_walkable(tile)

    def add_item(self, item: items.Item, level: Optional[int] = None, xy: Optional[Location] = None):
        """Add an item to a given location in the map of a given or current level. If no location is given, one free
        space is randomly searched. This method might never if the probability of finding a free space is low.
        """
        if level is None:
            level = self.level + 1
        if 0 < level <= len(self.dungeon):
            self.dungeon[level - 1].add_item(item, xy)

    def loc(self, xy: Location) -> Tile:
        """Get the tile type at a give location."""
        return self.dungeon[self.level].loc(xy)

    def index(self, tile: Tile) -> Location:
        """Get the location of a given tile in the map. If there are multiple tiles of that type, then only one is
        returned. See Level.index().
        """
        return self.dungeon[self.level].index(tile)

    def get_items(self, xy: Location) -> List[items.Item]:
        """Get a list of all items at a given location. Removes the items from that location. See Level.get_items()."""
        return self.dungeon[self.level].get_items(xy)

    def dig(self, xy: Location) -> None:
        """Replace a WALL at the given location, by AIR. See Level.dig()."""
        return self.dungeon[self.level].dig(xy)
#completar
    def is_free(self, xy: Location) -> bool:
        """NOT IMPLEMENTED. Check if a given location is free of other entities. See Level.is_free()."""
        return self.dungeon[self.level].is_free(xy)
    
    def get_columns(self) -> int:
        return self.columns
    
    def get_rows(self) -> int:
        return self.rows
