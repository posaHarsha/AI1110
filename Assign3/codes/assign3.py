n=int(input("Enter no of Tosses of coin "))
if n<0:
    print("INVALID INPUT")
elif n%2==1:
    for i in range(n+1):
        if i%2==1:
            print(i)
elif n%2==0:
    for i in range(n+1):
        if i%2==0:
            print(i)

