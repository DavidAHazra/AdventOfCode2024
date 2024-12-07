import codetiming


def load_equations() -> list[tuple[int, list[int]]]:
    with open("input.txt") as input_file:
        return [
            (int(target), list(map(int, parameters.split())))
            for line in input_file
            for target, parameters in [line.strip().split(":")]
        ]


def equals_target(target: int, params: list[int]):
    if len(params) == 1:
        return params[0] == target

    stack = [(params[0], params[1:])]

    while stack:
        current, remaining = stack.pop()

        if not remaining:
            if current == target:
                return True

            continue

        stack.append((current + remaining[0], remaining[1:]))
        stack.append((current * remaining[0], remaining[1:]))

    return False


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    equations = load_equations()

    result = sum(
        target
        for target, params in equations
        if equals_target(target, params)
    )

    print(f"The total calibration result is {result}")


if __name__ == '__main__':
    main()
