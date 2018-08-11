import unittest
import datetime
import os
from src.settings import settings



class settings_tests(unittest.TestCase):

#    def setUp(self):
#        self.parent_folder = fp.get_parent_folder()
#        self.curr_file = fp.get_curr_file()

    def test_init(self):
        ctf_settings = settings("ctf")
        self.assertEqual(ctf_settings.config_file_name, "conf.json")
        self.assertEqual(ctf_settings.root_path, "~/")
        self.assertEqual(ctf_settings.category_path, "~/ctf/")

        audit_settings = settings("audit")
        self.assertEqual(audit_settings.config_file_name, "conf.json")
        self.assertEqual(audit_settings.root_path, "~/")
        self.assertEqual(audit_settings.category_path, "~/audit/")

#   def test_curr_file(self):
#       curr_file_split = self.curr_file.split("/")
#
#       self.assertEqual(curr_file_split[-2], self.parent_folder.split("/")[-1])
#       self.assertEqual(curr_file_split[-1], "test_findpath.py")
