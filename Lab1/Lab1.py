import sys


def get_params():
    try:
        params = [float(i) for i in sys.argv[1:]]
    except:
        print("Ошибка при взятии аргументов из cmd")
    else:
        if len(params) == 3 and params[0] != 0:
            print("Взяты параметры из cmd")
            return params
        else:
            print("Ошибка при взятии аргументов из cmd")

    while len(params) != 3 or params[0] == 0:
        try:
            prompt = "Введите 3 действительных числа через пробел (A, B, C): "
            params = list(map(float, input(prompt).split()))
        except:
            print("Error")
        else:
            if len(params) != 3 or params[0] == 0:
                print("Error")
    return params


def find_roots(arr):
    roots = []
    d = float(arr[1] ** 2 - 4 * arr[0] * arr[2])
    if d == 0:
        x = -arr[1] / (2 * arr[0])
        roots.append(x)
    elif d > 0:
        x1 = (-arr[1] + d ** 0.5) / (2 * arr[0])
        x2 = (-arr[1] - d ** 0.5) / (2 * arr[0])
        if x1 > 0:
            roots.append(x1 ** 0.5)
            roots.append(-(x1 ** 0.5))
        if x2 > 0:
            roots.append(x2 ** 0.5)
            roots.append(-(x2 ** 0.5))
    return roots


def main():
    params = get_params()
    roots = find_roots(params)
    if len(roots) >= 1:
        for el in roots:
            print("X = {:.6}".format(el))
    else:
        print("Корней нет")


if '__main__' == __name__:
    main()
