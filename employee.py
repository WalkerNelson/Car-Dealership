class Employee:
    def __init__(self, name, position, cars_sold):
        self.name = name
        self.position = position
        self.cars_sold = cars_sold
        self.revenue_generated = 0.0

    def set_position(self, positionname):
        self.position = positionname

    def get_position(self):
        return self.position

    def increment_cars_sold(self):
        self.cars_sold += 1

    def get_cars_sold(self):
        return self.cars_sold

    def get_revenue_generated(self):
        return self.revenue_generated

    def generate_revenue(self, amount):
        self.revenue_generated += amount
