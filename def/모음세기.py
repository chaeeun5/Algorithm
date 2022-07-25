def count_vowels(words) :
    sum_v = 0
    for v in ('a', 'e', 'i','o','u') : #모음에 a,e,i,o,u에 대하여
        sum_v += words.count(v) #words에 각각의 모음의 count를 구하고 sum_v에 더하라
    print(sum_v) #print함수로 결과값 출력, 값을 저장하고 싶으면 따로 return사용

count_vowels('apple')
count_vowels('aeiou')

