# -*- coding: utf-8 -*-
"""
    Принцип работы схож с task_13. Единственное отличие в том, что здесь используются
    регулярные выражения для выделения слов. Шаблон regexp ищет поледовательность символов от а до я или от
    a до z. Функцией findall получаем список подстрок, удовлетворяющих данному шаблону, т.е., всех слов.
    В функции вывода длина строки определяется как длина слова + 2 + длина цифры.
"""

import re
import codecs


def get_word_dict(filename):
    fp = codecs.open(filename, "rt", encoding="UTF-8")
    regexp = re.compile(u"[a-zа-я]+")
    result = {}
    for string in fp:
        string = regexp.findall(string)
        for sym in string:
            if sym in result:
                result[sym] += 1
            else:
                result[sym] = 1
    return result


def print_dict(value):
    value = [(k, value[k]) for k in value.keys()]
    string_len = max([len(x[0]) + len(str(x[1])) + 2 for x in value])
    value.sort(key=(lambda x: x[1]), reverse=True)
    for t in value:
        res_str = u"{0}".format(t[0])
        res_str = res_str.ljust(string_len - len(str(t[1])), " ")
        print res_str + str(t[1])


if __name__ == "__main__":
    print_dict(get_word_dict("task_13.txt"))
