def checkmate(board: str):

    lines = board.split('\n')
    grid = [list(line) for line in lines if line]
    
    if not grid:
        print("Error")
        return

    rows = len(grid)
    cols = len(grid[0])

    for row in grid:
        if len(row) != cols:
            print("Error")
            return
    if rows != cols:
        print("Error")
        return

    king_pos = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'K':
                if king_pos is not None:
                    print("Error")
                    return
                king_pos = (r, c)
                
    if king_pos is None:
        print("Error")
        return
    kr, kc = king_pos
    
    ortho_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    diag_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    in_check = False

    for dr, dc in ortho_dirs:
        r, c = kr + dr, kc + dc
        while 0 <= r < rows and 0 <= c < cols:
            char = grid[r][c]
            if char in ['P', 'B', 'R', 'Q']:
                if char in ['R', 'Q']:
                    in_check = True
                break
            r += dr
            c += dc

    for dr, dc in diag_dirs:
        r, c = kr + dr, kc + dc
        dist = 1
        while 0 <= r < rows and 0 <= c < cols:
            char = grid[r][c]
            if char in ['P', 'B', 'R', 'Q']:
                if char in ['B', 'Q']:
                    in_check = True
                elif char == 'P' and dist == 1 and dr == 1:
                    in_check = True
                break
            r += dr
            c += dc
            dist += 1

    if in_check:
        print("Success")
    else:
        print("Fail")

