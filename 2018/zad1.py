
with open("input.txt","r") as f:
    a = int(f.readline())


with open("output.txt","w") as f:
    summ = a//10 + a%10
    res = a /summ
    n = str(res).find('.')
    drob = str(res)[n+1:]
    



    if int(drob) == 0:
        f.write(str(int(res)))
    elif len(drob)==1:
        f.write("{:3.1f}".format(res))
    elif len(drob)==2:
        f.write("{:3.2f}".format(res))
    else:
        f.write("{:3.3f}".format(res))
