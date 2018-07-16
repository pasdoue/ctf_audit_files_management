import os
import json




class settings:

    def __init__(self):
        self.config_file_name = "conf.json"
        with open(os.getcwd() + "/" + self.config_file_name, 'r') as f:
            self.global_conf = json.load(f)

        self.audit_conf = self.global_conf["audit_conf"]
        self.ctf_conf = self.global_conf["ctf_conf"]

