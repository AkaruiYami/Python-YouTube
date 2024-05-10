salaries = list(map(int, input().split(",")))

result = [salaries[0]]
for salary in salaries[1::]:
    if salary > result[-1] + 200:
        result.append(salary)

print(*result, sep=", ")
