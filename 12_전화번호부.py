phoneList = []
numOfData = 0 # 현재 추가된 번호가 몇개인지

def inputData(): #1번 메뉴 함수화
    name = input("이름 입력 : ")  # input은 하나당 하나밖에 저장 안된다
    number = input("번호 입력 : ")
    phoneList.append({"name": name, "number": number})
    global  numOfData
    numOfData += 1

def searchData():
    search = input("이름 입력 >> ")
    find = False
    for data in phoneList:
        if search == data["name"]:
            print("-------------")
            print("이름:", data["name"])
            print("번호:", data["number"])
            print("-------------")
            find = True
    if find == False:
        print("-------------")
        print("찾는 이름이 없습니다.")
        print("-------------")


def eraseData():
    erase = input("이름 입력 >> ")
    find = False
    for data in phoneList:
        if erase == data["name"]:
            phoneList.remove(data)
            global numOfData
            numOfData -= 1
            print("-------------")
            print("삭제 되었습니다.")
            print("-------------")
            find = True

    if find == False:
        print("-------------")
        print("찾는 이름이 없습니다")
        print("-------------")


def showAllData():
    for data in phoneList:
        print("-------------")
        print("이름:", data["name"])
        print("번호:", data["number"])
        print("-------------")
while True:
    print("===============")
    print("현재 데이터 개수 : {}개".format(numOfData))
    print("1. 전화번호 추가")
    print("2. 전화번호 검색")
    print("3. 전화번호 삭제")
    print("4. 전화번호 전체 출력")
    print("5. 종료")
    print("===============")
    menu = int(input("선택 >> "))
    if menu == 1:
        inputData() #함수 불러오기
    elif menu == 2:
        searchData()
    elif menu == 3:
        eraseData()
    elif menu == 4:
        showAllData()
    elif menu == 5:
        print("종료되었습니다")
        break
    else:
        print("올바른 번호가 아닙니다")