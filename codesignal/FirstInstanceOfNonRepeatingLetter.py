def solution(s):
    map={}
    set_of_s = set(s)
    result=0
    list_of_s=list(dict.fromkeys(s))
    for s_value in set_of_s:
        map[s_value]=0

    for character in s:
        map[character]+=1

    for char in list_of_s:
        result=map.get(char)
        if result==1:
            return char

    return "_"


