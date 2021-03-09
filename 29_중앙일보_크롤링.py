import urllib.request as req
from bs4 import BeautifulSoup
import  urllib.parse as par #한글을 특수한 문자로 변환

keyword = input("키워드 입력 >> ")
encoded = par.quote(keyword) #한글을 특수한 문자로 변환

page_num = 1
while True:
    url = "https://news.joins.com/Search/TotalNews?Keyword={}&SortType=New&SearchCategoryType=TotalNews&PeriodType=All&ScopeType=All&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&TotalCount=0&StartCount=0&IsChosung=False&IssueCategoryType=All&IsDuplicate=True&Page={}&PageSize=10&IsNeedTotalCount=True".format(encoded, page_num)
    code = req.urlopen(url)
    soup = BeautifulSoup(code, "html.parser")
    title = soup.select("h2.headline.mg > a")
    if len(title) == 0: # 리스트자료형인 title의 원소가 0개 라면 == 끝에 페이지까지 크롤링 완료 했으면?
        break
    for i in title:
        #print(i.string) #받아온 요소의 내용안에 또다른 요소가 있으면 none으로 출력 --> text로 대체
        print("제목 : ", i.text)
        print("링크 : ", i.attrs["href"]) #기사 본문의 주소 -> attrs : 속성값 가져오기
        code_news = req.urlopen(i.attrs["href"])
        soup_news = BeautifulSoup(code_news, "html.parser")
        content = soup_news.select_one("div#article_body") #요소 하나만 가져오기
        print(content.text.strip().replace("        "," ").replace("         ",""))#데이터 가공하기 -> strip : 쓸데 없는 공백 없애기 -> replace: 문자열 사이 공백
    page_num +=1
