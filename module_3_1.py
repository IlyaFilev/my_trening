# "Счётчик вызовов"
calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    count_calls()
    long_ = (len(string), string.upper(), string.lower())
    return long_

def is_contains(string, list_to_search):
    count_calls()
    list_to_search_m = [x.lower() for x in list_to_search]
    if string.lower() in list_to_search_m:
        return True
    else:
        return False


print(string_info('CapybarA'))
print(string_info('Armageddon'))
print(string_info('Spaceship'))
print(is_contains('Urban', ['UrBaN', 'qwe']))
print(is_contains('Batut', ['Yakibana', 'BaNaN', 'BAtUT']))
print(is_contains('Orang', ['Oran', 'BaNaN', 'Аpple']))
print(calls)
