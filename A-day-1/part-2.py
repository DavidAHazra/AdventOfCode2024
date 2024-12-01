import collections
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
    right_list_frequencies = collections.Counter(right_list)

    similarity_score = sum(
        left * right_list_frequencies.get(left, 0)
        for left in left_list
    )

    print(f"The similarity score between the two lists is {similarity_score}")


if __name__ == '__main__':
    main()
