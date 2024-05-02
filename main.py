import os
from commands import *  # Импортируем все функции из commands.py
from config import WORKDIR

def main():
    os.chdir(WORKDIR)  # Устанавливаем начальную рабочую директорию

    while True:
        command, *args = input(f"{os.getcwd()}> ").split()  # Получаем команду и аргументы

        if command == "exit":
            break

        try:
            globals()[command](args)  # Выполняем функцию, соответствующую команде
        except KeyError:
            print(f"Неизвестная команда: {command}")

if __name__ == "__main__":
    main()