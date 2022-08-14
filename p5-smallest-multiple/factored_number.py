class factored_number:

    def __init__(self, number):
        self.number = number
        self.factors: dict = {}

    def get_number(self) -> int:
        return self.number

    def get_factors(self) -> dict:
        return self.factors

    def calculate_factors_from(self, smaller_numbers) -> None:
        number_to_factor = self.get_number()
        in_loop = True
        while in_loop:
            for number in smaller_numbers:
                number = number.get_number()
                if number == number_to_factor and self.factors != {}:
                    continue
                if number_to_factor % number == 0:
                    self.save(number)
                    if number_to_factor != number:
                        self.save(number_to_factor // number)
                    
                in_loop = False

    def save(self, number):
        if number in self.get_factors():
            self.factors[number] += 1
        else:
            self.factors[number] = 1

    def __str__(self):
        return self.number
