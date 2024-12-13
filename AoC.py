from abc import abstractmethod
from typing import List, Callable, Any
import time

class AoC:
    def __init__(self, example: bool = False):
        """
        Initialize the AoC class with a day number and example mode.
        :param example: Whether to use the example input file.
        """
        self.input_file = f"{'example' if example else 'input'}.txt"
        self.input_data = self.get_lines()
        self.start_time = None

    def get_lines(self) -> List[str]:
        with open(self.input_file, 'r') as f:
            return [line.strip() for line in f]

    def get_raw_file_content(self) -> str:
        """Return the raw data from the input file."""
        return ''.join(self.input_data)

    def parse_lines(self, parser: Callable[[str], Any] = str) -> List[Any]:
        """
        Parse each line of the input with the given parser function.
        :param parser: A function to apply to each line (e.g., int, str.split).
        :return: A list of parsed lines.
        """
        return [parser(line) for line in self.input_data]

    def get_grid(self) -> dict[tuple[int, int], str]:
        return {(x, y): c for y, row in enumerate(self.input_data) for x, c in enumerate(row)}

    def get_grid_complex(self) -> dict[complex, str]:
        return {x + y * 1j: c for y, row in enumerate(self.input_data) for x, c in enumerate(row)}

    # Looking to remove the following two methods
    def parse_grid_rows(self) -> tuple[tuple[str]]:
        """Parse input into a grid of characters."""
        return tuple(map(tuple, self.input_data))

    def parse_grid_columns(self) -> tuple[tuple[str]]:
        return tuple(zip(*self.parse_grid_rows()))

    def set_input_data(self, data: List[str]):
        """Directly set input data for testing without files."""
        self.input_data = data

    def start_timer(self):
        """Start a timer for performance measurement."""
        self.start_time = time.time()

    def end_timer(self, label: str = "Execution"):
        """End a timer and print the elapsed time."""
        if self.start_time is None:
            print("Timer not started!")
        else:
            elapsed = time.time() - self.start_time
            print(f"{label} took {elapsed:.4f} seconds")
            self.start_time = None

    @staticmethod
    def _evaluate_test(result: Any, expected: Any):
        if result == expected:
            print(f"✅ Test passed: {result} == {expected}")
        else:
            print(f"❌ Test failed: {result} != {expected}")

    def test_part_1(self, expected: Any):
        self._evaluate_test(
            result=self.part_1(),
            expected=expected
        )

    def test_part_2(self, expected: Any):
        self._evaluate_test(
            result=self.part_2(),
            expected=expected
        )

    @abstractmethod
    def part_1(self) -> Any:
        """Solve part 1 of the problem. Must be implemented in child class."""
        raise NotImplementedError("Part 1 is not implemented.")

    @abstractmethod
    def part_2(self) -> Any:
        """Solve part 2 of the problem. Must be implemented in child class."""
        raise NotImplementedError("Part 2 is not implemented.")
