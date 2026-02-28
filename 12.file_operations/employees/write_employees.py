employees = ["hari","dijo","alan","akshay"]

fw = open("12.file_operations\\employees\\employees.txt","w")


for e in employees:

    fw.write(e+"\n")


print("completed............")