import pandas as pd

# 1차원 :Series, 2차원 : DateFrame
# []리스트 구조 -> 데이터분석에 용이하게 만든 라이브러리

temp = pd.Series([-20,-10,10,20])
print(temp)
print(temp[0])


# index추가
temp = pd.Series([-20,-10,10,20],index=['jan','Feb','Mar','Apr'])
print(temp)

# print(type(temp))
# print(type(1))
# print(type([1,2,3,4,5]))
