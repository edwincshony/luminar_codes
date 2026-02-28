fr_all_students = open("12.file_operations\\failed students detector\\all_students.txt","r")
fr_passes_students = open("12.file_operations\\failed students detector\\passed_students.txt","r")
fr_failed_students = open("12.file_operations\\failed students detector\\failed_students.txt","w")

all_students_list = set([line.rstrip("\n")  for line in fr_all_students])
passes_students_list = set([line.rstrip("\n")  for line in fr_passes_students])

failed_students = set(all_students_list).difference(passes_students_list)

print(failed_students)

for f in failed_students:

    fr_failed_students.write(f+"\n")


# for all in all_students_list:

#     if all not in passes_students_list:

#         fr_failed_students.write(all+"\n")

