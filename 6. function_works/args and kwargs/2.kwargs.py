"""
**kargs = receives any number of parameter as dictionary
"""

def employee_detail(**kwargs:dict): #{'name': 'hari', 'dept': 'hr', 'salary': 23400}

    print(kwargs.get("name"))

employee_detail(name="hari",dept="hr",salary=23400)