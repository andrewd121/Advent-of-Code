from AoC import AoC
import re
import numpy as np

class Day1(AoC):
    def __init__(self, example: bool = False):
        super().__init__(example=example)

    def part_1(self):
        left_numbers, right_numbers = np.array(list(map(sorted,
            zip(*self.parse_lines(lambda line: map(int, re.findall(r'\d+', line))))
        )))
        return sum(
            abs(left_numbers - right_numbers)
        )

    def part_2(self):
        left_numbers, right_numbers = np.array(list(zip(
            *self.parse_lines(lambda line: map(int, re.findall(r'\d+', line)))
        )))
        freq_in_right = np.array([np.count_nonzero(right_numbers == num) for num in left_numbers])

        return sum(left_numbers * freq_in_right)

if __name__ == "__main__":
    # Example mode
    day1_example = Day1(example=True)
    day1_example.test_part_1(expected=11)
    day1_example.test_part_2(expected=31)

    # Real input mode
    day1 = Day1()
    print("Part 1:", day1.part_1())
    print("Part 2:", day1.part_2())
