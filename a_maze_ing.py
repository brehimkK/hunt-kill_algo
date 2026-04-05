import sys
import os
from maze.maze_solver import MazeSolver
from maze.maze_generator import MazeGenerator


def parse_config() -> dict:
    """
    Parse the Config File, Validate and Store the Data
    in a Dict, Handle the Error using try/Except to prevent
    Crashes
    """

    # Get Line, Strip it, Split based on '=', Store key value
    try:
        config = {}
        if len(sys.argv) > 1:
            filename = sys.argv[1]
            with open(filename, "r") as file:
                for line in file:
                    line = line.strip()
                    if line == "":
                        continue

                    elif line.startswith("#"):
                        continue

                    elif "=" not in line:
                        raise ValueError("Invalid Config Line")

                    else:
                        key, value = line.split("=", 1)
                        key, value = key.strip(), value.strip()
                        if key in config:
                            raise ValueError("Duplicate Lines")
                        config[key] = value
        else:
            raise IndexError("No Config File Given")

    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    # Convert the Dict values into valide Data ready to Use
    try:
        for key, value in config.items():

            if key in ["ENTRY", "EXIT"]:
                x, y = value.split(",")
                x, y = int(x), int(y)
                if x < 0 or y < 0:
                    raise ValueError(f"{key} coordinates out of bounds")
                config[key] = (x, y)

            elif key in ["WIDTH", "HEIGHT", "SEED"]:
                try:
                    config[key] = int(value)
                except (TypeError, ValueError):
                    raise ValueError(f"'{value}' must be an int")

            elif key == "PERFECT":
                value = value.lower().capitalize()
                if (
                    value == "0"
                    or value == "1"
                    or value == "+1"
                    or value == "+0"
                    or value == "-0"
                ):
                    config[key] = int(value)
                elif value in ["True", "False"]:
                    config[key] = value == "True"
                else:
                    raise ValueError(
                        "'PERFECT' value must be (True - False - 0 or 1)"
                    )

            elif key == "OUTPUT_FILE":
                lower_value = value.lower()
                if "." in value:
                    basename, format = lower_value.split(".", 1)
                    if format != "txt" or value == "":
                        raise ValueError(f"OUTPUT_FILE '{value}' is not valid")
                    config[key] = lower_value
                else:
                    raise ValueError("Output file format is Invalid")

    except Exception as err:
        print(f"ERROR: {err}", file=sys.stderr)
        sys.exit(1)

    return config


def init_program(algo: str) -> None:
    if algo == "hak":
        algo = "Hunt & Kill"
    if algo == "dfs":
        algo = "Depth first search - dfs"

    print("\n=== A_Maze_ing ===")
    print("1. Re-generate a new maze")
    print("2. Show/Hide path from entry to exit")
    print("3. Rotate maze colors")
    print(f"4. Toggle Algorithm ({algo.upper()})")
    print("5. Quit")


def start_program(maze: MazeGenerator) -> int:
    try:
        user_input = int(input("Choice? (1-5): "))
        if 1 <= user_input <= 5:
            return user_input
        else:
            print(f"'{user_input}' is not a valid choice!")
            return start_program(maze)
    except ValueError:
        print("Please enter a valid number.")
        return start_program(maze)


def main() -> None:
    config = parse_config()
    algo = "dfs"
    index = 0

    while True:
        maze = MazeGenerator(config)
        solve = MazeSolver(maze)
        try:
            maze.grid_builder()
            if not maze.grid:
                raise ValueError("Empty grid")

            # Get the Entry Coordinates from the config
            entry = config["ENTRY"]
            end = config["EXIT"]
            x, y = entry
            exit_x, exit_y = end

            start_block = maze.grid[y][x]
            end_block = maze.grid[exit_y][exit_x]

            maze.entry = start_block
            maze.exit = end_block

            maze.ft_pattern()
        except Exception as e:
            print(f"Unexpected Error: {e}")
            exit(0)

        if algo == "dfs":
            maze.dfs_generation(start_block)
        elif algo == "hak":
            maze.hunt_kill_generation()

        if not config["PERFECT"]:
            maze.random_loops()

        solve.solve_maze(start_block, end_block)

        # maze visualization
        maze.visual(index)

        try:
            hex_output = maze.hex_encoding()
            path = maze.path_direction()

            output_file = config["OUTPUT_FILE"]
            with open(output_file, "w") as f:
                for row in hex_output:
                    f.write("".join(row) + "\n")

                f.write("\n")
                f.write(f"{x},{y}")
                f.write("\n")
                f.write(f"{exit_x},{exit_y}")

                f.write("\n")
                for p in path:
                    f.write(p)
        except Exception as err:
            print(f"ERROR: {err}")

        while True:
            os.system("clear")
            maze.visual(index)
            init_program(algo)
            choice = start_program(maze)

            if choice == 1:
                config["SEED"] += 1
                break

            elif choice == 2:
                maze.show_path = not maze.show_path

            elif choice == 3:
                index = (index + 1) % 3

            elif choice == 4:
                algo = "hak" if algo == "dfs" else "dfs"
                break

            elif choice == 5:
                print(">> Exiting...")
                return


if __name__ == "__main__":
    main()
