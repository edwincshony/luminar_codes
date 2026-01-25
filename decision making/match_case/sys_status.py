"""
read prompt
if prompt is start then display system starting ....
if prompt is stop then display system stopping xxxx
if prompt is restart then display system restarting !!!!
display invalid prompt otherwise
"""

prompt = input("enter prompt: ")

match prompt:
    case "start": print("system starting ....")
    case "stop": print("system stopping xxxx")
    case "restart": print("system restrating !!!!")
    case _: print("invalid prompt")