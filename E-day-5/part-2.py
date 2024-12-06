import codetiming
import collections


def load_input() -> tuple[collections.defaultdict[int, set], list[list[int]]]:
    with open("input.txt") as input_file:
        ordering, rules = input_file.read().split("\n\n")

    ordering_dict = collections.defaultdict(set)
    for order in ordering.split("\n"):
        left, right = order.strip().split("|")
        ordering_dict[int(left)].add(int(right))

    rules = [
        list(map(int, rule.split(",")))
        for rule in rules.split("\n")
    ]

    return ordering_dict, rules


def topological_sort(nodes: list[int], edges: collections.defaultdict[int, set]):
    nodes = set(nodes)

    # Only use nodes from requested list
    exterior_edges = collections.defaultdict(set)
    in_degree = collections.defaultdict(int)
    for node in nodes:
        for to_node in edges[node]:
            if to_node in nodes:
                exterior_edges[node].add(to_node)
                in_degree[to_node] += 1

    # Do topological sort
    sorted_output = []
    leaf_nodes = {node for node in nodes if in_degree[node] == 0}

    while leaf_nodes:
        current = leaf_nodes.pop()
        sorted_output.append(current)

        for adj in exterior_edges[current].copy():
            exterior_edges[current].remove(adj)
            in_degree[adj] -= 1
            if in_degree[adj] == 0:
                leaf_nodes.add(adj)

    return sorted_output


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    ordering, pages = load_input()

    middle_page_sum = sum(
        topological_sort(page, ordering)[len(page) // 2]
        for page in pages
        if not all(
            all(
                page[future_idx] in ordering[page[current_idx]]
                for future_idx in range(current_idx + 1, len(page))
            )
            for current_idx in range(len(page) - 1)
        )
    )

    # O(|pages|) * O(|page|) * O(|page|) * O(V + E)

    print(f"The sum of the middle page number of the incorrect (turned correct) updates is {middle_page_sum}")


if __name__ == '__main__':
    main()
