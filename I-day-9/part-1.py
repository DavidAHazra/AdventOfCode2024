import codetiming


def read_disk() -> list[int]:
    with open("input.txt") as input_file:
        return list(map(int, input_file.read()))


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    disk = read_disk()

    checksum, checksum_index = 0, 0
    left, right = 0, len(disk) - 1
    while left <= right:
        if left % 2 == 0 or disk[left] == 0:
            # Used to be a loop, simplified to single expression from arithmetic sequence
            checksum += (left // 2) * disk[left] * (2 * checksum_index + disk[left] - 1) // 2
            checksum_index += disk[left]
            left += 1
            continue

        if right % 2 == 1 or disk[right] == 0:
            right -= 1
            continue

        # Otherwise move data from right to left
        disk[right] -= 1
        disk[left] -= 1

        checksum += checksum_index * (right // 2)
        checksum_index += 1

    print(f"The compressed filesystem checksum is {checksum}")


if __name__ == '__main__':
    main()
