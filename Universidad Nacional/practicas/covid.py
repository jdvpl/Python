def main(n,m):
    # n=int(input())
    # m=int(input())
    dia=1
    if(1 <=n <= 10**8 and 1 <= m <= n):
        while (m<n):
            n=n*1.02
            m=m*1.03
            dia+=1
        print(dia)
        print(n)
        print(m)
    else:
        print("error en los datos ingresados ")

x=int(input())
y=int(input())
main(x,y)
x1=int(input())
y2=int(input())
main(x1,y2)