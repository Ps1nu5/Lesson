first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

dict_zip = zip(first, second)
first_result = (len(word1) - len(word2) for word1, word2 in dict_zip if len(word1) != len(word2))
second_result = (len(first[word]) == len(second[word]) for word in range(len(first)))

print(list(first_result))
print(list(second_result))