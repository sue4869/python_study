from bs4 import BeautifulSoup
import urllib.request as req

f = open("./알라딘중고샵.txt","w")

page_num = 1
while True :
    url="https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Used&KeyWord=%ED%8C%8C%EC%9D%B4%EC%8D%AC&KeyRecentPublish=0&OutStock=0&ViewType=Detail&SortOrder=11&CustReviewCount=0&CustReviewRank=0&KeyFullWord=%ED%8C%8C%EC%9D%B4%EC%8D%AC&KeyLastWord=%ED%8C%8C%EC%9D%B4%EC%8D%AC&CategorySearch=&chkKeyTitle=&chkKeyAuthor=&chkKeyPublisher=&ViewRowCount=25&page={}".format(page_num)
    code = req.urlopen(url)
    soup = BeautifulSoup(code,"html.parser")
    title = soup.select("a.bo3 > b")
    price = soup.select("a.bo_used > b")
    if len(title) == 0: #끝페이지까지 크롤링 완료
        break           # 끝 페이지까지 크롤링을 다하면, 다음 페이지가 아무것도 없으니 title 변수에 원소가 0개이다

    for i in range(len(title)):                          # len 함수에 리스트 함수 전달시 -> 리스트 속 원소의 개수를 알려줌
        print(title[i].string, price[i].string)          # range(n) : 0부터 n-1까지 들어있는 리스트를 한번에 만들어준다 0 1 2 3 4 ... n-1
        f.write(title[i].string + ", " + price[i].string + "\n")  #  -> 결론적으로 i는 리스트자료형들의 인덱스 번호를 뜻하게 된다
    page_num += 1
f.close()

# \n : 한줄씩 정보 나오게 한다