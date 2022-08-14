from calculate_solution import calculate_solution


def main_func(max_number: int) -> int:
    for number in range(1, max_number + 1):
        print(number)
    valids_exponents = {}

    solution = calculate_solution(valids_exponents)
    return solution


solution = main_func(10)
print(solution)
