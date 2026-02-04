def solution(age):
    answer = ''
    a = {
        0:"a", 
        1:"b", 
        2:"c", 
        3:"d", 
        4:"e", 
        5:"f", 
        6:"g",
        7:"h", 
        8:"i", 
        9:"j"
    }
    age_list = list(map(int, str(age)))

    for i in age_list:
        answer += a[i]

    return answer