import codetiming


def load_lists() -> tuple[list[int], list[int]]:
    with open('input.txt') as input_file:
        return zip(
            *(
                map(int, line.split())
                for line in input_file
            )
        )


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    left_list, right_list = load_lists()
    assert len(left_list) == len(right_list)

    total_distance = sum(
        abs(left - right)
        for left, right in zip(sorted(left_list), sorted(right_list))
    )

    print(f"The total distance between the two lists is {total_distance}")


if __name__ == '__main__':
    main()
