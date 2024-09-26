# Usando dicionario 
# There will always be one or more students having the second lowest grade.
# Output Format

# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

if __name__ == '__main__':
    students = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students[name] = score

    grades = sorted(set(students.values()))
    second_lowest_grade = grades[1]

    second_lowest_students = [name for name, score in students.items() if score == second_lowest_grade]

    second_lowest_students.sort()

    for student in second_lowest_students:
        print(student)

#usando lista
if __name__ == '__main__':
    alist = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        alist.append([name, score])
second_highest = sorted(set([score for name, score in alist]))[1]
print('\n'.join(sorted([name for name, score in alist if score == second_highest])))

