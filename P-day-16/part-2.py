import heapq
import codetiming

CARDINALS = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]


def read_map() -> list[str]:
    with open("input.txt") as input_file:
        return [
            line.strip()
            for line in input_file
        ]


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

    unique_spots = set()
    visited = dict()
    priority_queue = [(0, start, {start}, (0, 1))]
    while priority_queue:
        cost, pos, path_tiles, direction = heapq.heappop(priority_queue)

        if pos == end:
            unique_spots.update(path_tiles)
            continue

        if (pos, direction) in visited and visited[(pos, direction)] < cost:
            continue

        visited[(pos, direction)] = cost

        for di, dj in CARDINALS:
            adj_i, adj_j = pos[0] + di, pos[1] + dj

            if race_map[adj_i][adj_j] != "#":
                heapq.heappush(
                    priority_queue,
                    (
                        cost + 1 + 1000 * ((di, dj) != direction),
                        (adj_i, adj_j),
                        path_tiles.union({(adj_i, adj_j)}),
                        (di, dj)
                    )
                )

    print(f"There are {len(unique_spots)} unique tiles part of the best paths through the maze")


if __name__ == '__main__':
    main()
