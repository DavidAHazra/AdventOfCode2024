import codetiming


def load_reports() -> list[list[int]]:
    with open('input.txt') as input_file:
        return [
            list(map(int, report.split()))
            for report in input_file
        ]


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    safe_reports = 0
    for report in load_reports():
        differences = [
            report[i + 1] - report[i]
            for i in range(len(report) - 1)
        ]

        is_increasing = differences[0] < 0
        safe_reports += all(
            (differences[i] < 0) == is_increasing
            and (1 <= abs(differences[i]) <= 3)
            for i in range(len(differences))
        )

    print(f"There are {safe_reports} safe reports")


if __name__ == '__main__':
    main()
