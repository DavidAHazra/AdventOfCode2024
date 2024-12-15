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

    return [
        list(line.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@."))
        for line in warehouse.split()
    ], movements.replace("\n", "")


def get_horisontal_shift(warehouse: list[list[str]], box_pos: tuple[int, int], move: tuple[int, int]) -> int:
    box_i, box_j = box_pos

    # Sanity checks
    assert move in (MOVES["<"], MOVES[">"])
    assert (warehouse[box_i][box_j] == "]" and move == MOVES["<"]) or (
            warehouse[box_i][box_j] == "[" and move == MOVES[">"])

    shift = 0
    h, w = len(warehouse), len(warehouse[0])
    while 0 <= box_j < w:
        if warehouse[box_i][box_j] == "#":
            return 0

        if warehouse[box_i][box_j] == ".":
            return shift

        box_j += move[1]
        shift += 1


def vertical_boxes_in_path(warehouse: list[list[str]], box_pos: tuple[int, int], move: tuple[int, int]) \
        -> set[tuple[int, int]]:

    box_i, box_j = box_pos
    is_left = warehouse[box_i][box_j] == "["

    # Sanity checks
    assert move in (MOVES["^"], MOVES["v"])
    assert (is_left and warehouse[box_i][box_j + 1] == "]") or (not is_left and warehouse[box_i][box_j - 1] == "[")

    boxes = {
        (box_i, box_j),
        (box_i, box_j + ((2 * is_left) - 1))
    }

    to_check = [
        (i + move[0], j)
        for i, j in boxes
    ]

    for check_i, check_j in to_check:
        if warehouse[check_i][check_j] == "#":
            return set()

        if warehouse[check_i][check_j] in "[]":
            above = vertical_boxes_in_path(warehouse, (check_i, check_j), move)
            if len(above) == 0:
                return set()

            boxes.update(above)

    return boxes


def simulate_move(warehouse: list[list[str]], move: tuple[int, int], robot_pos: tuple[int, int]) \
        -> tuple[list[list[str]], tuple[int, int]]:

    new_i, new_j = (robot_pos[0] + move[0], robot_pos[1] + move[1])

    # Can't move through walls
    if warehouse[new_i][new_j] == "#":
        return warehouse, robot_pos

    # Move to empty space
    if warehouse[new_i][new_j] == ".":
        warehouse[robot_pos[0]][robot_pos[1]] = "."
        return warehouse, (new_i, new_j)

    # Horisontal movement is almost the same (movement along a single axis) O(w)
    if move in (MOVES["<"], MOVES[">"]):
        shift = get_horisontal_shift(warehouse, (new_i, new_j), move)
        if shift == 0:
            return warehouse, robot_pos

        cursor_i, cursor_j = robot_pos
        to_swap = "."
        for _ in range(shift + 2):
            warehouse[cursor_i][cursor_j], to_swap = to_swap, warehouse[cursor_i][cursor_j]

            cursor_i += move[0]
            cursor_j += move[1]

        return warehouse, (new_i, new_j)

    # Vertical movement is more annoying
    # Fetch all boxes that CAN move, then move them in a sorted order
    to_move = vertical_boxes_in_path(warehouse, (new_i, new_j), move)
    if len(to_move) == 0:
        return warehouse, robot_pos

    for i, j in sorted(to_move, reverse=move == MOVES["v"]):
        warehouse[i][j], warehouse[i + move[0]][j + move[1]] = ".", warehouse[i][j]

    warehouse[robot_pos[0]][robot_pos[1]] = "."
    return warehouse, (new_i, new_j)


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
        if warehouse[i][j] == "["
    )

    print(f"The sum of all boxes' GPS coordinates is {box_gps_sum}")


if __name__ == '__main__':
    main()
