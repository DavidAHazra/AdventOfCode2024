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

    # Idea: each stone is independent of all others, so we can simulate for each and sum to get the result
    # Define some f(stone, k) = num stones after blinking k times starting with 'stone'
    # Each simulation will have overlapping subtasks, so we can memoize f(stone, k) for efficiency

    num_stones = sum(
        f(stone, 75)
        for stone in stones
    )

    print(f"There are {num_stones} stones after blinking 75 times")


if __name__ == '__main__':
    main()
