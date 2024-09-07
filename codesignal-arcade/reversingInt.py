import math
def solution(n):
    count=int(math.log10(n))
    number=0
    while n>0 and count>=0:
        digit=n%10
        number=number+(10**count)*digit
        count-=1
        n=n//10
    return number