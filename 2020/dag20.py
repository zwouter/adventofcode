tiles = open("data20").read().split("\n\n")

tile_ids = {tile.split(":\n")[1]: tile.split(":\n")[0] for tile in tiles}

tile_permutations = {tile.split(":\n")[1]: [(t[0], ) for t in [tile.split(":\n")[1].split("\n")]] for tile in tiles}

print(tile_ids)

