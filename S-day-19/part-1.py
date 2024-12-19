import codetiming


def read_towels_and_designs() -> tuple[tuple[str], list[str]]:
    with open("input.txt") as input_file:
        towels, designs = input_file.read().split("\n\n")

    return tuple(map(str.strip, towels.split(","))), designs.split()


def is_possible(design: str, towels: tuple[str]) -> bool:
    if design == "":
        return True

    for towel in towels:
        if design.startswith(towel) and is_possible(design[len(towel):], towels):
            return True

    return False


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    towels, designs = read_towels_and_designs()

    possible_designs = sum(
        is_possible(design, towels)
        for design in designs
    )

    print(f"There are {possible_designs} possible designs")


if __name__ == '__main__':
    main()
