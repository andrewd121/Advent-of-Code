from AoC import AoC
import re
import numpy as np

class Day2(AoC):
    def __init__(self, example: bool = False):
        super().__init__(example=example)

    @staticmethod
    def is_safe(report):
        return (np.all((np.diff(report) >= 1) & (np.diff(report) <= 3)) or
                np.all((np.diff(report) <= -1) & (np.diff(report) >= -3)))

    def part_1(self):
        return sum(
            1 for report in self.parse_lines(lambda line: np.array(list(map(int, re.findall(r'\d+', line)))))
            if self.is_safe(report)
        )

    def part_2(self):
        return sum(
            1 for report in self.parse_lines(lambda line: np.array(list(map(int, re.findall(r'\d+', line)))))
            if self.is_safe(report) or any(
                self.is_safe(np.concatenate((report[:i], report[i+1:])))
                for i in range(len(report))
            )
        )

if __name__ == "__main__":
    # Example mode
    day2_example = Day2(example=True)
    day2_example.test_part_1(expected=2)
    day2_example.test_part_2(expected=4)

    # Real input mode
    day2 = Day2()
    print("Part 1:", day2.part_1())
    print("Part 2:", day2.part_2())
