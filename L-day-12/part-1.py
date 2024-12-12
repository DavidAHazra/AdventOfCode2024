import codetiming


def read_garden() -> list[str]:
    with open("input.txt") as input_file:
        return [
            line.strip()
            for line in input_file
        ]


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

            region_code = garden[i][j]
            area, perimeter = 0, 0

            # DFS all connected cells with region_code to determine area/perimeter
            stack = [(i, j)]
            while stack:
                current_i, current_j = stack.pop()
                if (current_i, current_j) in seen:
                    continue

                seen.add((current_i, current_j))

                area += 1
                perimeter += 4

                for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    adj_i, adj_j = current_i + di, current_j + dj

                    if 0 <= adj_i < h and 0 <= adj_j < w and garden[adj_i][adj_j] == region_code:
                        perimeter -= 1

                        if (adj_i, adj_j) not in seen:
                            stack.append((adj_i, adj_j))

            all_region_price += area * perimeter

    print(f"The total price of fencing all regions on the map is {all_region_price}")


if __name__ == '__main__':
    main()
