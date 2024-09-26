n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    score = list(map(float, line))
    student_marks[name] = score
    query_name = input()

print('%.02F' % (sum(student_marks[query_name]) / 3))



