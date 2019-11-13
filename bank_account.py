"""
МОДУЛЬ 3
Программа "Банковский счет"
Работа программы:
Запускаем программу.На счету -0
Программа предлагает:
1. пополнить счет
2. оплатить покупку
3. вывести историю покупок
4. выход

"""
def replenish_balance(account, history):#Функция пополнения баланса
    replenish_sum = float(input("\nВводим сумму пополнения счета: "))
    return account + replenish_sum, history

def purchase(account,history): #Функция  покупки
    purchase_sum = float(input("\nВводим сумму покупки: "))
    if account - purchase_sum >=0:
        purchase_name = input("Вводим название покупки:")
        history.append(f"Покупка \"{purchase_name}\" на сумму {purchase_sum}")
        print(f" На счету осталось {account-purchase_sum}")
    else:
        print("На счету недостаточно средств")
        return account, history
    return account-purchase_sum, history



def print_history(history): #Печать истории изменений баланса счета
    for elem_history in history:
        print(elem_history)
    return


account = 0
history = []
while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    choice = input('Выберите пункт меню:')
    if choice == '1':
        account, history = replenish_balance(account, history)

    elif choice == '2':
        account, history = purchase(account, history)
    elif choice == '3':
        print_history(history)
    elif choice == '4':
        break