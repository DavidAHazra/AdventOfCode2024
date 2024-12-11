import functools
import codetiming


def read_stones() -> list[int]:
    with open("input.txt") as input_file:
        return list(map(int, input_file.read().split()))


@functools.cache
def f(stone: int, k: int) -> int:
    if k == 0:
        return 1

    # Rule 1
    if stone == 0:
        return f(1, k - 1)

    # Rule 2
    str_stone = str(stone)
    if len(str_stone) % 2 == 0:
        mid = len(str_stone) // 2
        return f(int(str_stone[:mid]), k - 1) + f(int(str_stone[mid:]), k - 1)

    # Rule 3
    return f(2024 * stone, k - 1)


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    stones = read_stones()

    # Initially I brute forced part 1 in 0.01 seconds
    # But my solution for part 2 was far superior, so I've used it here too

    num_stones = sum(
        f(stone, 25)
        for stone in stones
    )

    print(f"There are {num_stones} stones after blinking 25 times")


if __name__ == '__main__':
    main()
