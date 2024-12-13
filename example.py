from AoC import AoC

class Day1(AoC):
    def __init__(self, example: bool = False):
        super().__init__(example=example)

    def part_1(self) -> int:
        """Solve part 1 of the problem."""
        data = self.parse_lines(int)  # Example: parse lines as integers
        return sum(data)

    def part_2(self) -> int:
        """Solve part 2 of the problem."""
        data = self.parse_lines(int)
        return max(data)

if __name__ == "__main__":
    # Example mode
    day1_example = Day1(example=True)
    day1_example.test_part_1(expected=12)
    day1_example.test_part_2(expected=8)

    # Real input mode
    day1 = Day1()
    day1.start_timer()
    print("Part 1:", day1.part_1())
    day1.end_timer("Part 1")
    day1.start_timer()
    print("Part 2:", day1.part_2())
    day1.end_timer("Part 2")
