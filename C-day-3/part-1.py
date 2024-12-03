import codetiming
import re


def load_memory() -> str:
    with open("input.txt") as input_file:
        return input_file.read()


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    memory = load_memory()

    result = sum(
        int(left) * int(right)
        for left, right in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", memory)
    )

    print(f"The sum of the valid multiplications is {result}")


if __name__ == '__main__':
    main()
