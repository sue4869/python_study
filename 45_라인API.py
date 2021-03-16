#line Notify api >> 로그인 >>마이페이지 >> generate token
#1-on-1 chat with LINE Notify클릭 >> 프로그램 제목 적기 >> api 복사
#an4SwFGANRsEBg1i6nAwjovJFeBFAZjYSnWgxzx0YX0
import requests

#설명서에 Notification
headers = {'Authorization':'Bearer an4SwFGANRsEBg1i6nAwjovJFeBFAZjYSnWgxzx0YX0'} #Request method #token
data = {"message" : "테스트!"} #Request parameters
requests.post(" https://notify-api.line.me/api/notify", headers = headers, data=data)

#현재 나에게만 라인 Notify로 알림해줌