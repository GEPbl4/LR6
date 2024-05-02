import os
import shutil

def list_files(path):
    """Возвращает список файлов и папок в заданном пути."""
    return os.listdir(path)

def create_directory(path):
    """Создает директорию по заданному пути."""
    os.makedirs(path, exist_ok=True)

def remove_file(path):
    """Удаляет файл по заданному пути."""
    os.remove(path)

def copy_file(source, destination):
    """Копирует файл из исходного пути в целевой путь."""
    shutil.copy2(source, destination)

def move_file(source, destination):
    """Перемещает файл из исходного пути в целевой путь."""
    shutil.move(source, destination)

def rename_file(source, destination):
    """Переименовывает файл или папку."""
    os.rename(source, destination)