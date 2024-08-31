class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model}")

if __name__ == "__main__":
    jlee = Car("JLR", "Range ROver", 2024)
    jlee.display_info()