columns = 40
import random
rows = 10
tiles = [[1] * 12 + [0] * (columns - 24) + [1] * 12]  # 0=air 1=rocks
for row in range(1, rows):
    local = tiles[row - 1][:]
    for i in range(2, columns - 2):
        vecindad = local[i - 1] + local[i] + local[i + 1]
        local[i] = random.choice([0]*100+[1]*(vecindad**3*40+1))
        print(local)
    tiles.append(local)
