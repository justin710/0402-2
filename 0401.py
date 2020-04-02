
money = 1000

rate = 0.0075

count = 0

# while count < 10:
#금리 원금 = (원금 * 이율)

while True:
    if count == 10:
        break
    money = money + (money*rate)

    print(count, money)
    count += 1