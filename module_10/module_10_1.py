import time
from threading import Thread
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, mode='w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            time.sleep(0.01)
        print(f'Завершилась запись в файл {file_name}')


start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

finish = datetime.now()

print(f'Работа функций {finish - start}')

start = datetime.now()

th1 = Thread(target=write_words, args=(10, 'example5.txt'))
th2 = Thread(target=write_words, args=(30, 'example6.txt'))
th3 = Thread(target=write_words, args=(200, 'example7.txt'))
th4 = Thread(target=write_words, args=(100, 'example8.txt'))
th5 = Thread(target=write_words, args=(100, 'example9.txt'))
th6 = Thread(target=write_words, args=(100, 'example10.txt'))
th7 = Thread(target=write_words, args=(100, 'example11.txt'))
th8 = Thread(target=write_words, args=(100, 'example12.txt'))

th1.start()
th2.start()
th3.start()
th4.start()
th5.start()
th6.start()
th7.start()
th8.start()

th1.join()
th2.join()
th3.join()
th4.join()
th5.join()
th6.join()
th7.join()
th8.join()

finish = datetime.now()
print(f'Работа потоков {finish - start}')