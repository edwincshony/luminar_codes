"""10. Write a Python program to copy the contents of one file to another file."""

source = open("Tasks\\mar 2\\q10org.txt","r")
destination = open("Tasks\\mar 2\\q10copy.txt","w")

data = source.read()

destination.write(data)

