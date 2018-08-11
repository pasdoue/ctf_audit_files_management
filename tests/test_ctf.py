import unittest
import datetime
import os
from src.ctf import ctfs
import src.settings



class ctf_tests(unittest.TestCase):


    """ Test for CTF class """

    def test_init(self):

        current_year = datetime.datetime.now().year
        toto = ctfs("my super CTF")

        self.assertEqual(current_year, toto.date)
        self.assertEqual(toto.name, "my super CTF")
        self.assertEqual(toto.settings.root_path, "~/")
        self.assertEqual(toto.settings.category_path, "~/ctf/")
        #print(os.path.dirname(os.path.realpath(__file__)))
        #print(os.path.realpath(__file__))