def get_n_by_SPi(s,p,i):
    n=(s/p-1)/i
    return n
def get_n_by_SPd(s,p,d):
    n=(1-p/s)/d
    return n
def get_t_by_SPi(s,p,i,k):
    i=get_n_by_SPi(s,p,i)*k
    return i
def get_y_by_SPd(s,p,d,k):
    i=get_n_by_SPd(s,p,d)*k
def get_i_by_SPn(s,p,n):
    i=(s/p-1)/n
    return i
def get_i_by_SPt(s,p,t,k):
    i=(s/p-1)*k/t
    return i
def get_d_by_SPn(s,p,n):
    d=(1-p/s)/n
    return d
def get_d_by_SPt(s,p,t,k):
    d=(1-p/s)*k/t
    return d
