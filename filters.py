grades = ['B', 'A', 'F', 'C', 'F', 'A']

def remove_fails(grade):
    return grade != 'F'

# FILTER
print(list(filter(remove_fails, grades)))

# Normal method

filtered_grades = []

for grade in grades:
    if grade != 'F':
        filtered_grades.append(grade)
print(filtered_grades)

#Comprehension

print([grade for grade in grades if grade != 'F'])