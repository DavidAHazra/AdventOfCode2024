import codetiming
import re
import math


def load_memory() -> str:
    with open("input.txt") as input_file:
        return input_file.read()


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    memory = load_memory()

    cleaned = re.findall(
        r"(do(?:n't)?\(\)|mul\(\d{1,3},\d{1,3}\))",
        memory
    )

    is_enabled, result = True, 0
    for expression in cleaned:
        if expression == "do()":
            is_enabled = True

        elif expression == "don't()":
            is_enabled = False

        elif is_enabled:
            result += math.prod(map(int, expression.replace("mul(", "").replace(")", "").split(",")))

    print(f"The sum of the valid multiplications is {result}")


if __name__ == '__main__':
    main()
