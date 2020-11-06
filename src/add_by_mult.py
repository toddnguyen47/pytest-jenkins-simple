class AddByMult:
    def add(self, num1: int, num2: int) -> int:
        sign = (num1 < 0 < num2)
        sign = sign or (num1 > 0 > num2)
        num1 = abs(num1)
        num2 = abs(num2)

        sum1 = 0
        for _ in range(num2):
            sum1 = sum1 + num1

        if sign:
            sum1 = -sum1

        return sum1

    def get_one(self):
        return 1
