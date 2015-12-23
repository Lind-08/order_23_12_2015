# -*- coding: utf-8 -*-
# TODO: Написать комментарии

operators = ["+", "-", "*", "/"]


def find(left, right):
    result = []
    for x1 in operators:
        for x2 in operators:
            left_str = "{0}{1}{2}{3}{4}".format(left[0], x1, left[1], x2, left[2])
            res = eval(left_str)
            for x3 in operators:
                for x4 in operators:
                    right_str = "{0}{1}{2}{3}{4}".format(right[0], x3, right[1], x4, right[2])
                    res1 = eval(right_str)
                    if res == res1:
                        result.append("{0} = {1}".format(left_str, right_str))
    return result


if __name__ == "__main__":
    for x in find([63, 9, 28], [7, 4, 7]):
        print(x)