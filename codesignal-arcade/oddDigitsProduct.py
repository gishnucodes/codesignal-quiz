def solution(n):
    flag=False
    product=1
    while n>0:
        digit=n%10
        if digit%2!=0:
            product*=digit
            flag=True
        n=n//10
    if flag==False:
        return 0
    return product

