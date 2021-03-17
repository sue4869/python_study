#감성분석 모델인 best_model 파일을 먼저 넣어둠
#감성 분류 함수
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import json
import os
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
    return score

#네이버 영화 리뷰 크롤링
from bs4 import BeautifulSoup
import urllib.request as req

page_num = 1
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

        result = sentiment_predict(i) #크롤링 된것을 감성분류함수에 넣기만 하면된다.
        print("--------------------------------")
    page_num += 1
    if page_num == 10:
        break