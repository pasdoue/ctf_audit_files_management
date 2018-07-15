import os






class Audit():

    """ 
    Class used to manage audit folders inside your system
    
    It follows the following path structure : 

    path_to_folders_managed_by_program/audits/[company_name]/[date]/[agreements]
                                                                  /[working_dir]
                                                                  /[report]
    
    where : 
    - path_to_folders_managed_by_program : is the path where ctfs and audit are handled by this prog
    - audits :                             as were are in Audit class....
    - company_name :                       company name
    - date :                               date
    - date/agreements :                    any files and contracts you and the company agreed on before performing audit
    - date/working_dir :                   working directory of audit
    - date/report :                        any files/reports to give to the company at the end of the audit
    """

