import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split #lable, data 훈련용과 테스트용으로 나누기
from sklearn.metrics import mean_squared_error #회귀용 채점지

csv = pd.read_csv("./머신러닝/머신러닝/Airbnb.csv")
label = csv["price"]
data = csv[["crim","dust","reservation","distance","like","review"]] #alt + 각각 더블클릭 --> 한번에 적용

train_data, valid_data, train_label,valid_label = train_test_split(data,label)
model = LinearRegression() #---> 자주쓰는 회귀전용모델
model.fit(train_data,train_label)

result = model.predict(valid_data)
score = mean_squared_error(result, valid_label)
#print(score **(1/2)) # 루트를 씌워줘야 정확하게 나온다.

answer = model.predict([
    [0.003021, 0.321, 4.3, 430, 143, 21]
])
print(answer)