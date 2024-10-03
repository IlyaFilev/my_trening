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
    if string in list_to_search:
        return True
    else:
        return False

print(string_info('Armageddon'))
print(string_info('Armageddon'))
print(string_info('Spaceship'))
print(string_info('Cosmopoliten'))
print(is_contains('Urban', ['ban', 'BaNaN', 'Urban'])) # Urban ~ urBAN
print(is_contains('batut', ['Yakibana', 'BaNaN', 'BAtUT']))

print(calls)