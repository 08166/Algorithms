import time

start_time = time.time()
"""
** 문자열 자료형
- 문자열 변수를 초기화할 때는 큰 따옴표(")나 작은 따옴표(')를 이용합니다.
- 문자열 안에 큰 따옴표나 작은따옴표가 포함되어야 하는 경우가 있습니다.
    - 전체 문자열을 큰 따옴표로 구성하는 경우, 내부적으로 작은따옴표를 포함할 수 있습니다.
    - 전체 문자열을 작은따옴표로 구성하는 경우, 내부적으로 큰 따옴표를 포함할 수 있습니다.
    - 혹은 백슬래시 (\) 를 사용하면, 큰따옴표나 작은따옴표를 원하는 만큼 포함시킬 수 있습니다.
"""
print("---------문자열 자료형---------")
data = 'Hello World!'
print(data)

data = "Don't you konw \"Python\"?"
print(data)












end_time = time.time()
print(f"time : {start_time - end_time}")