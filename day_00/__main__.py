from AoC import AoC
import re

class Day0(AoC):
    def __init__(self, example: bool = False):
        super().__init__(example=example)

    def part_1(self):
        def get_calibration_value(line):
            digits = re.findall(r'\d', line)
            return int(digits[0] + digits[-1])

        return sum(self.parse_lines(get_calibration_value))

    def part_2(self):
        # Text-to-number mapping for the given numbers in the text
        text_number_mapping = {
            'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
            'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
        }

        def get_calib_value(line):
            digits = re.findall(
                r'(?=(\d|' + '|'.join(text_number_mapping) + '))',
                line
            )
            digits = [text_number_mapping.get(d, d) for d in digits]
            return int(digits[0] + digits[-1])

        return sum(self.parse_lines(get_calib_value))


if __name__ == "__main__":
    # Example mode
    day0_example1 = Day0(example=True)
    # For some reason two different example datas are provided so set the data input manually/overwrite the input data
    day0_example1.input_data = "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet".split('\n')
    day0_example1.test_part_1(expected=142)

    day0_example2 = Day0(example=True)
    day0_example2.test_part_2(expected=281)

    # Real input mode
    day0 = Day0()
    print("Part 1:", day0.part_1())
    print("Part 2:", day0.part_2())
