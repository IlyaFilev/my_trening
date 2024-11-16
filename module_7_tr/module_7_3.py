# "Оператор "with" - оператор "with". Сначала пишется выражение, затем добавляется «as» и указывается
# объект, в который всё это сохраняется, после чего выполняется необходимое действие:
class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                text = (file.read()).lower()
                for simbol in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    if simbol in text:
                        text = text.replace(simbol, '')
            all_words.update({name: text.split()})
        return all_words

    def find(self, word):
        find = {}
        for elem in self.get_all_words().items():
            s = 0
            for i in elem[1]:
                s += 1
                if word.lower() == i:
                    find.update({elem[0]: s})
                    break
        return find

    def count(self, word):
        count = {}
        for elem in self.get_all_words().items():
            s = 0
            for i in elem[1]:
                if word.lower() == i:
                    s += 1
                    count.update({elem[0]: s})
        return count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего