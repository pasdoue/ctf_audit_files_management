import os
import datetime





class CTF():

    """ 
    Class used to manage ctf folders inside your system
    
    It follows the following path structure : 

    path_to_folders_managed_by_program/ctfs/[ctf_name]/[year]/[category]/[chall_name]/
    
    where : 
    - path_to_folders_managed_by_program : is the path where ctfs and audit are handled by this prog
    - ctfs :                               as were are in CTF class....
    - ctf_name :                           name of the current CTF
    - year :                               the current year
    - category :                           one of the many categories encountered in general during CTF (stegano, forensic, pwn...)
    - chall_name :                         name of the current challenge/exercise you're trying to do (gambate ^^)
    """

    categories = ["stegano", "forensic", "prog", "pwn", "crypto", "web", "misc", "network", "app_script", "app_system"]

    def __init__(self, name):
        self.name = name
        self.date = datetime.datetime.now().year

        with open("../config.json") as config_file : 
            self.conf = json.load(config_file)["ctf_conf"]



class CTF_chall(CTF):

    def __init__(self):
        CTF.__init__(self)