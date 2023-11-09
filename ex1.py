from collections import deque


def replace_at_index(lab: str, res: str, idx: int) -> str:
    return lab[:idx] + res + lab[idx + len(res):]
# takes str (labyrinth), replacement str and index; replaces the specified index in the str with replacement


def print_labyrinth(lab: list[str], path: list[tuple[int, int]] = None):
    height = len(lab)  # the dimensions of the original labyrinth
    width = len(lab[0]) if height > 0 else 0

    labyrinth_with_numbers = []

    top_edge_numbers = " " + "".join(str(i % 10) for i in range(width)) + " "
    labyrinth_with_numbers.append(top_edge_numbers)

    # Add numbers to the left and right edges
    for i in range(height):
        row = str(i % 10) + lab[i] + str(i % 10)
        labyrinth_with_numbers.append(row)

    bottom_edge_numbers = " " + "".join(str(i % 10) for i in range(width)) + " "
    labyrinth_with_numbers.append(bottom_edge_numbers)

    for row in labyrinth_with_numbers:
        print(row)

    solution = list(lab)

    if path:  # if path it is given
        for i, element in enumerate(path):
            row, column = element
            res = "X"
            if solution[row][column] == ' ':
                solution[row] = replace_at_index(solution[row], res, column)

        return solution


labyrinth = [
    "███████",
    "█     █",
    "█   ███",
    "█ ███ █",
    "█     █",
    "███████"
]


print_labyrinth(labyrinth)


def prompt_integer(message: str) -> int:  # prompts for valid integer input until valid int is entered
    while True:
        input_number = input(message)
        while input_number.isdigit():
            return int(input_number)
        print("Enter a valid number.")


def prompt_user_for_location(prompt: str) -> tuple:  # to get the row and column
    row = prompt_integer(f"{prompt} row: ")
    column = prompt_integer(f"{prompt} column: ")
    return row, column


start = prompt_user_for_location("Start")
end = prompt_user_for_location("End")
print("Start location is", start)
print("End location is", end)

# labyrinth is represented as a list of strings where each string is a row of the lab
# bfs takes lab, start and end locations; q is all considerable paths; v for visited locations;
# algorithm goes through possible moves (check if the move is traversable); so until the end loc is found


def bfs(lab: list[str], start_loc: tuple[int, int], end_loc: tuple[int, int]) -> list[tuple[int, int]]:
    q = deque([deque([start_loc])])  # holds all paths we considered until now and add start path here
    v = set()  # set holding all locations we already visited
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def is_traversable(location):
        x, y = location
        return 0 <= x < len(lab) and 0 <= y < len(lab[0]) and lab[x][y] == " "

    while q:
        path = q.popleft()
        last = path[-1]

        if last == end_loc:
            return list(path)

        if last not in v:
            v.add(last)

            for move in moves:
                next_x, next_y = last[0] + move[0], last[1] + move[1]
                next_location = (next_x, next_y)

                if is_traversable(next_location):
                    new_path = deque(path)
                    new_path.append(next_location)
                    q.append(new_path)
    return


result = bfs(labyrinth, start, end)


if result:
    print("Path found:", result)
    print("Solved labyrinth:")
    solved = list(labyrinth)
    for x, y in result:
        solved[x] = replace_at_index(solved[x], "X", y)
    print_labyrinth(solved)
else:
    print("No path found.")
