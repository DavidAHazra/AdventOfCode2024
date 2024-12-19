import functools
import codetiming


def read_towels_and_designs() -> tuple[tuple[str], list[str]]:
    with open("input.txt") as input_file:
        towels, designs = input_file.read().split("\n\n")

    return tuple(map(str.strip, towels.split(","))), designs.split()


@functools.cache
def num_arrangements(design: str, towels: tuple[str]) -> int:
    if design == "":
        return 1

    return sum(
        num_arrangements(design[len(towel):], towels)
        for towel in towels
        if design.startswith(towel)
    )


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    towels, designs = read_towels_and_designs()

    sum_design_arrangements = sum(
        num_arrangements(design, towels)
        for design in designs
    )

    print(f"There are {sum_design_arrangements} total ways to make up all designs")


if __name__ == '__main__':
    main()
