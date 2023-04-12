if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for i in student_marks:
        if i == query_name:
            sum_scores = 0
            for j in range(len(student_marks[i])):
                sum_scores += student_marks[i][j]

    print(f"{sum_scores/3:.2f}")
