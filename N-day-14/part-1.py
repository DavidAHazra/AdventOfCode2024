import codetiming
import re

WIDTH, HEIGHT = 101, 103


def read_robots() -> list[tuple[int, ...]]:
    with open("input.txt") as input_file:
        return [
            tuple(map(int, re.findall(r"-?\d+", line)))
            for line in input_file
        ]


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    robots = read_robots()

    # Simulate robot positions 100 times
    for _ in range(100):
        robots = [
            (
                (pos_x + vel_x) % WIDTH,
                (pos_y + vel_y) % HEIGHT,
                vel_x, vel_y
            )
            for pos_x, pos_y, vel_x, vel_y in robots
        ]

    # Split into quadrants and count
    middle_x, middle_y = WIDTH // 2, HEIGHT // 2
    quadrant_counts = [0, 0, 0, 0]

    for pos_x, pos_y, _, _ in robots:
        # Here in_top != not in_bottom due to the discarded equality
        in_top, in_left, in_bottom, in_right = (pos_y < middle_y,
                                                pos_x < middle_x,
                                                pos_y > middle_y,
                                                pos_x > middle_x)

        quadrant_counts[0] += in_top and in_left
        quadrant_counts[1] += in_top and in_right
        quadrant_counts[2] += in_bottom and in_left
        quadrant_counts[3] += in_bottom and in_right

    safety_factor = quadrant_counts[0] * quadrant_counts[1] * quadrant_counts[2] * quadrant_counts[3]
    print(f"The safety factor after 100 seconds is {safety_factor}")


if __name__ == '__main__':
    main()
