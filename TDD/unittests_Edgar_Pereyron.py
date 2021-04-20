import unittest
from class_thea import sport
from class_thea import team
from class_thea import solo

class TestSport(unittest.TestCase):

    def test_sport_is_instance_of_sport(self):
        sp = sport("filet","sable","oui")
        self.assertIsInstance(sp,sport)

    def test_material_for_volley(self):
        volley = team("net","parquet floor","yes")
        self.assertMultiLineEqual("net",volley.material)

    def test_rugby_players_play_outside(self):
        rugby = team("ball","grass","yes")
        rugby.attribute(15,"outside")
        self.assertMultiLineEqual("outside",rugby.place)

    def test_begin_age_is_positive(self):
        judo = solo("kimono","tatami","yes")
        judo.attribute("no",4)
        self.assertGreater(judo.beginner_age,0)

if __name__ == '__main__':
    unittest.main()




