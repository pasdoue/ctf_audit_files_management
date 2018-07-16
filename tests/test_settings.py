import unittest
import datetime
import os
from src.settings import settings



class settings_tests(unittest.TestCase):

#    def setUp(self):
#        self.parent_folder = fp.get_parent_folder()
#        self.curr_file = fp.get_curr_file()

    def test_init(self):
        curr_settings = settings()
        self.assertEqual(curr_settings.config_file_name, "conf.json")
        self.assertEqual(curr_settings.global_conf["folder_audit_and_ctf"], "~/")

#   def test_curr_file(self):
#       curr_file_split = self.curr_file.split("/")
#
#       self.assertEqual(curr_file_split[-2], self.parent_folder.split("/")[-1])
#       self.assertEqual(curr_file_split[-1], "test_findpath.py")
