def solution(a):
    number=0
    index_main=99999

    set_of_a = set(a)
    map = {}

    if len(a)==len(set_of_a):
        return -1


    for index,num in enumerate(a):
        if num in map:
            map[num].append(index)
        else:
            map[num]=[index]

    for num in set_of_a:

        list_of_index = map.get(num)
        if len(list_of_index)>1:
            list_of_index=sorted(list_of_index)
            for val in list_of_index[1:]:
                if val<index_main:
                    index_main=val
                    number=num


    return number





