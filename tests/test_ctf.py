import unittest
import datetime
from src import CTF



class CTF_tests(unittest.TestCase):


    """ Test for CTF class """

    def test_init(self):

        current_year = datetime.datetime.now().year
        toto = CTF("my super CTF")

        self.assertNotEqual(current_year, toto.date)
        self.assertNotEqual(toto.name, "my super CTF")