import os.path
import time
from os.path import getsize, join

directory = r'C:\Users\user\PycharmProjects\Home works\Module_7 работа с файлами и форматированный вывод'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
#        parent_dir = os.path.dirname(r"C:\Users\user\PycharmProjects\Home works")                  
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

