from AoC import AoC
from collections import defaultdict
from tqdm import tqdm

class Day9(AoC):
    def __init__(self, example: bool = False):
        super().__init__(example=example)

    @staticmethod
    def create_file_structure(disk_map):
        file_structure = []
        file_id = 0
        for i, instruction in enumerate(map(int, disk_map)):
            if i % 2 == 0:
                if instruction != 0:
                    file_structure.extend([str(file_id)] * instruction)
                    file_id += 1
            else:
                file_structure.extend(['.'] * instruction)

        return file_structure

    @staticmethod
    def create_grouped_file_structure(disk_map):
        file_structure = []
        file_id = 0
        for i, instruction in enumerate(map(int, disk_map)):
            if i % 2 == 0:
                if instruction != 0:
                    file_structure.append([str(file_id)] * instruction)
                    file_id += 1
            else:
                file_structure.append(['.'] * instruction)

        return file_structure

    @staticmethod
    def calc_checksum(file_structure):
        return sum(
            i * int(file_id)
            for i, file_id in enumerate(file_structure) if file_id != '.'
        )

    def part_1(self):
        disk_map = self.get_raw_file_content()

        file_structure = self.create_file_structure(disk_map)

        # Shuffle file structure
        left, right = 0, len(file_structure) - 1
        while left < right:
            # Find first free space from left
            while left < len(file_structure) and file_structure[left] != '.':
                left += 1
            # Find last non-dot file from right
            while right >= 0 and file_structure[right] == '.':
                right -= 1
            # If pointers haven't crossed, swap
            if left < right:
                file_structure[left], file_structure[right] = file_structure[right], '.'

        return self.calc_checksum(file_structure)


    def part_2(self):
        disk_map = self.get_raw_file_content()
        file_structure = self.create_file_structure(disk_map)
        grouped_file_structure = self.create_grouped_file_structure(disk_map)

        file_map = defaultdict(tuple)
        current_index = 0
        for group in grouped_file_structure:
            if group and group[0] != '.':  # Ignore free space
                file_map[group[0]] = (current_index, len(group))
            current_index += len(group)

        for file_id, file_address_info in tqdm(reversed(file_map.items()), desc='Files', total=len(file_map)):
            file_start, file_length = file_address_info
            free_space_address = 0
            is_free_space = False

            while free_space_address < file_start:
                free_space = file_structure[free_space_address:free_space_address + file_length]
                if file_length and free_space == ['.'] * file_length:
                    is_free_space = True
                    break
                else:
                    free_space_address += 1
                    is_free_space = False

            if is_free_space:
                file_structure[free_space_address:free_space_address + file_address_info[1]] = [file_id] * file_address_info[1]

                file_structure[file_address_info[0]:file_address_info[0] + file_address_info[1]] = ['.'] * file_address_info[1]

        return self.calc_checksum(file_structure)

if __name__ == "__main__":
    # Example mode
    day9_example = Day9(example=True)
    day9_example.test_part_1(expected=1928)
    day9_example.test_part_2(expected=2858)

    # Real input mode
    day9 = Day9()
    print("Part 1:", day9.part_1())
    print("Part 2:", day9.part_2())
