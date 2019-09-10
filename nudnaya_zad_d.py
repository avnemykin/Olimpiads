from math import sqrt
with open('input.txt', 'r') as f_in:
    a,b,c,d = map(int,f_in.readlines())

korny = []

with open('output.txt', 'w') as f_out:
    

    for i in range(0,1001,1):
        if a*(i**3)+b*(i**2)+c*i+d==0:
             korny.append(i)
    
    korny.sort()
    korny = map(str,korny)
    
    f_out.write(" ".join(korny))
        
