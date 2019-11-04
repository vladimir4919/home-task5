import os
import shutil
import sys
import platform

"""
Библиотечные функции
"""
import os

def show_help():
    print('===================================================')
    print('            Консольный файловый менеджер')
    print('===================================================')
    print(' 1 - Создать папку')
    print(' 2 - Удалить (файл/папку)')
    print(' 3 - Копировать (файл/папку)')
    print(' 4 - Просмотр содержимого рабочей директории')
    print(' 5 - Посмотреть только папки')
    print(' 6 - Посмотреть только файлы')
    print(' 7 - Просмотр информации об операционной системе')
    print(' 8 - Создатель программы')
    print(' 9 - Играть в викторину')
    print(' 10 - Мой банковский счет')
    print(' 11 - Смена рабочей директории')
    print(' 0 - Выход')
    print('===================================================')

def create_dir():
    version = input('Ввести имя создаваемой директории: ')
    created_by_dir = os.path.join(os.getcwd(),version)#os.getcwd()- какой путь используется- ,os.path.join-совмещаем
    #используемый путь и новую директорию
    if os.path.exists(created_by_dir):
        print("Директория существует.Использовать другое имя.")
    else:
        os.mkdir(created_by_dir)
        print("Директория успешно создана")


def copy_file_or_dir():

    source = input('Вводим имя файла/папки для копирования: ')
    copy_file_or_dir = input('Вводим  имя файла/папки куда копируем: ')
    if  source == copy_file_or_dir:
        print("ПРЕДУПРЕЖДЕНИЕ. Исходное имя файла/папки совпадает с конечным именем. Повторите операцию.")
    if source != copy_file_or_dir:
        source = os.path.join(os.getcwd(), source)
        copy_file_or_dir = os.path.join(os.getcwd(), copy_file_or_dir)
        if os.path.exists(source):
            if os.path.isfile(source):          # если копируем файл
                shutil.copy2(source, copy_file_or_dir)
                    print("скопировали Файл  ")
            elif os.path.isdir(source):         # если директория -> директорию
                    shutil.copytree(source, copy_file_or_dir)
                    print("скопировали каталог")
        return copy_file_or_dir

def viewing_all_in_working_dir():#Просмотр содержимого рабочей директории
    content_dir = []
    print("Список директорий и файлов в текущем каталоге (с вложенными файлами/каталогами):")
    for elem in os.walk(os.getcwd()):
        content_dir.append(elem)

    for address, dirs, files in content_dir:
        for dir in dirs:
            for file in files:
                print(f"директория: {os.path.join(address, dir)}, файл: {file}")


def get_files_in_working_dir():#Посмотреть только файлы
    print("Список файлов в рабочей директории:")
    print("\n".join(list(filter(lambda x: os.path.isfile(x), os.listdir(".")))))
    print()


def get_dir_in_working_dir():
    print("Список директорий в рабочей директории:")
    print("\n".join(list(filter(lambda x: os.path.isdir(x), os.listdir(".")))))
    print()

def get_system_info():
    print()
    print("Информация о системе:")
    ops, name, oper_ver, build, proc, proc_fam = platform.uname()
    print(f"Операционная система: {ops}")
    print(f"Архитектура: {platform.architecture()}")
    print(f"Платформа: {sys.platform}")
    print(f"Версия операционной системы: {oper_ver}")
    print(f"Релиз операционной системы: {build}")
    print(f"Пользователь системы: {name}")
    print()
    print(f"Архитектура процессора: {proc}")
    print(f"Модель процессора: {proc_fam}")
    print()
    print(f"Версия Python: {' от '.join(platform.python_build())}")
    print(f"Версия компилятора Python: {platform.python_compiler()}")
    print(f"Реализация Python: {platform.python_implementation()}")
    print(f"Папка установки интерпретатора Python: {sys.prefix}")
    print()


def change_working_dir():
    dir = os.getcwd()
    print(f"Текущая рабочая директория: {dir}")
    answer = input('Укажите новую рабочую директорию: -> ')
    try:
        os.chdir(answer)
        print(f"Текущая рабочая директория: {os.getcwd()}")
    except BaseException as e:
        print(f'ОШИБКА. Сообщение: {e.strerror}')
        os.chdir(dir)
        print(f"Текущая рабочая директория не изменилась: {os.getcwd()}")

def del_file_or_dir():
    suggestion= input('Укажите имя файла или папки для удаления -> ')
        desired_name = os.path.join(os.getcwd(),suggestion)
            if os.path.exists(desired_name):  # Объект найден
                if os.path.isfile(desired_name):  # Файл
                    os.remove(desired_name)
                    print("файл удалён")
                elif os.path.isdir(desired_name):  # Директория
                    shutil.rmtree(desired_name)
                    print("директория  удалена")
            else:
                print("Искомый файл/директория не найдена в рабочей  директории")

