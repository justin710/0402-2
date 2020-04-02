from random import randrange

balls = [ x for x in range(1,46)]

#루프를 nums가 6개가 되는동안
balls.pop()

for x in range(6):
    num = randrange(1, 46)
    balls.pop()
    print(balls)



#1부터 45 사이의 숫자를 뽑는다


print(balls)
#뽑은 값이 있다면 다시 뽑는다
