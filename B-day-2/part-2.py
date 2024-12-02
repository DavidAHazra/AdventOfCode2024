import codetiming


def load_reports() -> list[list[int]]:
    with open('input.txt') as input_file:
        return [
            list(map(int, report.split()))
            for report in input_file
        ]


def is_safe_original(report):
    differences = [
        report[i + 1] - report[i]
        for i in range(len(report) - 1)
    ]

    is_increasing = differences[0] < 0
    return all(
        (differences[i] < 0) == is_increasing and (1 <= abs(differences[i]) <= 3)
        for i in range(len(differences))
    )


def is_safe_with_removals(report: list[int]) -> bool:
    if is_safe_original(report):
        return True

    return any(
        is_safe_original(report[:to_remove] + report[to_remove + 1:])
        for to_remove in range(len(report))
    )


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    safe_reports = sum(
        is_safe_with_removals(report)
        for report in load_reports()
    )

    print(f"There are {safe_reports} safe reports")


if __name__ == '__main__':
    main()
