#알파벳 분류

import glob
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# -------------------언어감지 함수 -----------------------------
def get_data_label(folder_name):
    def Normalize(i):
        return  i/total

    files = glob.glob("./머신러닝/머신러닝/language/{}/*.txt".format(folder_name))  # 폴더 내 텍스트 파일 추출
    data = []
    label = []

    for fname in files:
        # 레이블 구하기
        basename = os.path.basename(fname)
        lang = basename.split("-")[0] #레이블 추출 #각 파일 이름들을 하나씩 가져옴

        # 텍스트 추출하기
        with open(fname, "r", encoding="utf-8") as f:
            text = f.read()
            text = text.lower()  # 소문자 변환

        # 알파벳 출현 빈도 구하기
        code_a = ord("a")
        code_z = ord("z")
        cnt = [0 for n in range(0, 26)]  # 26개의 0
        for char in text:
            code_current = ord(char)
            if code_a <= code_current <= code_z: #알파벳 이외의 , . 등을 거르는 단계
                cnt[code_current - code_a] += 1
        #print(cnt) # 현재 리스트 안의 숫자가 너무 크다. 고쳐줘야 함 --> 데이터 전처리

        #데이터 전처리 하기(정규화) # 각 수를 리스트당 합계로 나누기
        total = sum(cnt)
        map(Normalize, cnt) #map : 리스트의 각 원소들(cnt)을 함수(Normalize)에 적용하게 한다.
        cnt_norm = list(map(Normalize,cnt)) #  0과 1사이로 된 모든숫자들이 들어가게 됨
                                      # map 함수 주의점 : list로 씌워줘야함
        # 리스트에 넣기
        label.append(lang)
        data.append(cnt_norm)
    return data, label


def show_me_the_graph(data, label):
    def Normalize(i):
        return i/total
    # 그래프 준비하기
    graph_dict = {}
    for i in range(0, len(data)):
        y = label[i]
        total = sum(data[i])
        x = list(map(Normalize, data[i]))
        if not (y in graph_dict):
            graph_dict[y] = x

    asclist = [[chr(n) for n in range(97, 97 + 26)]]
    df = pd.DataFrame(graph_dict, index=asclist)
    # 바그래프
    df.plot(kind='bar', subplots=True, ylim=(0, 0.15))
    plt.show()

#------------------------------------------------------------

train_data,train_label = get_data_label("train")
test_data,test_label = get_data_label("test")

#show_me_the_graph(train_data,train_label)

model = SVC()
model.fit(train_data, train_label)

result = model.predict(test_data)
score = accuracy_score(result,test_label)
#print(score)  -------------학습 끝-----------------------

#실제로 적용시키기
def Normalize(i):
    return i / total

test_string = """Ang kimtsi, binabaybay na kimchi, gimchi, kimchee, o kim chee sa Ingles, ay isang pagkaing itinuturing na pampalusog sa Korea. Mahalaga ang paglalagay ng pampalasa rito. Maaari itong gawin na may sari-saring mga uri ng mga gulay, ngunit mas pangkaraniwan ang repolyo at labanos. Binuburo ang mga gulay sa inasnang tubig at hinuhugasan pagkaraan. Pagkaraang matanggal ang tubig, nilalagyan ng mga pampalasa ang mga gulay. Mababa sa kaloriya at kolesterol ang kimtsi, at may mataas na antas ng hibla o pibra. Kung ihahambing sa mansanas, mas mataas ang bilang ng mga bitamina ng kimtsi.[1]"""
# 위키피디아에서 아무 문장이나 넣은것

   # 알파벳 출현 빈도 구하기
code_a = ord("a")
code_z = ord("z")
cnt = [0 for n in range(0, 26)]  # 26개의 0
for char in test_string:
    code_current = ord(char)
    if code_a <= code_current <= code_z:
        cnt[code_current - code_a] += 1
total = sum(cnt)
cnt_norm = list(map(Normalize, cnt))

answer =model.predict([cnt_norm])
print(answer)