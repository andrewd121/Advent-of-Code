from AoC import AoC
import re
import itertools

class Day7(AoC):
    def __init__(self, example: bool = False):
        super().__init__(example=example)

    @staticmethod
    def calc_calibration(lines, operators_dict):
        running_total = 0

        for line in lines:
            for solution, operands in line.items():
                for operators in itertools.product(operators_dict.keys(), repeat=len(operands) - 1):
                    result = operands[0]
                    for i, operator in enumerate(operators):
                        result = operators_dict[operator](result, operands[i + 1])

                    if result == solution:
                        running_total += solution
                        break

        return running_total

    def part_1(self):
        return self.calc_calibration(
            lines=self.parse_lines(
                lambda line: {
                    int(left): tuple(map(int, right.split()))
                    for left, right in re.findall(r"^(\d+):\s*([\d\s]+)$", line)
                }
            ),
            operators_dict={
                "+": lambda x, y: x + y,
                "*": lambda x, y: x * y
            }
        )

    def part_2(self):
        return self.calc_calibration(
            lines=self.parse_lines(
                lambda line: {
                    int(left): tuple(map(int, right.split()))
                    for left, right in re.findall(r"^(\d+):\s*([\d\s]+)$", line)
                }
            ),
            operators_dict={
                "+" : lambda x, y: x + y,
                "*" : lambda x, y: x * y,
                "||": lambda x, y: int(f"{x}{y}"),
            }
        )

if __name__ == "__main__":
    # Example mode
    day7_example = Day7(example=True)
    day7_example.test_part_1(expected=3749)
    day7_example.test_part_2(expected=11387)

    # Real input mode
    day7 = Day7()
    print("Part 1:", day7.part_1())
    print("Part 2:", day7.part_2())
