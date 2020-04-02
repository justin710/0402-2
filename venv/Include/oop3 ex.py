
class Menu:

    def __init__(self, n, p):
        self.name = n
        self.price = p


class Kiosk:
    def __init__(self):
        self.menu_list = [
            Menu('Americano', 4100),
            Menu('Latte', 4600),
            Menu('Cappuccino', 4600),
            Menu('Mocha', 5100)
        ]

    def start_service(self):
        print("Welcome")
        num = 1
        for menu in self.menu_list:
            print(num, menu.name, menu.price)
            num += 1
        print('---------------------------------------------------------')
        choice = int(input('메뉴 번호를 선택하시오, 0을 누르면 완료\n'))

       # if choice == 0:


        self.start_service()


kiosk = Kiosk()
kiosk.start_service()