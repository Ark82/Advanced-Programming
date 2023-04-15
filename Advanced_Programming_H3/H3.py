def tuple_max_min_dict(dict_1: dict) -> tuple:
    max_v = min_v = list(dict_1.items())[0][1]
    max_k = min_k = list(dict_1.items())[0][0]
    for i in range(len(dict_1)):
        if list(dict_1.items())[i][1] < min_v:
            min_v = list(dict_1.items())[i][1]
            min_k = list(dict_1.items())[i][0]
        if list(dict_1.items())[i][1] > max_v:
            max_v = list(dict_1.items())[i][1]
            max_k = list(dict_1.items())[i][0]
    return (max_k, min_k)


def list_tuple_dict(dict_1: dict) -> list:
    list_1 = []
    for i in range(len(dict_1)):
        list_1.append((list(dict_1.items())[i][0], list(dict_1.items())[i][1]))
    return list_1


def dict_2lists(list_1: list, list_2: list) -> dict:
    dict_1 = {}
    if len(list_1) > len(list_2):
        min_l = len(list_2)
    else:
        min_l = len(list_1)
    for i in range(min_l):
        dict_1[f"{list_1[i]}"] = list_2[i]
    return dict_1


def tuple_key_values_dict(dict_1: dict, value: int) -> tuple:
    list_1 = []
    for i in range(len(dict_1)):
        if list(dict_1.items())[i][1] == value:
            list_1.append(list(dict_1.items())[i][0])
    return tuple(list_1)


def dict_list_values_2dict(dict_1: dict, dict_2: dict) -> dict:
    for i in range(len(dict_2)):
        if list(dict_2.items())[i][0] in dict_1:
            for j in range(len(dict_1)):
                if list(dict_1.items())[j][0] == list(dict_2.items())[i][0]:
                    dict_2[list(dict_2.items())[i][0]] = [list(dict_1.items())[j][1], list(dict_2.items())[i][1]]
        else:
            dict_2[list(dict_2.items())[i][0]] = [list(dict_2.items())[i][1]]
    for i in range(len(dict_1)):
        if list(dict_1.items())[i][0] in dict_2:
            continue
        else:
            dict_1[list(dict_1.items())[i][0]] = [list(dict_1.items())[i][1]]
    dict_1.update(dict_2)
    return dict_1
