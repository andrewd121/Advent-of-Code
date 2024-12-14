from AoC import AoC

class Day10(AoC):
    def __init__(self, example: bool = False):
        super().__init__(example=example)

    @staticmethod
    def surounding_coords(coord):
        return [(coord[0] + x, coord[1] + y) for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]]

    def part_1(self):
        grid = self.get_grid()

        trail_scores = []
        for trail_start in [coord for coord in grid if grid[coord] == '0']:
            trail = { 0 : {trail_start} }
            current_height = 0

            while trail.get(current_height):
                for coord in trail[current_height]:
                    for c in self.surounding_coords(coord):
                        if grid.get(c) == str(current_height + 1):
                            trail[current_height + 1] = trail.get(current_height + 1, set()) | {c}

                current_height += 1

            trail_scores.append(len(trail.get(9)))

        return sum(trail_scores)

    def part_2(self):
        grid = self.get_grid()

        trail_scores = []
        for trail_start in [coord for coord in grid if grid[coord] == '0']:
            trails = { (trail_start,) }
            current_height = 0

            while trails and current_height < 9:
                new_trails = set()
                for trail in trails:
                    for c in self.surounding_coords(trail[-1]):
                        if grid.get(c) == str(current_height + 1):
                            new_trails.add(trail + (c,))
                trails = new_trails
                current_height += 1

            trail_scores.append(len(trails))

        return sum(trail_scores)

if __name__ == "__main__":
    # Example mode
    day10_example = Day10(example=True)
    day10_example.test_part_1(expected=36)
    day10_example.test_part_2(expected=81)

    # Real input mode
    day10 = Day10()
    print("Part 1:", day10.part_1())
    print("Part 2:", day10.part_2())
