import codetiming

MOVES = {
    "<": (0, -1),
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0)
}


def read_warehouse_and_movements() -> tuple[list[list[str]], str]:
    with open("input.txt") as input_file:
        warehouse, movements = input_file.read().split("\n\n")
        return list(map(list, warehouse.split())), movements.replace("\n", "")


def simulate_move(warehouse: list[list[str]], move: tuple[int, int], robot_pos: tuple[int, int]) \
        -> tuple[list[list[str]], tuple[int, int]]:

    moved_i, moved_j = robot_pos[0] + move[0], robot_pos[1] + move[1]

    # Can't move through walls
    if warehouse[moved_i][moved_j] == "#":
        return warehouse, robot_pos

    # Move to empty space
    if warehouse[moved_i][moved_j] == ".":
        warehouse[robot_pos[0]][robot_pos[1]] = "."
        warehouse[moved_i][moved_j] = "@"
        return warehouse, (moved_i, moved_j)

    # Scan for empty space at the end of a group of boxes
    h, w = len(warehouse), len(warehouse[0])
    search_i, search_j = moved_i, moved_j
    while 0 <= search_i < h and 0 <= search_j < w:
        search_value = warehouse[search_i][search_j]

        # Found a wall, so we can't move the boxes
        if search_value == "#":
            return warehouse, robot_pos

        # Found empty space
        if search_value == ".":
            break

        # Found another box so keep looking
        search_i += move[0]
        search_j += move[1]

    warehouse[robot_pos[0]][robot_pos[1]] = "."
    warehouse[moved_i][moved_j] = "@"
    warehouse[search_i][search_j] = "O"
    return warehouse, (moved_i, moved_j)


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    warehouse, movements = read_warehouse_and_movements()
    h, w = len(warehouse), len(warehouse[0])

    # Find initial robot position
    robot_pos = None
    for i in range(h):
        for j in range(w):
            if warehouse[i][j] == "@":
                robot_pos = (i, j)
                break

        if robot_pos:
            break

    # Simulate movements
    for move in movements:
        warehouse, robot_pos = simulate_move(warehouse, MOVES[move], robot_pos)

    # Find sum of GPS coordinates
    box_gps_sum = sum(
        100 * i + j
        for i in range(h)
        for j in range(w)
        if warehouse[i][j] == "O"
    )
    print(f"The sum of all boxes' GPS coordinates is {box_gps_sum}")


if __name__ == '__main__':
    main()
