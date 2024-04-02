""" terno pitagórico para qual a+b+c = 1000  ( para range(1,500) valores menores que 500 eu acho resultado 225 300 475"""

for i in range(1,1000):
    for j in range(1,1000):
            for k in range(1, 1000):
                if pow(i,2)+pow(j,2)== pow(k,2) and (i+j+k == 1000):
                    print(i, j, k)
