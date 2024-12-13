import os
import sys

def setup_day(day: int):
    """
    Setup directory, data files, and template code for the given day.
    :param day: The day of the challenge.
    """
    directory = f"day_{day:02d}"

    if not os.path.exists(directory):
        # Create the directory
        os.makedirs(directory)

        # Create the data files
        with open(f"{directory}/example.txt", "w") as f:
            f.write("# Add example data here\n")
        with open(f"{directory}/input.txt", "w") as f:
            f.write("# Add real input data here\n")

        # Create the main Python file
        main_code = f"""from AoC import AoC

class Day{day}(AoC):
    def __init__(self, example: bool = False):
        super().__init__(example=example)

    def part_1(self):
        # Add logic for part 1 here
        return

    def part_2(self):
        # Add logic for part 2 here
        return

if __name__ == "__main__":
    # Example mode
    day{day}_example = Day{day}(example=True)
    day{day}_example.test_part_1(expected=None)
    day{day}_example.test_part_2(expected=None)

    # Real input mode
    day{day} = Day{day}()
    print("Part 1:", day{day}.part_1())
    print("Part 2:", day{day}.part_2())
"""
        with open(f"{directory}/__main__.py", "w") as f:
            f.write(main_code)

        print(f"Setup complete for Day {day}: {directory}/")
    else:
        print(f"Directory {directory} already exists. No changes made.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python setup.py <day_number>")
    else:
        try:
            day = int(sys.argv[1])
            setup_day(day)
        except ValueError:
            print("Error: <day_number> must be an integer.")