def money(func):
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        return '${:,.2f}'.format(return_value)
    return wrapper

def defaul_simple_rates(p,t,i,k):
    S=p*(1+i*t/k)
    return round(S,2)
def changing_simple_rates(p,t,i,k):
    s=0
    for ti,ii,ki in zip(t,i,k):
        s+=ti*ii/ki
    S=p+p*s
    return round(S,2)
def reinvestment_simple_rates(p,t,i,k):
    prod=1
    for ti,ki,ii in zip(t,k,i):
        prod*=1+ti*ii/ki
    S=p*prod
    return round(S,2)
def simple_rates_for_time_changing_sums(r,t,i,k):
    s=0
    for ri,ti in zip(r,t):
        s+=ri*ti
    mn=round(k/i)
    I=s/mn
    return round(I,2)
def single_time_payment(s,n,m):
    R=s/n/m
    return round(R,2)
def discount_prise(s,i,t,k):
    P=s/(1+i*t/k)
    return round(P,2)
def discount(t,k,p,i):
    n=t/k
    D=n*p*i
    return round(D,2)
def bank_accounting_rate(s,p,t,k):
    d=(s-p)/(s*t/k)
    return round(d,2)
def bank_accounting(s,d,t,k):
    P=s-s*d*t/k
    return round(P,2)
