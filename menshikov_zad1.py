with open("input.txt","r") as f:
    m,n = map(int, f.readline().split())
chisla = []
if m<=2:
    chisla.append(str(2))
    if m %2 and m+1<=n:
        m+=1

for i in range(m,n+1,2):
    flug = 0; j = 2;
    while flug<1 and j<i:
        if i %j ==0:
            flug = 1
        j +=1
        
    if flug == 0:
        chisla.append(str(i))
with open("output.txt","w") as f:
    if len(chisla)>0:
        f.write("\n".join(chisla))
    else:
        f.write("Absent")
