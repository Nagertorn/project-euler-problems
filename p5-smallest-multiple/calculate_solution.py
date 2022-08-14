def calculate_solution(valid_exponents: dict) -> int:
    keys = valid_exponents.keys()
    output = 1
    for key in keys:
        output *= pow(key, valid_exponents[key])
    return output


if __name__ == "__main__":
    a = {
        2: 3,
        3: 2,
        5: 1,
        7: 1
    }
    solution = calculate_solution(a)
    print(solution)
