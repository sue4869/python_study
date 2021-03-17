from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import json
import os

#감정 분석 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

okt = Okt() #한국의 형태소분석 --> 각 형태소마다 token화 한다.
tokenizer = Tokenizer(19417, oov_token = 'OOV')
with open('wordIndex.json') as json_file:
  word_index = json.load(json_file)
  tokenizer.word_index = word_index

loaded_model = load_model('best_model.h5')
def sentiment_predict(new_sentence):
    print(new_sentence)
    max_len = 30
    stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']
    new_sentence = okt.morphs(new_sentence, stem=True) # 토큰화
    new_sentence = [word for word in new_sentence if not word in stopwords] # 불용어 제거
    encoded = tokenizer.texts_to_sequences([new_sentence]) # 정수 인코딩
    pad_new = pad_sequences(encoded, maxlen = max_len) # 패딩
    score = float(loaded_model.predict(pad_new)) # 예측
    if score >= 0.5:
        print("{:.2f}% 확률로 긍정 리뷰입니다.".format(score*100)) #:.2f --> 소숫점 2자리 수까지만 표현
    else:
        print("{:.2f}% 확률로 부정 리뷰입니다.".format((1-score)*100))


    #---------추가----------
    if 0.8 <= score <1:
        return "매우긍정"
    elif 0.6 <= score < 0.8:
        return "긍정"
    elif 0.4 <= score <= 0.6:
        return "중립"
    elif 0.2 <= score < 0.4:
        return "부정"
    else:
        return "매우부정"
    #-----------------------

#네이버 영화 리뷰 크롤링
from bs4 import BeautifulSoup
import urllib.request as req

page_num = 1
emotion_result = {"매우긍정":0 ,"긍정":0, "중립":0,"부정":0,"매우부정":0}
while True:
    code = req.urlopen("https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=189069&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}".format(page_num))
    soup = BeautifulSoup(code, "html.parser")
    comment = soup.select("li > div.score_reple > p > span")
    if len(comment) == 0:
        break
    for i in comment:
        i = i.text.strip()
        if i == "관람객":
            continue

        result = sentiment_predict(i)
        emotion_result[result] += 1
        print("--------------------------------")
    page_num += 1
    if page_num == 10:
        break

#----------------------------달라지는 곳
#pyecharts bar3d검색 >> BD예제 코드 복사

from pyecharts import Bar3D

bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
x_axis = ["매우긍정", "긍정", "중립", "부정", "매우부정"]
y_aixs = []
data = [[0,0,emotion_result["매우긍정"]],[0,1,emotion_result["긍정"]],[0,2,emotion_result["중립"]],[0,3,emotion_result["부정"]],[0,4,emotion_result["매우부정"]]]
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
bar3d.add("", x_axis, y_aixs, [[d[1], d[0], d[2]] for d in data], is_visualmap=True,
          visual_range=[0, 20], visual_range_color=range_color, grid3d_width=200, grid3d_depth=40)
bar3d.show_config()
bar3d.render("./bar3d.html")

from selenium import webdriver #자동으로 결과 웹 브라우져 나오도록
import os
browser = webdriver.Chrome("./chromedriver.exe")
bar3d_html = os.path.abspath("./bar3d.html")
browser.get("file://" + bar3d_html)


