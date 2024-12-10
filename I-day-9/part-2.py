import codetiming


def read_disk() -> list[int]:
    with open("input.txt") as input_file:
        return list(map(int, input_file.read()))


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    disk = read_disk()

    disk = [
        (block_idx // 2 if block_idx % 2 == 0 else None, length)
        for block_idx, length in enumerate(disk)
    ]

    for right in range(len(disk) - 1, -1, -1):
        if disk[right][0] is None:
            continue

        for left in range(0, right):
            if disk[left][0] is not None or disk[left][1] < disk[right][1]:
                continue

            if disk[left][1] == disk[right][1]:
                disk[left], disk[right] = disk[right], disk[left]
                break

            # Found space, but too much
            right_copy = disk[right]
            disk[right] = (None, right_copy[1])
            disk[left] = (disk[left][0], disk[left][1] - right_copy[1])
            disk.insert(left, right_copy)
            break

    checksum, checksum_index = 0, 0
    for block_idx, length in disk:
        if block_idx is not None:
            checksum += block_idx * length * (2 * checksum_index + length - 1) // 2

        checksum_index += length

    print(f"The compressed filesystem checksum is {checksum}")


if __name__ == '__main__':
    main()
