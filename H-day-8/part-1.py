import collections
import itertools
import codetiming


def load_antenna_map() -> list[str]:
    with open("input.txt") as input_file:
        return [
            line.strip()
            for line in input_file
        ]


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    antenna_map = load_antenna_map()
    h, w = len(antenna_map), len(antenna_map[0])

    # Group antennae by frequency
    frequency_groups = collections.defaultdict(list)
    for i in range(h):
        for j in range(w):
            if antenna_map[i][j] != ".":
                frequency_groups[antenna_map[i][j]].append((i, j))

    antinodes = set()
    for frequency in frequency_groups:
        for from_node, to_node in itertools.permutations(frequency_groups[frequency], 2):
            possible_antinode = (
                2 * to_node[0] - from_node[0],
                2 * to_node[1] - from_node[1]
            )

            if 0 <= possible_antinode[0] < h and 0 <= possible_antinode[1] < w:
                antinodes.add(possible_antinode)

    print(f"There are {len(antinodes)} antinodes")


if __name__ == '__main__':
    main()
