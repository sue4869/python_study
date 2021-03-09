# 모듈명이랑 파일이름과 같으면 안된다.

import calendar as cal  # import: 모듈을 가져온다. 모듈. 치면 그 모듈 속 함수를 쓸 수 있다

# as를 씀으로써 별명을 붙여줄 수 있다.
# from (모듈명) import (함수명)

cal.prmonth(2020, 9)  # calendar.prmonth(2020,9)
# #모듈. 치면 그 모듈 속 함수를 쓸 수 있다 --> 함수 : 메서드
# calendar을 객체화 : cal.


from calendar import prmonth  # calendar모듈로 부터 prmonth함수 하나만 가져온다
# 메모리적 이득
# 이로써 앞에 cal을 안쓰고 prmonth(2020,9) 가능
