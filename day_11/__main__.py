from AoC import AoC
from collections import Counter

class Day11(AoC):
    def __init__(self, example: bool = False):
        super().__init__(example=example)

    @staticmethod
    def sim_new_stone_states(start_state, num_blinks):
        stones = start_state
        for _ in range(num_blinks):
            for stone, count in list(stones.items()):
                stones[stone] -= count
                if stone == '0':
                    stones['1'] += count
                elif len(stone) % 2:
                    stones[str(int(stone) * 2024)] += count
                else:
                    mid = int(len(stone) / 2)
                    stones[str(int(stone[:mid]))] += count
                    stones[str(int(stone[mid:]))] += count
        return stones.values()

    def part_1(self):
        return sum(self.sim_new_stone_states(
            start_state=Counter(self.get_raw_file_content().split()),
            num_blinks=25))

    def part_2(self):
        return sum(self.sim_new_stone_states(
            start_state=Counter(self.get_raw_file_content().split()),
            num_blinks=75)
        )

if __name__ == "__main__":
    # Example mode
    day11_example = Day11(example=True)
    day11_example.test_part_1(expected=55312)
    day11_example.test_part_2(expected=None)

    # Real input mode
    day11 = Day11()
    print("Part 1:", day11.part_1())
    print("Part 2:", day11.part_2())
