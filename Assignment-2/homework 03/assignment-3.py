def rotate(a,r):
    b=[]
    n=len(a)
    for i in range(n-r,n):
        b.append(a[i])
    for i in range(0,n-r):
        b.append(a[i])
    print(b)


a=[]
a = list(map(int, input("Enter numbers: ").split())) 
r=int(input("Enter r: "))
n=len(a)
r=r%n
rotate(a,r)