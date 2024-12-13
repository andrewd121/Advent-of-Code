from AoC import AoC
import re
from collections import deque

class Day3(AoC):
    def __init__(self, example: bool = False):
        super().__init__(example=example)

    def part_1(self):
        return sum(
            int(num1) * int(num2)
            for num1, num2 in
            re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', self.get_raw_file_content())
        )

    def part_2(self):
        instruction_reg = deque(maxlen=7)
        valid_content = []
        read_flag = True

        for char in self.get_raw_file_content():
            instruction_reg.append(char)
            instruction = "".join(instruction_reg)

            if instruction == "don't()":
                read_flag = False
            elif "do()" in instruction:
                read_flag = True

            if read_flag:
                valid_content.append(char)

        return sum(
            int(num1) * int(num2)
            for num1, num2 in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', "".join(valid_content))
        )


if __name__ == "__main__":
    # Example mode
    day3_example = Day3(example=True)
    day3_example.test_part_1(expected=161)
    day3_example.test_part_2(expected=48)

    # Real input mode
    day3 = Day3()
    print("Part 1:", day3.part_1())
    print("Part 2:", day3.part_2())
