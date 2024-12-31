n = 1000
while n>100:
    result=int(str(n)[0])**3+int(str(n)[1])**3+int(str(n)[2])**3
    if result==n:
        print("The", n ,"is a armstrong number")
    n -= 1
    