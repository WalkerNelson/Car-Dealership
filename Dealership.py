import car 
import employee

class Dealership:
    def __init__(self):
        self.staff = []
        self.inventory = []
        self.revenue = 0.0

    def get_revenue(self):
        return self.revenue

    def sell_car(self, model_name, used, employee_sold):
        for car in self.inventory:
            if car.model == model_name and car.used == used:
                self.inventory.remove(car)
                self.revenue += car.get_value()
                employee_sold.increment_cars_sold()
                employee_sold.generate_revenue(car.get_value())
                return f"Car sold by {employee_sold.name} for ${car.get_value()}"
        return "Car not found in inventory"

    def add_car(self, model_name, value, used=False):
        new_car = Car(model_name, value, used)
        self.inventory.append(new_car)

    def get_cars(self):
        return [(car.model, car.get_value(), car.used) for car in self.inventory]

    def in_stock(self, model_name, used):
        for car in self.inventory:
            if car.model == model_name and car.used == used:
                return True
        return False

    def add_employee(self, name, position):
        new_employee = Employee(name, position)
        self.staff.append(new_employee)

    def fire(self, name):
        self.staff = [employee for employee in self.staff if employee.name != name]
