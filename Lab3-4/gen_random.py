from random import randrange


def gen_random(num_count, begin, end):
    return [randrange(begin, end + 1) for i in range(num_count)]


if __name__ == "__main__":
    print(gen_random(5, 1, 3))
