# -*- coding: utf-8 -*-
"""
    Так как, в задаче нам необходимо искать русские буквы, то файл необходимо открывать в кодировке utf-8.
    Для этого используется модуль codecs.
    Далее, построчно считываем файл. Переводим все символы строки в нижний регистр.
    При помощи функции isalpha проверяем, является ли элмент строки буквенным символом.
    Если да, то проверяем его наличие в словаре. Если он есть, то увеличиваем число вхождений на один.
    Иначе оно равно 1.
    В функции print_dict определяем максимальную длину строки для вывода
    из всех. Длина строки определяется как 3 (1 символ + 2 пробела) + длина числа.
    Получаем список кортежей (k, value[k]). Он необходим для сортировки по значениям словаря.
    Производим сортировку списка кортежей. В поле key объявлена lambda-функция(анонимная) для выбора 2-го
    элемента кортежа. Reverse=True означает сортировку по убыванию.
    Затем формируем результирующую строку и выводим ее.
    Функция ljust дополняет заполнителем строку на определенную длину справа.
"""

import codecs


def get_alpha_dict(filename):
    fp = codecs.open(filename, "rt", encoding="UTF-8")
    result = {}
    for string in fp:
        string = string.lower()
        for sym in string:
            if sym.isalpha():
                if sym in result:
                    result[sym] += 1
                else:
                    result[sym] = 1
    return result


def print_dict(value):
    string_len = max([3 + len(str(x)) for x in value.values()])
    value = [(k, value[k]) for k in value.keys()]
    value.sort(key=(lambda x: x[1]), reverse=True)
    for t in value:
        res_str = u"{0}".format(t[0])
        res_str = res_str.ljust(string_len - len(str(t[1])), " ")
        print res_str + str(t[1])


if __name__ == "__main__":
    print_dict(get_alpha_dict("task_13.txt"))