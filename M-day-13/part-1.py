import codetiming
import re


def read_equations() -> list[list[tuple[int]]]:
    with open("input.txt") as input_file:
        return [
            [
                tuple(map(int, re.findall(r"\d+", line)))
                for line in block.split("\n")
            ]
            for block in input_file.read().split("\n\n")
        ]


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    equations = read_equations()

    # Each simultaneous equation is of the form
    # p_x = a_x * A + b_x * B
    # p_y = a_y * A + b_y * B
    #
    # Put into vector notation:
    # [p_x] = [a_x  b_x] * [A]
    # [p_y]   [a_y  b_y]   [B]
    #
    # or P = C * K
    #
    # To solve for K we can use the inverse of matrix C:
    # C^-1 * P = K
    #
    # The inverse of matrix C (C^-1), can be calculated using the determinant and the adjugate matrix
    # C^-1 = adj(C) / det(C)

    token_cost = 0
    for (ax, ay), (bx, by), (px, py) in equations:
        determinant = ax * by - ay * bx
        assert determinant != 0, "det(C) = 0 so C is not invertible (the equations are not solvable)"

        A_numerator = by * px - bx * py
        B_numerator = -ay * px + ax * py
        if A_numerator % determinant != 0 or B_numerator % determinant != 0:
            # Can't be solved in an integer number of button presses
            continue

        token_cost += 3 * int(A_numerator / determinant) + int(B_numerator / determinant)

    print(f"The fewest tokens you'd need to spend to win all prizes is {token_cost}")


if __name__ == '__main__':
    main()
