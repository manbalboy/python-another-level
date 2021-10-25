재고량 = 10

if 재고량 > 0 :
    print('지금주문가능합니다.') #indent가 들어가게끔 그니까 들여쓰기를 잘써야 이프문이 먹는다.

중고차재고 = ['K6', 'BMW', 'BENZ']

if 'K5' in 중고차재고 : # in문법 자주 사용함 중고차재고라는 array안에 해당 데이터가 있는가를 확인함
    print('지금주문가능합니다.')
elif 'K6' in 중고차재고 : # else if 가 elif임
    print('k6는 주문 가능함')
else  :
    print('주문불가능하다고!')