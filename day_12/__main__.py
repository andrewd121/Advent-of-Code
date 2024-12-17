from AoC import AoC
from collections import defaultdict

class Day12(AoC):
    def __init__(self, example: bool = False):
        super().__init__(example=example)

    @staticmethod
    def get_regions(grid):
        class Region:
            def __init__(self, label: str = None):
                self.label = label
                self.boxes = set()
                self.vertices = set()
                self.area = 0
                self.perimeter = 0
                self.sides = 0

            def calc_area(self):
                self.area = len(self.boxes)

            def calc_sides(self):
                # Revert to counting vertices
                self.sides = len(self.vertices)

            def calc_vertices(self):
                corner_counts = defaultdict(int)

                # Iterate through each box and record corner touches
                for box in self.boxes:
                    for corner in [
                        (box[0], box[1]),  # top-left
                        (box[0], box[1] + 1),  # bottom-left
                        (box[0] + 1, box[1]),  # top-right
                        (box[0] + 1, box[1] + 1)  # bottom-right
                    ]:
                        corner_counts[corner] += 1

                # A vertex is a point shared by an odd number of boxes
                self.vertices = {corner for corner, count in corner_counts.items() if count % 2}


        regions = set()
        unallocated_points = grid.copy()

        while unallocated_points:
            coord, label = next(iter(unallocated_points.items()))

            region = Region(label)
            to_explore = {coord}

            while to_explore:
                c = to_explore.pop()
                if c in unallocated_points:
                    region.boxes.add(c)
                    del unallocated_points[c]

                    # Add neighboring cells to explore
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        neighbor = (c[0] + dx, c[1] + dy)
                        if grid.get(neighbor) == label:
                            to_explore.add(neighbor)
                        else:
                            # Edge exposed if neighbor is not part of the same region
                            if neighbor not in grid or grid.get(neighbor) != label:
                                region.perimeter += 1

            # Compute region stats
            region.calc_vertices()
            region.calc_area()
            region.calc_sides()

            # Add the region to the list
            regions.add(region)

        return regions

    def part_1(self):
        grid = self.get_grid()
        regions = self.get_regions(grid)

        return sum(
            region.area * region.perimeter
            for region in regions
        )

    def part_2(self):
        grid = self.get_grid()
        regions = self.get_regions(grid)

        return sum(
            region.area * region.sides
            for region in regions
        )

if __name__ == "__main__":
    # Example mode
    day12_example = Day12(example=True)
    day12_example.test_part_1(expected=1930)
    day12_example.test_part_2(expected=1206)

    # Real input mode
    day12 = Day12()
    print("Part 1:", day12.part_1())
    print("Part 2:", day12.part_2())
