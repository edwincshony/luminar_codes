employees = ["hari","dijo","alan","akshay"]

fr = open("12.file_operations\\employees\\employees.txt","w")

for line in employees:

    fr.write(line+"\n")