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

    # When the exit is blocked it is blocked for good, so the output is an ordered list of True (unblocked) followed
    # by False (blocked). We can binary search for the transition

    left, right = 0, len(falling) - 1
    while left <= right:
        mid = (left + right) // 2

        if find_shortest_path(set(falling[:mid])) is None:
            if find_shortest_path(set(falling[:mid - 1])) is not None:
                break

            right = mid - 1

        else:
            if find_shortest_path(set(falling[:mid + 1])) is None:
                break

            left = mid + 1

    formatted_first_block = ",".join(map(str, falling[(left + right) // 2]))
    print(f"The coordinates of thh first byte that prevents the exit being reachable is: {formatted_first_block}")


if __name__ == '__main__':
    main()
