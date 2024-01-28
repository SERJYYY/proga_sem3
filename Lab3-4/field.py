def field(dicts, *args):
    assert len(args) > 0
    ans = []
    for cur_dict in dicts:
        if len(args) == 1:
            for key in args:
                if cur_dict.get(key) is not None:
                    ans.append(cur_dict.get(key))
        else:
            cur_ans = dict()
            for key in args:
                if cur_dict.get(key) is not None:
                    cur_ans[key] = cur_dict[key]
            ans.append(cur_ans)
    return ans


if __name__ == "__main__":
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    print(field(goods, 'title'))
    print(field(goods, 'title', 'price'))
