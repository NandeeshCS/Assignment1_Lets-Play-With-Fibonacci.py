variable1, variable2 = 0, 1
result = []

while variable2 <= 50:
    result.append(variable2)
    variable1, variable2 = variable2, variable1 + variable2

print(result)
