import unittest
from class_Edgar import vehicle
from class_Edgar import truck
from class_Edgar import car

class TestVehicle(unittest.TestCase):

    def test_weight_is_positive(self):
        five_tons=truck(15,"white","Renault")
        five_tons.attributes(8,5)
        self.assertGreater(five_tons.weight,0)

    def test_honda_has_5_places(self):
        honda_civic=car(6,"red","Honda")
        honda_civic.attributes(5,"break")
        self.assertEqual(honda_civic.nb_of_places,5)

#this test does not work and I don't know why, there is no Error message
    #def family_car_is_not_a_sport_car(self):
       # scenic=car(4,"beige","Renault")
       # scenic.attributes(5,"family car")
       # ref=scenic.test_type("sport car")
       # self.assertIs(ref,"The type does not match")

    def test_scenic_is_a_car(self) :
        scenic = car(4,"beige","Renault")
        self.assertIsInstance(scenic,car)

    def test_renault_is_a_brand(self):
        vh = vehicle(7,"blue","Renault")
        self.assertMultiLineEqual("Renault",vh.brand)


if __name__ == '__main__':
    unittest.main()
