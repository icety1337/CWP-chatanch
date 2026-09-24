from checkmate import checkmate
def main():
    board = """\
R...
.K..
..P.
....\
"""
    print("=== Board ===")
    print(board)
    checkmate(board)

main()