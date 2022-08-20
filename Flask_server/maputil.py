import random as rd
import mathlib as mt
from .database import Map
from . import database


global size
size = 46656


def safe(pos:int):
    max = size**2
    if pos > 0 and pos < max:
        return True
    return False

def safe_coords(pos:str):
    pos_int = int(pos, 36)
    return safe(pos_int)

def pos_up(pos):
    pos_int = int(pos,36)
    up = pos_int + size
    if safe(up) == True:
        return mt.to360(up)
    return False

def pos_down(pos):
    pos_int = int(pos, 36)
    down = pos_int - size
    if safe(down) == True:
        return mt.to360(down)
    return False

def pos_left(pos):
    pos_int = int(pos, 36)
    left = pos_int - 1
    if safe(left) == True:
        return mt.to360(left)
    return False

def pos_right(pos):
    pos_int = int(pos, 36)
    right = pos_int + 1
    if safe(right) == True:
        return mt.to360(right)
    return False

def check_sides(pos:str):
    """
    ____________    If the image on the right is the grid of the map,
    |___|__|___|     this function checks if the position of the player
    |___|__|___|     is at the bottom, the top, then left or right; if 
    |___|__|___|     it's not, it returns False.
    """
    pos_int = int(pos, 36)
    if pos_int < size:
        return True
    if pos_int > (size - 1) * size:
        return True
    
    sides = [0, size - 1]
    for side in sides:
        while side < size and side <= pos_int:
            if pos_int == side:
                return True
            side += size
    return False

def info_chunk(pos):
    pos_int = int(pos, 36)

    #Controll
    if safe(pos_int) is not True:
        return "404"
    #
    query = Map.query.get(id = pos)

    if query:
        id = query.id
        special = query.special
        tile_id = query.tile_id

        return id, special, tile_id

    else:
        generate_chunk(pos, allow_multiple = True)

def is_real_chunk(pos):
    if Map.query.get(id = pos):
        return True
    return False


def generate_chunk(pos, allow_multiple = False):
    pos_int = int(pos, 36)
    chunks = [pos_up(pos), pos_right(pos), pos_down(pos), pos_left(pos)]
    memory = []
    special = 0.05
    tiles = []
    weight = []
    
    n = 4

    #create chunk percentage
    for a in range(n):
        tiles.append(a)
        weight.append(round(1/n, 3))    

    for chunk in chunks:
        if is_real_chunk(chunk) == True:
            id, s, tile_id = info_chunk(chunk)
            if s is False:
                memory.append(tile_id)
                memory = list(dict.fromkeys(memory))
            else:
                special = special **2

    if memory != []:
        for tile in memory:
            weight[tile - 1] = weight[tile - 1] **2
    #Decides if is a special chunk and what type of chunk is
    special = rd.choice([True, False], [special, 1 - special])
    if special == False:
        tile = rd.choices(tiles, weights=weight)
    if special == True:
        tile = rd.randrange(2)

    #Register the chunk

    new_chunk = Map(id = pos, special = special, tile_id = tile)
    database.session.add(new_chunk)
    database.session.commit()
    
    return new_chunk