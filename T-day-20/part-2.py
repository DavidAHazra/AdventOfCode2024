import codetiming

CARDINALS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

MAX_CHEAT_PICOSECONDS = 20

CHEAT_MOVEMENT = [
    (x, y, abs(x) + abs(y))
    for x in range(-MAX_CHEAT_PICOSECONDS, MAX_CHEAT_PICOSECONDS + 1)
    for y in range(-MAX_CHEAT_PICOSECONDS, MAX_CHEAT_PICOSECONDS + 1)
    if 2 <= abs(x) + abs(y) <= MAX_CHEAT_PICOSECONDS
]


def read_track() -> list[str]:
    with open("input.txt") as input_file:
        return [
            line.strip()
            for line in input_file
        ]


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    track = read_track()
    h, w = len(track), len(track[0])

    # Find start and end point
    start, end = None, None
    for i in range(h):
        for j in range(w):
            if track[i][j] == "S":
                start = (i, j)

            elif track[i][j] == "E":
                end = (i, j)

            if start and end:
                break

        if start and end:
            break

    # Find non-cheating path
    non_cheating_path = dict()
    stack = [start]
    while stack:
        i, j = stack.pop()

        non_cheating_path[(i, j)] = len(non_cheating_path) + 1

        if (i, j) == end:
            break

        for di, dj in CARDINALS:
            adj_i, adj_j = i + di, j + dj

            if (
                0 <= adj_i < h and
                0 <= adj_j < w and
                (adj_i, adj_j) not in non_cheating_path and
                track[adj_i][adj_j] != "#"
            ):
                stack.append((adj_i, adj_j))

    # Idea:
    # Pretty much the same as part 1 except with a bigger radius
    # We also can't assume that there is a fixed cost to cheating

    num_fast_paths = sum(
        0 <= pos[0] + di < h and
        0 <= pos[1] + dj < w and
        track[pos[0] + di][pos[1] + dj] != "#" and
        non_cheating_path[(pos[0] + di, pos[1] + dj)] - non_cheating_path[pos] - cheat_cost >= 100
        for pos in non_cheating_path
        for di, dj, cheat_cost in CHEAT_MOVEMENT
    )

    print(f"There are {num_fast_paths} cheating paths that would save at least 100 picoseconds")


if __name__ == '__main__':
    main()
