# -*- coding: utf-8 -*-
"""
    Общий ход решения.
    Открываем два файла: входной и выходной.
    Построчно считываем входной файл.
    Получаем список элементов строки, разделенных пробелом. Преобразуем их в числа.
    Функция map применяет функцию ко всей коллекции.
    Далее считаем среднее значение, определяя при помощи функций sum
    и len сумму элементов и число элементов соотв.
    После, записываем результат в выходной файл. Надо помнить, что в считанной строке присутствует
    символ конца строки \n. При помощи среза выбираем всю строку до него.
"""


def calculate_average(filename):
    fp = open(filename, "rt")
    fp1 = open("result_" + filename, "w+t")
    for string in fp:
        temp = map(float, string.split(" "))
        avg = sum(temp) / len(temp)
        fp1.writelines(string[:-1] + " {0}\n".format(avg))

if __name__ == "__main__":
    calculate_average("task_11.txt")

