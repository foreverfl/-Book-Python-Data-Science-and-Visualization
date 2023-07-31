import pandas as pd

# 1. Slicing (슬라이싱)
arr = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 인덱스 2부터 인덱스 5까지의 원소를 슬라이싱하여 추출
result = arr[2:6]
print(result)


# 2. Indexing (인덱싱)
arr = pd.Series([11, 22, 33, 44, 55])

# 인덱스 3의 원소를 가져옴
result = arr[3]
print(result)


# 3. Boolean Indexing (불리언 인덱싱)
arr = pd.Series([1, 2, 3, 4, 5])

# 배열에서 짝수인 원소만 추출
condition = arr % 2 == 0
result = arr[condition]
print(result)


# 4. Fancy Indexing (팬시 인덱싱)
arr = pd.Series([10, 20, 30, 40, 50])

# 인덱스 1, 3의 원소를 추출
indices = [1, 3]
result = arr[indices]
print(result)
