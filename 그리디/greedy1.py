n = int(input())
cnt = 0

k = int(input())

def minus (a) :
    return a -1

def division (a , b) :
    return a // b

while n != 1 :
    if n % k != 0 :
        n = minus(n)
        cnt += 1

    elif n % k ==0 :
        n = division(n,k)
        cnt += 1

print(cnt)