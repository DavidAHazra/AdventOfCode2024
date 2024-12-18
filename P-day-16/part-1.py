import heapq

import codetiming

CARDINALS = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]


def read_map() -> list[str]:
    with open("input.txt") as input_file:
        return list(map(str.strip, input_file.readlines()))


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    race_map = read_map()

    start, end = None, None
    for i in range(len(race_map)):
        for j in range(len(race_map[0])):
            if race_map[i][j] == "S":
                start = (i, j)

            elif race_map[i][j] == "E":
                end = (i, j)

            if start and end:
                break

        if start and end:
            break

    lowest_score = None
    visited = set()
    priority_queue = [(0, start, (0, 1))]
    while priority_queue:
        cost, pos, direction = heapq.heappop(priority_queue)

        # Found the end. Due to priority queue we can break immediately since it must be the lowest cost
        if pos == end:
            lowest_score = cost
            break

        # Since we're using a priority queue we don't need to check that
        # the current tile has already been reached with a lower score
        if (pos, direction) in visited:
            continue

        visited.add((pos, direction))

        for di, dj in CARDINALS:
            adj_i, adj_j = pos[0] + di, pos[1] + dj

            # Don't need to check map bounds since it's encased in walls
            if race_map[adj_i][adj_j] != "#":
                heapq.heappush(
                    priority_queue,
                    (
                        cost + 1 + 1000 * ((di, dj) != direction),
                        (adj_i, adj_j),
                        (di, dj)
                    )
                )

    print(f"The lowest score a Reindeer could get is {lowest_score}")


if __name__ == '__main__':
    main()
