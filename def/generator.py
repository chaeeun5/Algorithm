#제너레이터 생성 함수

def fn_d(n) :
    sum_d = n
    while n > 0:
        sum_d += n % 10
        n = n//10
    return print(sum_d)
fn_d(91)
fn_d(50)