from mult_eachother_in import mult_eachother_in
from remove_impostors import remove_impostors
from factored_number import factored_number


def solution_by_mind(range_of_numbers: range) -> int:

    factored_numbers: list[factored_number] = []

    for number in range_of_numbers:
        if number == 1:
            continue
        factored_numbers.append(factored_number(number))

    for f_number in factored_numbers:
        f_number.calculate_factors_from(factored_numbers)
        print(f_number.get_number(), f_number.get_factors())

    solution2 = mult_eachother_in(range_of_numbers)
    return solution2


if __name__ == "__main__":
    solution_by_mind([1, 2, 3, 4, 5, 6, 7, 8])
