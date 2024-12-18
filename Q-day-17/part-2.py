import collections
import re
import codetiming


def read_program() -> tuple[list[int], list[int]]:
    with open("input.txt") as input_file:
        registers, program = input_file.read().split("\n\n")

    registers = [
        int(re.findall(r"\d+", line)[0])
        for line in registers.split("\n")
    ]

    program = list(map(int, program.replace("Program:", "").split(",")))

    return registers, program


def combo_operand(operand: int, registers: list[int]) -> int:
    return operand if operand < 4 else registers[operand - 4]


def adv(registers: list[int], raw_operand: int, instruction_pointer: int, _: list[int]) -> int:
    registers[0] //= 2 ** combo_operand(raw_operand, registers)
    return instruction_pointer + 2


def bxl(registers: list[int], operand: int, instruction_pointer: int, _: list[int]) -> int:
    registers[1] = registers[1] ^ operand
    return instruction_pointer + 2


def bst(registers: list[int], operand: int, instruction_pointer: int, _: list[int]) -> int:
    registers[1] = combo_operand(operand, registers) % 8
    return instruction_pointer + 2


def jnz(registers: list[int], operand: int, instruction_pointer: int, _: list[int]) -> int:
    return operand if registers[0] > 0 else instruction_pointer + 2


def bxc(registers: list[int], _: int, instruction_pointer: int, __: list[int]) -> int:
    registers[1] ^= registers[2]
    return instruction_pointer + 2


def out(registers: list[int], operand: int, instruction_pointer: int, output: list[int]) -> int:
    output.append(combo_operand(operand, registers) % 8)
    return instruction_pointer + 2


def bdv(registers: list[int], operand: int, instruction_pointer: int, _: list[int]) -> int:
    registers[1] = registers[0] // 2 ** combo_operand(operand, registers)
    return instruction_pointer + 2


def cdv(registers: list[int], operand: int, instruction_pointer: int, _: list[int]) -> int:
    registers[2] = registers[0] // 2 ** combo_operand(operand, registers)
    return instruction_pointer + 2


INSTRUCTIONS = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]


def get_output(registers: list[int], program: list[int]) -> list[int]:
    output, instruction_pointer = [], 0
    while instruction_pointer < len(program):
        instruction_pointer = INSTRUCTIONS[program[instruction_pointer]](
            registers, program[instruction_pointer + 1], instruction_pointer, output
        )

    return output


@codetiming.Timer(text="\n🕑 {:.5f} seconds")
def main():
    initial_registers, program = read_program()

    # Idea:
    # - observed that each 3 bits in A corresponds to a subarray of the output, so we can build A progressively
    # - also observed by plotting A against len(output) that it increases logarithmically (base 8).
    # - use bfs to exhaustively search for register A

    smallest_a = float('inf')
    queue = collections.deque([(0, 0)])
    while queue:
        base, depth = queue.popleft()

        if depth == len(program):
            smallest_a = min(smallest_a, base)
            continue

        for remainder in range(8):
            adj_a = 8 * base + remainder

            if get_output([adj_a, initial_registers[1], initial_registers[2]], program) == program[-depth - 1:]:
                queue.append((adj_a, depth + 1))

    print(f"The lowest initial value for register A that causes the program to output itself is {smallest_a}")


if __name__ == '__main__':
    main()
