import os
from file_utils import (
    list_files,
    create_directory,
    remove_file,
    copy_file,
    move_file,
    rename_file,
)
from config import WORKDIR
import fnmatch
import datetime


def cd(args):
    """Изменяет текущую директорию."""
    if not args:
        print("Использование: cd <путь>")
        return

    new_dir = os.path.join(os.getcwd(), args[0])
    if os.path.isdir(new_dir) and new_dir.startswith(WORKDIR):
        os.chdir(new_dir)
    else:
        print("Ошибка: директория не найдена.")


def ls(args):
    """Отображает список файлов и папок."""
    path = os.getcwd() if not args else os.path.join(os.getcwd(), args[0])
    if os.path.isdir(path) and path.startswith(WORKDIR):
        for entry in list_files(path):
            print(entry)
    else:
        print("Ошибка: директория не найдена.")


def mkdir(args):
    """Создает директорию."""
    if not args:
        print("Использование: mkdir <имя_директории>")
        return

    path = os.path.join(os.getcwd(), args[0])
    if not path.startswith(WORKDIR):
        print("Ошибка: выход за пределы рабочей директории.")
    elif os.path.exists(path):
        print("Ошибка: директория уже существует.")
    else:
        create_directory(path)


def rm(args):
    """Удаляет файл или папку."""
    if not args:
        print("Использование: rm <имя_файла_или_папки>")
        return

    path = os.path.join(os.getcwd(), args[0])
    if not path.startswith(WORKDIR):
        print("Ошибка: выход за пределы рабочей директории.")
    elif not os.path.exists(path):
        print("Ошибка: файл или папка не существует.")
    else:
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            remove_file(path)


def cp(args):
    """Копирует файл или папку."""
    if len(args) != 2:
        print("Использование: cp <источник> <назначение>")
        return

    source = os.path.join(os.getcwd(), args[0])
    destination = os.path.join(os.getcwd(), args[1])
    if not source.startswith(WORKDIR) or not destination.startswith(WORKDIR):
        print("Ошибка: выход за пределы рабочей директории.")
    elif not os.path.exists(source):
        print("Ошибка: исходный файл или папка не существует.")
    else:
        copy_file(source, destination)


def mv(args):
    """Перемещает или переименовывает файл или папку."""
    if len(args) != 2:
        print("Использование: mv <источник> <назначение>")
        return

    source = os.path.join(os.getcwd(), args[0])
    destination = os.path.join(os.getcwd(), args[1])
    if not source.startswith(WORKDIR) or not destination.startswith(WORKDIR):
        print("Ошибка: выход за пределы рабочей директории.")
    elif not os.path.exists(source):
        print("Ошибка: исходный файл или папка не существует.")
    else:
        move_file(source, destination)


def rename(args):
    """Переименовывает файл или папку."""
    if len(args) != 2:
        print("Использование: rename <старое_имя> <новое_имя>")
        return

    old_name = os.path.join(os.getcwd(), args[0])
    new_name = os.path.join(os.getcwd(), args[1])
    if not old_name.startswith(WORKDIR) or not new_name.startswith(WORKDIR):
        print("Ошибка: выход за пределы рабочей директории.")
    elif not os.path.exists(old_name):
        print("Ошибка: файл или папка не существует.") 
    else:
        rename_file(old_name, new_name)

def cat(args):
    """Отображает содержимое файла."""
    if not args:
        print("Использование: cat <имя_файла>")
        return

    path = os.path.join(os.getcwd(), args[0])
    if not path.startswith(WORKDIR):
        print("Ошибка: выход за пределы рабочей директории.")
    elif not os.path.isfile(path):
        print("Ошибка: файл не существует.")
    else:
        try:
            with open(path, "r") as f:
                print(f.read())
        except UnicodeDecodeError:
            print("Ошибка: не удается прочитать файл.")

def info(args):
    """Отображает информацию о файле или папке."""
    if not args:
        print("Использование: info <имя_файла_или_папки>")
        return

    path = os.path.join(os.getcwd(), args[0])
    if not path.startswith(WORKDIR):
        print("Ошибка: выход за пределы рабочей директории.")
    elif not os.path.exists(path):
        print("Ошибка: файл или папка не существует.")
    else:
        print(f"Имя: {os.path.basename(path)}")
        print(f"Размер: {os.path.getsize(path)} байт")
        print(f"Дата последнего изменения: {datetime.datetime.fromtimestamp(os.path.getmtime(path))}")
        print(f"Тип: {'Директория' if os.path.isdir(path) else 'Файл'}")

def find(args):
    """Ищет файлы по имени."""
    if not args:
        print("Использование: find <имя_файла>")
        return

    pattern = args[0]
    for root, _, files in os.walk(WORKDIR):
        for file in files:
            if fnmatch.fnmatch(file, pattern):
                print(os.path.join(root, file))