
money = 1000

rate = 0.0075

count = 0

# while count < 10:
#총액 = 원금 + (원금 * 이율)

for x in range(1,11):


    money = money + (money*rate)

    print(x, money)
