"""6. Write a Python program to create a file and write 5 lines of text into it.
"""

fw = open("Tasks\\mar 2\\q6file.txt","w")

names = ["edwin","gopi","sreerag","mustafa","rahul"]

for n in names:

    fw.write(n+"\n")