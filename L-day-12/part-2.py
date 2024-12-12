import collections

import codetiming

CARDINAL_DIRECTIONS = (
    (0, 1), (0, -1), (1, 0), (-1, 0)
)


def read_garden() -> list[str]:
    with open("input.txt") as input_file:
        return [
            line.strip()
            for line in input_file
        ]


def get_num_connected_components(points: set[tuple[int, int]]) -> int:
    result = 0
    while points:
        result += 1

        stack = [points.pop()]
        while stack:
            current_i, current_j = stack.pop()

            for di, dj in CARDINAL_DIRECTIONS:
                new_i, new_j = current_i + di, current_j + dj

                if (new_i, new_j) in points:
                    points.remove((new_i, new_j))
                    stack.append((new_i, new_j))

    return result


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    garden = read_garden()
    h, w = len(garden), len(garden[0])

    all_region_price = 0
    seen = set()
    for i in range(h):
        for j in range(w):
            if (i, j) in seen:
                continue

            edges = collections.defaultdict(set)
            region_code = garden[i][j]
            area = 0

            # DFS all connected cells with region_code to determine area and edge orientation
            stack = [(i, j)]
            while stack:
                current_i, current_j = stack.pop()
                if (current_i, current_j) in seen:
                    continue

                seen.add((current_i, current_j))
                area += 1

                for di, dj in CARDINAL_DIRECTIONS:
                    adj_i, adj_j = current_i + di, current_j + dj

                    if 0 <= adj_i < h and 0 <= adj_j < w and garden[adj_i][adj_j] == region_code:
                        if (adj_i, adj_j) in seen:
                            continue

                        stack.append((adj_i, adj_j))

                    else:
                        edges[(di, dj)].add((current_i, current_j))

            # Find all edges in the region by grouping connected edges with the same direction
            num_edges = sum(
                get_num_connected_components(edges[direction])
                for direction in edges
            )

            all_region_price += area * num_edges

    print(f"The total price of fencing all regions on the map is {all_region_price}")


if __name__ == '__main__':
    main()
