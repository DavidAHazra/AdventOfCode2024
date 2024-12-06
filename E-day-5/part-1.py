import codetiming
import collections


def load_input() -> tuple[collections.defaultdict[int, set], list[list[int]]]:
    with open("input.txt") as input_file:
        ordering, rules = input_file.read().split("\n\n")

    ordering_dict = collections.defaultdict(set)
    for order in ordering.split("\n"):
        left, right = order.strip().split("|")
        ordering_dict[int(left)].add(int(right))

    rules = [
        list(map(int, rule.split(",")))
        for rule in rules.split("\n")
    ]

    return ordering_dict, rules


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    ordering, pages = load_input()

    middle_page_sum = sum(
        page[len(page) // 2]
        for page in pages
        if all(
            all(
                page[future_idx] in ordering[page[current_idx]]
                for future_idx in range(current_idx + 1, len(page))
            )
            for current_idx in range(len(page) - 1)
        )
    )

    print(f"The sum of the middle page number of the correctly ordered updates is {middle_page_sum}")


if __name__ == '__main__':
    main()
