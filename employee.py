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


# Employee One
employee = Employee("John Doe", "salesman", 20)
employee.generate_revenue(20000)
print(f"Name: {employee.name}")
print(f"Position: {employee.get_position()}")
print(f"Cars Sold: {employee.get_cars_sold()}")
print(f"Revenue Generated: ${employee.get_revenue_generated()}")

# Employee Two
print('\n')
employee = Employee("Jane Doe", "salesman", 21)
employee.generate_revenue(300000)
print(f"Name: {employee.name}")
print(f"Position: {employee.get_position()}")
print(f"Cars Sold: {employee.get_cars_sold()}")
print(f"Revenue Generated: ${employee.get_revenue_generated()}")
