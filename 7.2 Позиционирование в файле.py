#import io
#from pprint import pprint

def custom_write(file_name, strings):
    with open(file_name, 'w', encoding='utf-8') as file:
        strings_positions = {}

        for i, string in enumerate(strings):
            start_byte = file.tell()
            file.write(string + '\n')
            strings_positions[i+1, start_byte] = string

    return strings_positions



info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']
result = custom_write('file.txt', info)
for elem in result.items():
  print(elem)