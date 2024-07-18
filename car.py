


class Car():
    def __init__(self,used = False,miles = 0,model = ""):
        self.used = used
        self.miles = miles
        self.model = model

    def set_model(self,model):
        self.model = model

    def get_model(self):
        return self.model

    def set_miles(self,miles):
        self.miles = miles

    def add_miles(self,addMiles):
        self.miles+=addMiles

    def get_miles(self):
        return self.miles

    def is_used(self):
        return self.used


