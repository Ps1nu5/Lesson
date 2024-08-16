class WordsFinder(): # создаём клас принимающий неограниченное количество текстовых файлов
    def __init__(self, *file_names):
        self.file_names = file_names

    def find(self, word):
        places = {}
        for key, valye in self.get_all_words.items():
            if word.lover in valye:
                places[key] = valye.index(word.lower())+1
        return places

    def count(self,word):
        counters = {}
        for valye, key in self.get_all_words.items():
            word_count = key.count(word.lower())
            counters[valye] = word_count

        return counters

    @property
    def get_all_words(self):
        all_word = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                info = file.read().lower()
                for syn in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    info = info.replace(syn,'')
                all_word[name] = info.split()

        return all_word





finder2 = WordsFinder('text_file.txt')
print(finder2.get_all_words) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
