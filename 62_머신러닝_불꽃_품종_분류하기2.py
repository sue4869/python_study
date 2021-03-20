import pandas as pd
from sklearn.svm import SVC
#학습용과 시험용으로 데이터를 나눌때 데이터를 랜덤하게 섞어줘야한다.
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score # 채점

csv = pd.read_csv("./머신러닝/머신러닝/iris.csv")
label = csv["variety"]
data = csv[["sepal.length","sepal.width","petal.length","petal.width"]]
train_data, valid_data, train_label,valid_label = train_test_split(data,label) #추가
#train_test_split의 데이터 반환값이 4개 였던것 #순서 중요

#컴퓨터가 사용할 모델(알고리즘)정하기 #학습용
model = SVC() #---> 분류전용
model.fit(train_data,  train_label) #전체 데이터의 3/4만 학습시킴 #수정

#학습한거 test
result = model.predict(valid_data) #수정
score = accuracy_score(result, valid_label) #(컴퓨터 답안지, 채점 )
                                            #컴퓨터가 최종적으로 맞춰야 할것 :valid_lable
#print(score) #score의 수치가 높을 수록 제시한 data와 label의 연관성이 높다는 것

#검증되었으니 이제 문제를 내서 컴퓨터에게 질문하자
answer = model.predict([
    [45.12,134.12,23.12,1.12]
])
print(answer)


# # , 예시
# def sum_and_multiply(a,b):
#     return a+b, a*b
#
# result1, result2 = sum_and_multiply(10,20)
# print(result2) #이렇게 한가지만 받아올 수 있다.
