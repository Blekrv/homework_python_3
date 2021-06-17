import random
from datetime import datetime as date

class DiscCard:

    def __init__(self):
        self.__number = random.randint(10000000, 99999999)
        self.__money = 0
        self.__disc = 1
        self.__date = date.now().strftime("%d-%m-%Y")

    def buy(self, cost: float):
        if cost > 0:
            pay = cost - (cost * self.__disc / 100)
            print(
                f'Твоя знижка  {cost * self.__disc / 100} грн. До сплати {pay} грн.')
            confirm = input("Ви хочете продовжити: Y/N --> ")
            if confirm.upper() == 'Y':
                self.__money += pay
                self.__disc = round(
                    self.__money // 1000 + 1) if round(self.__money // 1000 + 1) <= 30 else 30
                print("Все пройшло успішно!\n")
            elif confirm.upper() == 'N':
                print("Бувай!\n")
            else:
                print("Не правильна команда. Спробуйте ще\n")
        else:
            print("Не правильна ціна. Повторіть спробу.\n")

    def disc_info(self):
        print(
            f'Ваша знижка {self.__disc}%.\n')

    def disc_dif_info(self):
        next_lev = self.__disc * 1000 - self.__money
        if next_lev == 0:
            next_lev = 1000
        print(
            f'Ваша знижка {self.__disc}%. Для більшої знижки вам потрібно купити товару на суму не менше ніж {next_lev} грн.\n')

    @property
    def number(self):
        return self.__number

    @property
    def money(self):
        return self.__money

    @property
    def disc(self):
        return self.__disc

    @property
    def date(self):
        return self.__date