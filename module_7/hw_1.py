with open('test_file.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        print(line, end='')
        print(f.tell())


