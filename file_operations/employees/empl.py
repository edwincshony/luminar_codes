fw = open("file_operations\\employees\\employees.txt","w")

lst = ["shony","maja","elna"]

for line in lst:

    fw.write(line+"\n")