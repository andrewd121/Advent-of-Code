from AoC import AoC
import re

class Day4(AoC):
    def __init__(self, example: bool = False):
        super().__init__(example=example)

    def part_1(self):
        horizontal_lines = self.input_data
        vertical_lines = [''.join(line) for line in zip(*horizontal_lines)]

        char_matrix = self.parse_grid()

        diagonals = [
            [char_matrix[i][i - p] for i in range(max(p, 0), min(len(char_matrix), len(char_matrix[0]) + p))]
            for p in range(-len(char_matrix) + 1, len(char_matrix[0]))
                    ] + [
            [char_matrix[i][p - i] for i in range(max(p - len(char_matrix[0]) + 1, 0), min(p + 1, len(char_matrix)))]
            for p in range(len(char_matrix) + len(char_matrix[0]) - 1)
        ]

        diagonal_lines = [''.join(line) for line in diagonals]

        possible_lines = horizontal_lines + vertical_lines + diagonal_lines

        def num_of_xmas(text):
            return len(re.findall(r'(?i)(?=(xmas|samx))', text))

        return sum(num_of_xmas(line) for line in possible_lines)

    def part_2(self):
        char_matrix = self.parse_grid()

        x_shapes = [[
            char_matrix[y][x],
            char_matrix[y][x + 2],
            char_matrix[y + 1][x + 1],
            char_matrix[y + 2][x],
            char_matrix[y + 2][x + 2]
        ] for x in range(len(char_matrix[0]) - 2)
            for y in range(len(char_matrix) - 2)]

        return sum(
            1
            for x_shape in x_shapes
            if ''.join(x_shape[0::2]) in ('MAS', 'SAM')
            and ''.join(x_shape[1:4]) in ('MAS', 'SAM')
        )

if __name__ == "__main__":
    # Example mode
    day4_example = Day4(example=True)
    day4_example.test_part_1(expected=18)
    day4_example.test_part_2(expected=9)

    # Real input mode
    day4 = Day4()
    print("Part 1:", day4.part_1())
    print("Part 2:", day4.part_2())
