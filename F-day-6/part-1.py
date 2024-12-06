import codetiming

ORIENTATIONS = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1)
}

TURNS = {
    (-1, 0): (0, 1),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
    (0, 1): (1, 0)
}


def load_map() -> list[str]:
    with open("input.txt") as input_file:
        return list(map(str.strip, input_file.readlines()))


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    guard_map = load_map()
    h, w = len(guard_map), len(guard_map[0])

    guard_pos, guard_look = None, None
    for i in range(h):
        for j in range(w):
            if guard_map[i][j] in ("^", "v", "<", ">"):
                guard_pos = (i, j)
                guard_look = ORIENTATIONS[guard_map[i][j]]
                break

        if guard_pos:
            break

    visited = {guard_pos}
    while True:
        new_pos = (guard_pos[0] + guard_look[0], guard_pos[1] + guard_look[1])

        if not ((0 <= new_pos[0] < h) and (0 <= new_pos[1] < w)):
            # Guard has left the map
            break

        if guard_map[new_pos[0]][new_pos[1]] == "#":
            # Blocked, stay and rotate 90 degrees
            guard_look = TURNS[guard_look]
            continue

        guard_pos = new_pos
        visited.add(guard_pos)

    print(f"The guard visits {len(visited)} different locations")


if __name__ == '__main__':
    main()
