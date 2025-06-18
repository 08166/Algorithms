def solution(v):
    # x_list = [p[0] for p in v]
    x_list = [p[0] for p in v]
    y_list = [p[1] for p in v]
    for x in x_list:
        if x_list.count(x) == 1:
            x4 = x
            break
    for y in y_list:
        if y_list.count(y) == 1:
            y4 = y
            break
    answer = [x4, y4]
    return answer

print(solution([[1, 4], [3, 4], [3, 10]]))
print(solution([[1, 1], [2, 2], [1, 2]]))