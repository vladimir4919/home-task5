"""
Tесты для всех новых функций в проекте


"""
import os
import pickle
#тест для пункта в console_file_manager""сохранить содержимое рабочей директории в файл""
def test_viewing_output():#тестирование записи содержимого рабочей директории в файл
    with open(LISTDIR, 'w', encoding='UTF-8') as f:
        names_files = ', '.join([elem for elem in os.listdir('.') if os.path.isfile(elem)])
        f.write(f'files: {names_files} \n')
        names_dirs = ', '.join([elem for elem in os.listdir('.') if os.path.isdir(elem)])
        f.write(f'dirs : {names_dirs}')
        f.close()
    with open(LISTDIR, 'r', encoding='UTF-8') as f:
        all_names_files = ', '.join([elem for elem in os.listdir('.')])
        assert f.read()== all_names_files


#функция сохранения истории покупок в файл в bank_account
def purchase(account, history):  # Функция  покупки
    purchase_sum = float(input("\nВводим сумму покупки: "))

    if account - purchase_sum >= 0:
        purchase_name = input("Вводим название покупки:")
        history.append(f"Покупка \"{purchase_name}\" на сумму {purchase_sum}")
        print(f" На счету осталось {account - purchase_sum}")
    with open(FILE_NAME, 'wb') as f:
        pickle.dump(history, f)
    else:
        print("На счету недостаточно средств")
        return account, history
    return account - purchase_sum, history

#модернизируем функцию purchase в purchase1,убрав операции ввода данных с терминала
def purchase1(account, history):  # Функция  покупки
    purchase_sum = 20
    if account - purchase_sum >= 0:
        history.append(f"Покупка nn на сумму {purchase_sum}")
        print(f" На счету осталось {account - purchase_sum}")
    with open(FILE_NAME, 'wb') as f:
        pickle.dump(history, f)
    else:
        print("На счету недостаточно средств")
        return account - purchase_sum, history



#тестирование вновь введенной операции  pickle.dump(history, f)
def test_history_save_listdir():
    account=30
    result=purchase1(account, history)
    if os.path.exists(FILE_NAME1):
        with open(FILE_NAME1, 'rb') as f:
            history_save= pickle.load(history, f)
            assert result ==10,history_save