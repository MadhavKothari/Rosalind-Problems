def run(k,m,n):
    t = k+m+n
    a = t*(t-1)
    d = (k/a)*(k-1+m+n) + (m/a)*(k+((m-1)*0.75)+(n*0.5)) + (n/a)*(k+m*0.5)
    print (d)