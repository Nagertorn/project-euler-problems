from functools import reduce

def mult_eachother_in(numbers: list) -> int:
    return reduce((lambda x, y: x * y), numbers)

if __name__ == "__main__":
    assert mult_eachother_in([1,2,3]) == 6
    assert mult_eachother_in([5,6,7]) == 210
