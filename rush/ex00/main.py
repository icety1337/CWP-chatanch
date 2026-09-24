from checkmate import checkmate


def main():
    # แต่ละตัวแทนตัวหมาก K = king R = rook[หอคอย] P = pawn[ตัวกระจอก]
    board_text = """\
R...
.K..
..P.
....\
"""
    print("=== Board ===")
    print(board_text)
    checkmate(board_text)


main()
