
students = [('Charlie', 35), ('David', 20), ('Alice', 30), ('Bob', 25)]
def sort_by_age(students):
       return sorted(students,key=lambda person:person[1])

sorted_students = sort_by_age(students)
print(sorted_students)