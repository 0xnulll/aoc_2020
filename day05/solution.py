def get_seat_id(input):
    return int("".join(map(lambda c: "1" if c in {"B", "R"} else "0", input)), 2)


def get_solution_1(input):
    return max(map(get_seat_id, input))


def get_solution_2(input):
    sorted_seat = sorted(map(get_seat_id, input))
    for seat_index in range(1, len(sorted_seat)):
        if sorted_seat[seat_index] - 1 != sorted_seat[seat_index-1]:
            return sorted_seat[seat_index-1] + 1


def process_input(input):
    return [item.strip() for item in input.split("\n")]


with open('input.txt') as file:
    input_str = file.read()
    input_processed = process_input(input_str)
    print(f"Solution 1 = {get_solution_1(input_processed)}")
    print(f"Solution 2 = {get_solution_2(input_processed)}")
