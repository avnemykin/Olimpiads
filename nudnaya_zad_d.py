with open('output.txt', 'w') as f_out:
    s=''
    if d!=0:
        for i in range(0,1001,d):
            if a*(i**3)+b*(i**2)+c*i+d==0:
                s+=str(i)+' '
    else:
        korny.append(0)
        discr = b**2-4*a*c
        if discr > 0:
            if 0<=int((-b-sqrt(discr))/(2*a))<=1000 :
                korny.append(int((-b-sqrt(discr))/(2*a)))
            if 0<=int((-b+sqrt(discr))/(2*a))<=1000:
                korny.append(int((-b+sqrt(discr))/(2*a)))
                
        elif discr==0:
            if 0<=int((-b)/(2*a))<=1000:
                korny.append(int((-b)/(2*a)))
    korny.sort()
    korny = map(str,korny)
    s = " ".join(korny)
    f_out.write(s)
