import codetiming


def read_topology() -> list[list[int]]:
    with open("input.txt") as input_file:
        return [
            list(map(int, line.strip()))
            for line in input_file
        ]


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    topology = read_topology()
    h, w = len(topology), len(topology[0])

    stack = [
        ((i, j), (i, j))
        for i in range(h)
        for j in range(w)
        if topology[i][j] == 0
    ]

    trailhead_rating_sum = 0
    while stack:
        (start_i, start_j), (current_i, current_j) = stack.pop()
        current_height = topology[current_i][current_j]

        if current_height == 9:
            trailhead_rating_sum += 1
            continue

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            adj_i, adj_j = current_i + di, current_j + dj

            if 0 <= adj_i < h and 0 <= adj_j < w and topology[adj_i][adj_j] == current_height + 1:
                stack.append(((start_i, start_j), (adj_i, adj_j)))

    print(f"The trailhead ratings sum to {trailhead_rating_sum}")


if __name__ == '__main__':
    main()