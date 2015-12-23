# -*- coding: utf-8 -*-
import codecs

# TODO: Написать комментарии


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