import random

def game():
    com = random.randrange(0,3) ##범위에서 시작점은 포함 마지막점은 미포함

    user = int(input('가위 0, 바위 1, 보2 '))

    #만일 컴이 사용자보다 작은 값이면 +3

    if user > com:
        com = com +3

    result = com - user


    if result == 2:
        result_str = 'WIN'

    elif result  == 1:
        result_str ='LOSE'

    else:
        result_str = 'DROW'

    return result_str

before_winner = ''
gamecount = 0

while True:

    result = game()


#    if result =='DROW'


    if before_winner != result:
        before_winner = result
        gamecount = + 1

    else:
        gamecount = gamecount + 1

    if gamecount == 10:
        break


print("------------------------------")
print(before_winner)