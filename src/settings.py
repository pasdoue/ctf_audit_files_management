import os
import json




class settings:

    def __init__(self, category="ctf"):
        self.config_file_name = "conf.json"
        #print(os.getcwd())
        with open(os.getcwd() + "/" + self.config_file_name, 'r') as f:
            self.global_conf = json.load(f)

        self.category_conf = self.global_conf[category+"_conf"]
        self.root_path = self.global_conf["folder_audit_and_ctf"]
        self.category_path = self.global_conf["folder_audit_and_ctf"] + category + "/"


