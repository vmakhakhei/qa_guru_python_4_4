

def test_greeting():
    name = "Анна"
    age = 25
    # TODO Сформируйте нужную строку
    output = ""
    # Проверяем результат
    assert output == f"Привет, Анна! Тебе 25 лет."


def test_rectangle():
    """
    Напишите программу, берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20

    # TODO сосчитайте периметр
    perimeter = 0
    assert perimeter == 60

    # TODO сосчитайте площадь
    area = 0
    assert area == 200


def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь. Используйте константу PI
    """
    r = 23
    # TODO сосчитайте площадь
    area = 0
    assert area == 1661.9025137490005

    # TODO сосчитайте длину окружности
    length = 0
    assert length == 144.29090290269986


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 и отсортируйте его по возрастанию.
    """

    # TODO создайте список
    l = []
    assert len(l) == 10
    assert l[0] < l[-1]


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # TODO удалите повторяющиеся элементы

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Выведите на экран все значения словаря.
    Подсказка: используй встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    d = {}

    assert isinstance(d, dict)
    assert len(d) == 5
