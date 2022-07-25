def only_square_area(a, b) :
    area = []
    for i in a: 
        if b.count(i) > 0: #a의 원소 i에 대해 b에서 count했을 때, 1개 이상 발견된다면 (=b에 같은 원소가 있다면)
            area.append(i**2) #i를 제곱해서 area에 추가하라
    print(area) #print함수로 결과값 출력, 값을 저장하고 싶으면 따로 return사용

only_square_area([12, 27,20],[27,56,12,35])
