from math import log as ln
def get_n_by_SPi(s,p,i):
    n=ln(s/p)/ln(1+i)
    return n
def get_n_by_SPd(s,p,d):
    n=ln(p/s)/ln(1-d)
    return n
def get_n_by_SPmj(s,p,m,j):
    n=ln(s/p)/(m*ln(1+j/m))
    return n
def get_n_by_SPmf(s,p,m,f):
    n=ln(p/s)/(m*ln(1-f/m))
    return n
def get_i_by_SPn(s,p,n):
    i=(s/p)**(1/n)-1
    return i
def get_d_by_SPn(s,p,n):
    d=1-(p/s)**(1/n)
    return d
def get_j_by_SPmn(s,p,m,n):
    j=((s/p)**(1/m/n)-1)*m
    return j
def get_f_by_SPmn(s,p,m,n):
    f=(1-(p/s)**(1/m/n))*m
    return f
