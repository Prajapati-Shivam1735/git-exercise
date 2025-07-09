class Adder:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

adder = Adder(number1, number2)
result = adder.add()

print("The sum is:", result)
