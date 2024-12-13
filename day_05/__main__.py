from AoC import AoC
from collections import defaultdict

class Day5(AoC):
    def __init__(self, example: bool = False):
        super().__init__(example=example)

    def part_1(self):
        # Get Lines
        lines = self.input_data

        # Split into rules and updates
        split_index = lines.index('')
        rules = [line.split('|') for line in lines[:split_index]]
        updates = [line.split(',') for line in lines[split_index + 1:]]

        # Return Sum of Middle Values of Valid Updates
        return sum(
            int(update[len(update) // 2])
            for update in updates
            if not any(
                update.index(rule[0]) > update.index(rule[1])
                for rule in rules if set(rule).issubset(set(update))
            )
        )

    def part_2(self):
        # Get Lines
        lines = self.input_data

        # Split into rules and updates
        split_index = lines.index('')
        rules = [line.split('|') for line in lines[:split_index]]
        updates = [line.split(',') for line in lines[split_index + 1:]]

        # Get incorrect updates
        incorrect_updates = [
            update
            for update in updates
            if any(
                update.index(rule[0]) > update.index(rule[1])
                for rule in rules if set(rule).issubset(set(update))
            )
        ]

        corrected_updates = []
        for update in incorrect_updates:
            relevant_rules = [rule for rule in rules if set(rule).issubset(set(update))]

            # Create the graph and in-degree dictionaries
            # graph = defaultdict(list)
            in_degree = defaultdict(int)

            # Populate graph and in-degree counts
            for before, after in relevant_rules:
                # graph[before].append(after)
                in_degree[after] += 1
                if before not in in_degree:
                    in_degree[before] = 0

            corrected_updates.append(list(dict(sorted(in_degree.items(), key=lambda item: item[1])).keys()))

        return sum(
            int(update[len(update) // 2]) for update in corrected_updates
        )



if __name__ == "__main__":
    # Example mode
    day5_example = Day5(example=True)
    day5_example.test_part_1(expected=143)
    day5_example.test_part_2(expected=123)

    # Real input mode
    day5 = Day5()
    print("Part 1:", day5.part_1())
    print("Part 2:", day5.part_2())
