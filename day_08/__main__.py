from AoC import AoC
from itertools import combinations

class Day8(AoC):
    def __init__(self, example: bool = False):
        super().__init__(example=example)

    def part_1(self):
        grid = self.get_grid_complex()

        freq_dict = {
            freq: [coords for coords in grid if grid[coords] == freq]
            for freq in set(grid.values()) - {'.'} # frequencies - . is not a frequency
        }

        antinodes = {
            antinode
            for freq in freq_dict.values()
            for a, b in combinations(freq, 2)
            for antinode in (2 * b - a, 2 * a - b)
            if antinode in grid
        }

        return len(antinodes)

        # Alternative solution
        # antinodes = set()
        # for freq in freq_dict.values():
        #     for a, b in combinations(freq, 2):
        #         antinodes.update({antinode for antinode in [2 * b - a, 2 * a - b] if antinode in grid})

    def part_2(self):
        grid = self.get_grid_complex()

        freq_dict = {
            freq: [coords for coords in grid if grid[coords] == freq]
            for freq in set(grid.values()) - {'.'} # frequencies - . is not a frequency
        }

        def is_close(a, b, tolerance=1e-10):
            return abs(a - b) < tolerance

        antinode_lines = set()
        for freq in freq_dict.values():
            for a, b in combinations(freq, 2):
                # Handle vertical and non-vertical lines separately
                if is_close(a.real, b.real):
                    antinode_lines.add(('vertical', a.real))
                else:
                    m = (b.imag - a.imag) / (b.real - a.real)
                    b = a.imag - m * a.real
                    antinode_lines.add(('slope', m, b))

        antinodes = set()
        for location in grid:
            for line in antinode_lines:
                if line[0] == 'vertical':
                    # Check if x coordinate matches
                    if is_close(location.real, line[1]):
                        antinodes.add(location)
                        break
                else:
                    # Check if point satisfies line equation with tolerance
                    m, b_intercept = line[1], line[2]
                    if is_close(location.imag, m * location.real + b_intercept):
                        antinodes.add(location)
                        break

        return len(antinodes)

if __name__ == "__main__":
    # Example mode
    day8_example = Day8(example=True)
    day8_example.test_part_1(expected=14)
    day8_example.test_part_2(expected=34)

    # Real input mode
    day8 = Day8()
    print("Part 1:", day8.part_1())
    print("Part 2:", day8.part_2())