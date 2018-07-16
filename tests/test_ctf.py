import unittest
import datetime
import os
from src.ctf import ctf



class ctf_tests(unittest.TestCase):


    """ Test for CTF class """

    def test_init(self):

        current_year = datetime.datetime.now().year
        toto = ctf("my super CTF")

        self.assertEqual(current_year, toto.date)
        self.assertEqual(toto.name, "my super CTF")
        #print(os.path.dirname(os.path.realpath(__file__)))
        #print(os.path.realpath(__file__))