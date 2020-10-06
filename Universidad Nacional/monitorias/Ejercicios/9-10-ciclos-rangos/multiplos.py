def multiplos():
    n = int(input("digite n:"))
    m = int(input("digite m:"))

    print("Los múltiplos son:")
    for i in range(0,n//m+1,1):
        print(m*i)

multiplos()