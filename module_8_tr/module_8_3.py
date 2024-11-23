# "Создание пользовательских исключений"
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):  # Созданы 2 собственных класса исключений.
    def __init__(self, message):
        self.message = message  # объекты этих классов имеют возможность вывести сообщение в консоль.


class Car:

    def __init__(self, model, vin_number, numbers):
        self.model = model
        if self.__is_valid_vin(vin_number):  # перед созданием объекта, передаем vin на проверку по условиям
            self.__vin = vin_number # Уровень доступа private
        if self.__is_valid_numbers(numbers):  # перед созданием объекта, передаем numbers на проверку по условиям
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        if not (isinstance(vin_number, int) and 1000000 <= vin_number <= 9999999):  # проверяем vin по условиям
            raise IncorrectVinNumber(
                'Неверный диапазон для vin номера')  # генерируем исключение с сообщением (создается объект класса
            # IncorrectVinNumber) которое отлавливаем в блоке try-except
        return True

    def __is_valid_numbers(self, numbers):
        if not (isinstance(numbers, str) and len(numbers) == 6):
            raise IncorrectCarNumbers('Неверная длина номера')
        return True


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)  # выводится переданное сообщение об ошибке
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
