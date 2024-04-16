def compute_pond_sizes(land: list[list[int]]) -> list[int]:
    ponds = []
    max_row = len(land)
    max_col = len(land[0])

    def search_water(land, row, col):
        if row >= max_row:
            return
        if col >= max_col:
            search_water(land, row+1, 0)
            return
        if land[row][col] == 0:
            ponds.append(search_adjacent(land, row, col))
            land[row][col] = -1
        search_water(land,row,col+1)
    
    def search_adjacent(land, row, col):
        num_water = 0
        if row >= max_row or col >= max_col or row < 0 or col < 0:
            return num_water
        if land[row][col] == 0:
            num_water += 1
            land[row][col] = -1
            num_water += search_adjacent(land, row, col+1)
            num_water += search_adjacent(land, row+1, col)
            num_water += search_adjacent(land, row-1, col)
            num_water += search_adjacent(land, row, col-1)
            num_water += search_adjacent(land, row+1, col+1)
            num_water += search_adjacent(land, row-1, col-1)
            num_water += search_adjacent(land, row+1, col-1)
            num_water += search_adjacent(land, row-1, col+1)
        return num_water
        
    search_water(land, 0, 0)

    for row in range(max_row):
        for col in range(max_col):
            if land[row][col] == -1:
                land[row][col] = 0

    return ponds