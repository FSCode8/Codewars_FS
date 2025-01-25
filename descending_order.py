def descending_order(num):
    numb_list = list(str(num))
    numb_list.sort(reverse=True)
    return int("".join(numb_list))

descending_order(1234)