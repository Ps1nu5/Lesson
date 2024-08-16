import os
import time

# получаем путь до текущей директории
directory = os.getcwd()
print(directory)

for root, dirs, files in os.walk(directory):
    for file in files:
        # получаем путь до текущего файла
        filepath = os.path.join(root, file)
        # время создания файла
        filetime = os.path.getmtime(filepath)
        # форматированное время создания файла
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        # размер файла
        filesize = os.path.getsize(filepath)
        # родительская директория
        parent_dir = os.path.dirname(filepath)

        print(f'Обнаружен файл: {file},\n'
              f'Путь: {filepath},\n'
              f'Размер: {filesize} байт,\n'
              f'Время изменения: {formatted_time},\n'
              f'Родительская директория: {parent_dir}\n\n')



