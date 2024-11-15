# "Оператор "with" - оператор "with". Сначала пишется выражение, затем добавляется «as» и указывается
# объект, в который всё это сохраняется, после чего выполняется необходимое действие:
# with EXPR as TARG:
#   ACTION

class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names
        print(self.file_names)

    def get_all_words(self):
        for name in self.file_names:
            print(name)
            self.all_words = {}
            with open(name, encoding='utf-8') as file:
                text = (file.read()).lower()
                print(text)
                for p in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    if p in text:
                        text = text.replace(p, '')
                self.all_words.update({name: text.split()})
        return print(self.all_words)






finder2 = WordsFinder('test_file.txt', 'test.txt', 'products.txt')

finder2.get_all_words()
