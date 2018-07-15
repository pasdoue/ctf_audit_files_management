import unittest
import datetime
from src import ctf



class ctf_tests(unittest.TestCase):


    """ Test for CTF class """

    def test_init(self):

        current_year = datetime.datetime.now().year
        toto = ctf.ctf("my super CTF")

        self.assertEqual(current_year, toto.date)
        self.assertEqual(toto.name, "my super CTF")