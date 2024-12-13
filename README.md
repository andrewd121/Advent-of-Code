# Advent of Code 2024

This repository contains my solutions to the [Advent of Code 2024](https://adventofcode.com/2024) challenges.

I have designed this repository to streamline the workflow for solving the Advent of Code puzzles.

### Key Features:
- A reusable base class (`AoC`)
- An automated setup script (`setup.py`)
- A consistent directory structure for each day

## Project Structure

```
advent_of_code/
    ├── AoC.py                  # Base class providing common utilities
    ├── setup.py                # Script to generate workspace for a specific day
    ├── day_01/
    │   ├── main.py             # Solution file for Day 1
    │   ├── example_data.txt    # Example input for testing
    │   ├── input_data.txt      # Real input from the Advent of Code website
    ├── day_02/
    │   ├── main.py
    │   ├── example_data.txt
    │   ├── input_data.txt
    └── ... (other days)
```


## Features

1. **Reusable `AoC` Base Class**:
   - Handles reading input files (`example_data.txt` and `input_data.txt`).
   - Provides utility functions like `parse_lines`, `parse_grid`, and timers.
   - Includes test helpers to verify your solutions.

2. **Automated Setup with `setup_day.py`**:
   - Quickly creates a directory for a specified day with:
     - Boilerplate code in `__main__.py`.
     - Empty `example_data.txt` and `input_data.txt` files for the day.

3. **Consistent Workflow**:
   - Focus on solving puzzles with minimal setup.
   - Pre-defined methods (`part_1` and `part_2`) to implement solutions.

---

## Usage

### 1. Setting Up a Day's Workspace

Run the setup script to create a workspace for a specific day:

```bash
    python setup_day.py <day_number>
```

### 2. Implementing Solutions

1. Open the generated directory for the day (e.g., `day_01/`), open file `__main.py__`
2. Implement solution for **Part 1** and **Part 2** by editing the methods `part_1` and `part_2`
3. Run your code with `python -m day_<day_number>`
