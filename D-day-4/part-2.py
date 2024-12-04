import codetiming
import itertools

UNIT_DIAGONAL_VECTORS = itertools.product((-1, 1), repeat=2)

DIAGONAL_PATTERNS = [
    (unit_diagonal, (-unit_diagonal[0], -unit_diagonal[1]))
    for unit_diagonal in UNIT_DIAGONAL_VECTORS
]


def load_board() -> list[str]:
    with open("input.txt") as input_file:
        return [
            line.strip()
            for line in input_file
        ]


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    board = load_board()
    h, w = len(board), len(board[0])

    # Count the number of MAS diagonals, if the count is 2 then there's an XMAS
    xmas_count = sum(
        1
        for i in range(h)
        for j in range(w)
        if board[i][j] == "A"
        and sum(
            all(
                ((0 <= i + delta_i < h) and (0 <= j + delta_j < w))
                and board[i + delta_i][j + delta_j] == "MS"[mas_index]
                for mas_index, (delta_i, delta_j) in enumerate(pattern)
            )
            for pattern in DIAGONAL_PATTERNS
        ) == 2
    )

    print(f"There are {xmas_count} instances of X-MAS on the board")


if __name__ == '__main__':
    main()
