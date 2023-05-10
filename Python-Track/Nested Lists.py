if __name__ == '__main__':
    records = []
    grade = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        grade.append(score)
    grade = sorted(set(grade))
    lowest_grade = grade[1]
    name=[]
    for x in records:
        if x[1]== lowest_grade:
            name.append(x[0])
    name.sort()
    for x in name:
        print(x)
