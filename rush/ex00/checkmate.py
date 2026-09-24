def checkmate(board_text: str):
    #เช็คว่า king จะโดนอีกฝั่งตีไหม

    # ตัดบรรทัดว่างออก ตัว \n แล้วแปลงแต่ละแถวให้เข้าถึงช่องด้วย index ได้ 
    board_lines = board_text.split('\n')
    board_grid = [list(line) for line in board_lines if line]

    if not board_grid:
        print("Error")
        return

    board_size = len(board_grid)
    expected_row_length = len(board_grid[0])

    # เช็คสี่เหลี่ยมจัตุรัส บนล่างซ้ายขวา
    for board_row in board_grid:
        if len(board_row) != expected_row_length:
            print("Error")
            return
    if board_size != expected_row_length:
        print("Error")
        return

    king_position = None
    for row_index in range(board_size):
        for column_index in range(expected_row_length):
            if board_grid[row_index][column_index] == 'K':
                # เช็คว่าคิงเกิน 1 ป่าว
                if king_position is not None:
                    print("Error")
                    return
                king_position = (row_index, column_index)

    if king_position is None:
        print("Error")
        return

    king_row, king_column = king_position

    orthogonal_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    is_king_in_check = False

    # ไล่จาก king ออกไปในแนวตรงทีละทิศทาง
    # หมากตัวแรกที่พบจะบังหมากทุกตัวที่อยู่ถัดไปในแนวเดียวกัน
    for row_step, column_step in orthogonal_directions:
        square_row, square_column = king_row + row_step, king_column + column_step
        while 0 <= square_row < board_size and 0 <= square_column < expected_row_length:
            piece = board_grid[square_row][square_column]
            if piece in ['P', 'B', 'R', 'Q']:
                if piece in ['R', 'Q']:
                    is_king_in_check = True
                break
            square_row += row_step
            square_column += column_step

    # ตัวแหว่งๆ [bishop] กับควีน โจมตีแนวทแยง ไปได้สุดเลย แต่ไอ้ตัวกระจอกสุด [pawn] โจมตีได้เพียงช่องทแยง
    # ด้านหน้า 1 ช่อง ทิศที่เลขแถวเพิ่มขึ้น
    for row_step, column_step in diagonal_directions:
        square_row, square_column = king_row + row_step, king_column + column_step
        distance_from_king = 1
        while 0 <= square_row < board_size and 0 <= square_column < expected_row_length:
            piece = board_grid[square_row][square_column]
            if piece in ['P', 'B', 'R', 'Q']:
                if piece in ['B', 'Q']:
                    is_king_in_check = True
                elif piece == 'P' and distance_from_king == 1 and row_step == 1:
                    is_king_in_check = True
                break
            square_row += row_step
            square_column += column_step
            distance_from_king += 1

    if is_king_in_check:
        print("Success")
    else:
        print("Fail")

