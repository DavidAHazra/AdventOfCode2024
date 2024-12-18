import collections
import codetiming

DIMENSION = 70


def read_falling_bytes() -> list[tuple[int, int]]:
    with open("input.txt") as input_file:
        # noinspection PyTypeChecker
        return [
            tuple(map(int, line.split(",")))
            for line in input_file
        ]


def find_shortest_path(blocks: set[tuple[int, int]]) -> int | None:
    visited = set()
    queue = collections.deque([(0, 0, 0)])
    while queue:
        i, j, steps = queue.popleft()

        if (i, j) in visited:
            continue

        if (i, j) == (DIMENSION, DIMENSION):
            return steps

        visited.add((i, j))

        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            adj_i, adj_j = i + di, j + dj

            if (
                    0 <= adj_i <= DIMENSION and
                    0 <= adj_j <= DIMENSION and
                    (adj_i, adj_j) not in blocks and
                    (adj_i, adj_j) not in visited
            ):
                queue.append((adj_i, adj_j, steps + 1))


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    falling = read_falling_bytes()

    print(f"The shortest path after 1024 simulations has length {find_shortest_path(set(falling[:1024]))}")


if __name__ == '__main__':
    main()
