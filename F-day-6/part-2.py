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


def load_map() -> list[list[str]]:
    with open("input.txt") as input_file:
        return [
            list(line.strip())
            for line in input_file
        ]


def get_path(current_map: list[list[str]], guard_pos: tuple[int, int], guard_look: tuple[int, int]) \
        -> set[tuple[int, int]]:

    h, w = len(current_map), len(current_map[0])

    visited = {guard_pos}
    while True:
        new_pos = (guard_pos[0] + guard_look[0], guard_pos[1] + guard_look[1])

        if not ((0 <= new_pos[0] < h) and (0 <= new_pos[1] < w)):
            # Guard has left the map
            break

        if current_map[new_pos[0]][new_pos[1]] == "#":
            # Blocked, stay and rotate 90 degrees
            guard_look = TURNS[guard_look]
            continue

        guard_pos = new_pos
        visited.add(guard_pos)

    return visited


def is_infinite_loop(current_map: list[list[str]], guard_pos: tuple[int, int], guard_look: tuple[int, int]) -> bool:
    h, w = len(current_map), len(current_map[0])

    visited_states = {(guard_pos, guard_look)}
    while True:
        new_pos = (guard_pos[0] + guard_look[0], guard_pos[1] + guard_look[1])

        if not ((0 <= new_pos[0] < h) and (0 <= new_pos[1] < w)):
            # Guard has left the map
            return False

        if current_map[new_pos[0]][new_pos[1]] == "#":
            # Blocked, stay and rotate 90 degrees

            guard_look = TURNS[guard_look]

            if (guard_pos, guard_look) in visited_states:
                return True

            visited_states.add((guard_pos, guard_look))
            continue

        if (new_pos, guard_look) in visited_states:
            return True

        guard_pos = new_pos
        visited_states.add((guard_pos, guard_look))


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    guard_map = load_map()

    # Find starting position and orientation of the guard
    guard_pos, guard_look = None, None
    for i in range(len(guard_map)):
        for j in range(len(guard_map[0])):
            if guard_map[i][j] in {"^", "v", "<", ">"}:
                guard_pos = (i, j)
                guard_look = ORIENTATIONS[guard_map[i][j]]
                break

        if guard_pos:
            break

    # Get the path the guard traverses with no obstacles
    # We only need to check for infinite loops along this path
    current_path = get_path(guard_map, guard_pos, guard_look) - {guard_pos}

    num_infinite = 0
    for i, j in current_path:
        guard_map[i][j] = "#"
        num_infinite += is_infinite_loop(guard_map, guard_pos, guard_look)
        guard_map[i][j] = "."

    print(f"There are {num_infinite} positions to add obstacles that would cause an infinite loop for the guard")


if __name__ == '__main__':
    main()
