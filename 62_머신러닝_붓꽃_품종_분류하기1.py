#모든 데이터를 이용하여 학습시킨 경우
#이 경우 모든 데이터는 150개

import pandas as pd
from sklearn.svm import SVC

#컴퓨터가 불꽃의 품종을 분류해야 한다.
csv = pd.read_csv("./머신러닝/머신러닝/iris.csv")
lable = csv["variety"]
data = csv[["sepal.length","sepal.width","petal.length","petal.width"]]
# 위에 lable 줄과 달리 대괄호가 2개? #여러개의 데이터를 불러올때. 리스트형으로 넣어야 한다.

#컴퓨터가 사용할 모델(알고리즘)정하기
model = SVC() #SVC()라는 알고리즘이 선을 그어서 분류하는 방법이다
model.fit(data, lable) # fit() :data와 lable을 주어 학습시키는것

#학습한거 확인하기
#위에 data =csv[[]]애 넣어준 데이터 순서대로 질문을 물어봐야 한다
result = model.predict(([
    [4.2,1.4,10.2,2.0],
    [2.5,0.4,12.3,4.0],
    [1.5,5.4,2.3,14.0]
]))
print(result)