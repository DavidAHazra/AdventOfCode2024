import codetiming
import re

WIDTH, HEIGHT = 101, 103


def read_robots() -> list[tuple[int, ...]]:
    with open("input.txt") as input_file:
        return [
            tuple(map(int, re.findall(r"-?\d+", line)))
            for line in input_file
        ]


def is_pattern_in_board(robots: list[tuple[int, int, int, int]]) -> bool:
    board = [
        ["."] * WIDTH
        for _ in range(HEIGHT)
    ]

    for i, j, _, _ in robots:
        board[j][i] = "X"

    # After visually inspecting the Easter egg there are 31 robots in a row which is unique
    for row in board:
        if "X" * 31 in "".join(row):
            return True

    return False


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    robots = read_robots()
    for seconds in range(1, 10000):
        robots = [
            (
                (pos_x + vel_x) % WIDTH,
                (pos_y + vel_y) % HEIGHT,
                vel_x, vel_y
            )
            for pos_x, pos_y, vel_x, vel_y in robots
        ]

        if is_pattern_in_board(robots):
            print(f"The fewest number of seconds for the robots to display a christmas tree is {seconds}")
            break


if __name__ == '__main__':
    main()
