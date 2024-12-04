import codetiming
import itertools


UNIT_VECTORS = [
    (x, y)
    for x, y in itertools.product(range(-1, 2), repeat=2)
    if x != 0 or y != 0
]

SEARCH_PATTERNS = [
    [(dx * length, dy * length) for length in range(1, 4)]
    for dx, dy in UNIT_VECTORS
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

    # Iterate through board to find a starting point X
    # Once found, search in all directions for MAS and add it to total if found
    xmas_count = sum(
        sum(
            all(
                ((0 <= i + delta_i < h) and (0 <= j + delta_j < w))
                and board[i + delta_i][j + delta_j] == "MAS"[xmas_index]
                for xmas_index, (delta_i, delta_j) in enumerate(pattern)
            )
            for pattern in SEARCH_PATTERNS
        )
        for i in range(h)
        for j in range(w)
        if board[i][j] == "X"
    )

    print(f"There are {xmas_count} instances of XMAS in the word search")


if __name__ == '__main__':
    main()
