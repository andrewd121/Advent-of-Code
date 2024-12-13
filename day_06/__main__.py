from AoC import AoC
import pandas as pd
from tqdm import tqdm


class Day6(AoC):
    def __init__(self, example: bool = False):
        super().__init__(example=example)

    def _run_guard_patrol_route_sim(self, rows, columns, start_position, start_direction):
        current_position = start_position
        current_direction = start_direction

        patrol_path = {
            'position': [start_position],
            'direction': [start_direction]
        }
        while True:
            x, y = current_position

            path_in_front = {
                0   : rows[y][x:],
                90  : columns[x][:y+1][::-1],
                180 : rows[y][:x+1][::-1],
                270 : columns[x][y:]
            }[current_direction]

            dist_to_obstacle = next((i for i, space in enumerate(path_in_front) if space == "#"), len(path_in_front))

            patrol_path['position'].extend({
                    0   : [(x + i, y) for i in range(1, dist_to_obstacle)],
                    90  : [(x, y - i) for i in range(1, dist_to_obstacle)],
                    180 : [(x - i, y) for i in range(1, dist_to_obstacle)],
                    270 : [(x, y + i) for i in range(1, dist_to_obstacle)]
                }[current_direction]
            )

            patrol_path['direction'].extend(current_direction for i in range(1, dist_to_obstacle))

            current_position = patrol_path['position'][-1]
            current_direction = (current_direction - 90) % 360

            if dist_to_obstacle >= len(path_in_front):
                break
            elif self._inf_loop_detection(patrol_path):
                return False

        return patrol_path

    @staticmethod
    def _inf_loop_detection(patrol_path):
        df = pd.DataFrame(patrol_path)
        duplicates = df[df.duplicated(['position', 'direction'], keep=False)]
        return not duplicates.empty


    def part_1(self):
        patrol_path = self._run_guard_patrol_route_sim(
            rows=self.parse_grid_rows(),  # Get rows - horizontal traversal
            columns=self.parse_grid_columns(),  # Get columns - vertical traversal
            start_position = next(((i, row.index("^")) for i, row in enumerate(self.parse_grid_columns()) if "^" in row)),
            start_direction = 90
        )

        return len(set(patrol_path['position']))

    def part_2(self):
        rows = self.parse_grid_rows()  # Get rows - horizontal traversal
        columns = self.parse_grid_columns()  # Get columns - vertical traversal
        start_position = next(((i, row.index("^")) for i, row in enumerate(columns) if "^" in row))
        start_direction = 90

        patrol_path = self._run_guard_patrol_route_sim(
            rows=rows,
            columns=columns,
            start_position=start_position,
            start_direction=start_direction
        )

        num_inf_loops = 0
        for position_in_path in tqdm(list(set(patrol_path['position']) - {start_position}), desc="Simulating Guard Pathing..."):
            x, y = position_in_path
            rows_copy = [[cell for cell in row] for row in rows]  # Convert rows and columns to lists
            columns_copy = [[cell for cell in col] for col in columns]

            rows_copy[y][x] = "#"
            columns_copy[x][y] = "#"
            if not self._run_guard_patrol_route_sim(
                rows=rows_copy,
                columns=columns_copy,
                start_position=start_position,
                start_direction=start_direction
            ):
                num_inf_loops += 1

        return num_inf_loops


if __name__ == "__main__":
    # Example mode
    day6_example = Day6(example=True)
    day6_example.test_part_1(expected=41)
    day6_example.test_part_2(expected=6)

    # Real input mode
    day6 = Day6()
    print("Part 1:", day6.part_1())
    print("Part 2:", day6.part_2())
