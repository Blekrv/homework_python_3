from datetime import datetime as date
from lib.DiscountCard import DiscCard

card1 = DiscCard()
try:
    exit = False
    while not exit:
        choice = int(input('1.Інформація про картку\n2. Купити товар з картою на знижку \n3. Інформація про величину знижки \n4. Сумма на яку потрібно купити товаруб щоб знижка збільшилась \n5.Вихід\n'))
        if choice == 1:
            print(f'\n\tНомер картки: {card1.number}\n\tДата видачі: {card1.date}\n')
        elif choice == 2:
            cost = float(input('Вартість товару який ви хочете купити: \t-->'))
            card1.buy(cost)
        elif choice == 3:
            card1.disc_info()
        elif choice == 4:
            card1.disc_dif_info()
        elif choice == 5:
            print('Бувай')
            exit = True
        else:
            print('Зробіть правильний вибір!!!')
except:
    print('Неправильно введені дані!')
# print(card1.number, card1.money, card1.disc, card1.date)

# card1.buy_article(1000)
# card1.buy_article(1500)
# card1.buy_article(1500)
# print(card1.number, card1.money, card1.disc, card1.date)

# card1.discount_info()
# card1.discount_inc_info()