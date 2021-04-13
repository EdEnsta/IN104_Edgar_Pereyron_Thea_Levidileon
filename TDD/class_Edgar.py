class vehicle:

    def __init__(self,horsepower,color,brand):
        self.horsepower = horsepower
        self.color = color
        self.brand = brand

class truck (vehicle):
    def attributes(self,nb_wheels,weight):
        self.nb_wheels = nb_wheels
        self.weight = weight

    def get_weight(self):
        return("This truck weighs " +str(self.weight)+ "tons. ")


class car (vehicle):
    def attributes(self,nb_of_places,type):
        self.nb_of_places = nb_of_places
        self.type = type  # voiture de sport, voiture utilitaire etc...

    def test_type(self, ref):
        if (self.type == ref):
            return ("The car has a matched type.")
        else:
            return("The type does not match.")